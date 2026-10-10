"""Generic validation and play-through suite run for EVERY mission in the
catalogue. Each mission must be solvable, every critical rule must be
reachable and must block mastery, every mistake rule must fire, duplicates
must not score twice, and every category must progress L1→L5 through the real
HTTP API including the knowledge check and server-side unlocks."""
from __future__ import annotations

import copy

import pytest

from app import engine
from app.config import Settings
from app.content import load_catalogue, load_missions, load_questions
from app.scoring import assess

from .solver import Run, synth

SETTINGS = Settings()
MISSIONS = load_missions(SETTINGS.shared_dir)
IDS = list(MISSIONS)
QUESTIONS = load_questions(SETTINGS.shared_dir)


def mission(mid):
    return MISSIONS[mid][0]


@pytest.mark.parametrize("mid", IDS)
def test_solution_path_reaches_mastery(mid):
    m = mission(mid)
    run = Run(m)
    run.solve()
    assert run.st.state == engine.COMPLETED
    res = assess(m, run.st, run.ctx, "completed")
    assert res["outcome"] == "mastery" and res["score"] == 100
    assert res["counters"]["criticalErrors"] == 0 and res["counters"]["mistakes"] == 0


@pytest.mark.parametrize("mid", IDS)
def test_structure(mid):
    m = mission(mid)
    required = [s for s in m.steps if not s.optional]
    assert 6 <= len(required) <= 20, "8–15 meaningful beats expected (incl. meet/briefing)"
    assert any(s.trigger.type == "decision_made" for s in required), "at least one decision checkpoint"
    assert m.criticalErrors, "an incorrect (unsafe) branch is required"
    assert len(m.mcq.questionIds) >= 4
    for qid in m.mcq.questionIds:
        q = QUESTIONS[qid]
        assert q.correct in {o.id for o in q.options}
    kinds = {s.trigger.type for s in required}
    assert len(kinds) >= 4, f"interactions too uniform: {kinds}"
    # MCQs are mission-specific (never recycled across missions).
    for qid in m.mcq.questionIds:
        assert QUESTIONS[qid].missionIds == [mid]


def _inject_at_earliest(m, rule, max_steps=60):
    """Play the solution until `rule` can fire, then fire it. Returns (run, result)."""
    run = Run(m)
    for _ in range(max_steps):
        ev = synth(rule.trigger, m)
        if engine.rule_ok(rule.condition, run.st) and run.st.state == engine.ACTIVE:
            probe = copy.deepcopy(run.st)
            r = engine.apply(m, probe, {**ev, "seq": run.seq + 1}, run.ctx)
            if r.get("ruleId") == rule.id:
                return run, run.emit(ev)
        if run.step_once() is None:
            break
    raise AssertionError(f"{m.id}: rule {rule.id} never becomes reachable")


@pytest.mark.parametrize("mid", IDS)
def test_every_critical_rule_blocks_and_prevents_mastery(mid):
    m = mission(mid)
    for rule in m.criticalErrors:
        run, r = _inject_at_earliest(m, rule)
        assert r["outcome"] == "critical_block" and r["ruleId"] == rule.id, (rule.id, r)
        assert run.emit({"type": "block_acknowledged"})["outcome"] in ("unblocked", "step_completed")
        run.solve()
        assert run.st.state == engine.COMPLETED, rule.id
        res = assess(m, run.st, run.ctx, "completed")
        assert res["outcome"] == "critical_error", rule.id
        assert rule.concept in res["missedConcepts"]


@pytest.mark.parametrize("mid", IDS)
def test_second_critical_error_fails_attempt(mid):
    m = mission(mid)
    rule = m.criticalErrors[0]
    run, r = _inject_at_earliest(m, rule)
    run.emit({"type": "block_acknowledged"})
    again = run.emit(synth(rule.trigger, m))
    if engine.rule_ok(rule.condition, run.st) or again["outcome"] == "critical_fail":
        assert again["outcome"] == "critical_fail"
        assert run.st.state == engine.FAILED
        assert assess(m, run.st, run.ctx, "critical_failure")["outcome"] == "not_passed"


@pytest.mark.parametrize("mid", IDS)
def test_mistake_rules_fire(mid):
    m = mission(mid)
    expected = {"incorrect_decision": "mistake", "invalid_action": "invalid_action", "advisory": "advisory"}
    for rule in m.mistakes:
        run = Run(m)
        fired = None
        for _ in range(60):
            if engine.rule_ok(rule.condition, run.st) and run.st.state == engine.ACTIVE:
                probe = copy.deepcopy(run.st)
                r = engine.apply(m, probe, {**synth(rule.trigger, m), "seq": run.seq + 1}, run.ctx)
                if r.get("ruleId") == rule.id:
                    fired = run.emit(synth(rule.trigger, m))
                    break
            if run.step_once() is None:
                break
        assert fired is not None, f"{mid}: mistake rule {rule.id} never fires"
        assert fired["outcome"] == expected[rule.kind]


@pytest.mark.parametrize("mid", IDS)
def test_duplicates_never_score_twice(mid):
    m = mission(mid)
    run = Run(m)
    done_event = None
    while run.st.state != engine.COMPLETED:
        cur = run.current()
        ev = synth(cur.trigger, m)
        run.step_once()
        if ev["type"] in ("object_inspected", "item_selected") and done_event is None:
            done_event = ev
            before = (list(run.st.completed), copy.deepcopy(run.st.counters))
            r = run.emit(ev)
            assert r["outcome"] in ("duplicate", "no_effect", "advisory", "prerequisite_missing"), r
            assert run.st.completed == before[0]
    assert done_event is not None
    assert assess(m, run.st, run.ctx, "completed")["score"] == 100


@pytest.mark.parametrize("mid", IDS)
def test_final_decision_out_of_order_is_not_rewarded(mid):
    m = mission(mid)
    decision_steps = [s for s in m.steps if s.trigger.type == "decision_made" and not s.optional]
    final = decision_steps[-1]
    run = Run(m)
    # Play only until the briefing is acknowledged, then try to jump to the final decision.
    while run.st.state == engine.BRIEFING:
        run.step_once()
    r = run.emit(synth(final.trigger, m))
    assert final.id not in run.st.completed
    assert r["outcome"] in ("mistake", "prerequisite_missing")


# ---------------------------------------------------------------- full API play-through per category
def _categories():
    cats: dict[str, list[str]] = {}
    for mid in IDS:
        m = mission(mid)
        cats.setdefault(m.category, []).append(mid)
    return {c: sorted(v, key=lambda x: mission(x).level) for c, v in cats.items()}


CATS = _categories()


def _play_api(c, mid, *, critical: bool = False):
    s = c.post("/api/sessions", json={"missionId": mid, "abandonOpen": True})
    assert s.status_code == 201, s.text
    sid = s.json()["id"]
    eff = c.get(f"/api/sessions/{sid}/mission").json()
    from app.content import MissionDef

    m = MissionDef.model_validate({k: v for k, v in eff.items() if k != "activeVariant"})
    run = Run(m)
    if critical:
        rule = m.criticalErrors[0]
        run, _ = _inject_at_earliest(m, rule)
        run.emit({"type": "block_acknowledged"})
    run.solve()
    events = [{"seq": e["seq"], "type": e["type"], "target": e.get("target"), "value": e.get("value")} for e, _ in run.log]
    # Send in two batches with a restore in between (interrupted-session behaviour).
    half = len(events) // 2
    r1 = c.post(f"/api/sessions/{sid}/events", json={"events": events[:half]})
    assert r1.status_code == 200, r1.text
    restored = c.get(f"/api/sessions/{sid}")
    assert restored.status_code == 200 and len(restored.json()["events"]) == half
    r2 = c.post(f"/api/sessions/{sid}/events", json={"events": events[half:]})
    assert r2.status_code == 200, r2.text
    assert all(x["accepted"] for x in r1.json()["results"] + r2.json()["results"]), [x for x in r1.json()["results"] + r2.json()["results"] if not x["accepted"]]
    result = c.get(f"/api/sessions/{sid}/result").json()
    return sid, result


@pytest.mark.parametrize("category", sorted(CATS))
def test_category_progression_through_api(trainee, category):
    mids = CATS[category]
    for i, mid in enumerate(mids):
        m = mission(mid)
        grid = trainee.get("/api/missions").json()["categories"]
        cat = next(cc for cc in grid if cc["category"] == category)
        slot = next(lv for lv in cat["levels"] if lv["level"] == m.level)
        assert slot["status"] == "available", (mid, slot)
        if m.level < 5:
            nxt = next((lv for lv in cat["levels"] if lv["level"] == m.level + 1), None)
            if nxt and nxt["missionId"]:
                assert nxt["status"] == "locked"
        if i == 0:
            # A critical attempt first: completes, but neither mastery nor progression.
            sid, res = _play_api(trainee, mid, critical=True)
            assert res["outcome"] == "critical_error"
            ans = {q: QUESTIONS[q].correct for q in m.mcq.questionIds}
            out = trainee.post(f"/api/sessions/{sid}/mcq", json={"answers": ans}).json()
            assert out["learning"]["criteriaMet"] is False
        sid, res = _play_api(trainee, mid)
        assert res["outcome"] == "mastery", (mid, res["outcome"])
        mcq = trainee.get(f"/api/sessions/{sid}/mcq").json()
        assert all("correct" not in q for q in mcq["questions"])
        ans = {q: QUESTIONS[q].correct for q in m.mcq.questionIds}
        out = trainee.post(f"/api/sessions/{sid}/mcq", json={"answers": ans}).json()
        assert out["passed"] and out["learning"]["criteriaMet"]
        prog = trainee.get("/api/progress").json()
        row = next(r for r in prog["missions"] if r["mission_id"] == mid)
        assert row["passed"] and row["learning_met"]


def test_catalogue_lists_every_authored_mission():
    cat = load_catalogue(SETTINGS.shared_dir)
    assert set(cat.missions) == set(IDS)
    slots = {(mission(m).category, mission(m).level) for m in IDS}
    assert len(slots) == len(IDS), "two missions in one category/level slot"


@pytest.mark.parametrize("mid", IDS)
def test_critical_triggers_during_briefing_never_crash(mid):
    """Before the briefing is acknowledged, rule triggers must not raise (no BRIEFING→BLOCKED)."""
    m = mission(mid)
    for rule in m.criticalErrors:
        run = Run(m)
        r = run.emit(synth(rule.trigger, m))
        assert r["outcome"] not in ("critical_block", "critical_fail")
        assert run.st.state == engine.BRIEFING
