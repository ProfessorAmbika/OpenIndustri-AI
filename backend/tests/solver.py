"""Deterministic mission solver used by the generic mission test-suite and the
cross-engine vector generator. It plays a mission through the real engine by
always performing the current objective's trigger, and can inject rule
triggers (critical errors, mistakes) at the earliest point they apply."""
from __future__ import annotations

from typing import Any

from app import engine
from app.content import MissionDef, Trigger


def synth(t: Trigger, mission: MissionDef | None = None) -> dict[str, Any]:
    ev: dict[str, Any] = {"type": t.type, "target": None, "value": None}
    if t.target is not None:
        ev["target"] = t.target
    elif t.targets:
        ev["target"] = t.targets[0]
    elif t.type == "evidence_flagged" and mission is not None:
        # An untargeted flag rule (e.g. 'wrong flag'): flag something that is NOT an issue.
        ok = [e.id for e in mission.evidence if e.complete] + [i.id for i in mission.inventory if not i.defect]
        ev["target"] = ok[0] if ok else None
    if t.value is not None:
        ev["value"] = t.value
    return ev


class Run:
    def __init__(self, mission: MissionDef, pathway: str = "standard") -> None:
        self.m = mission
        self.st = engine.EngineState()
        engine.start(self.st)
        self.ctx = engine.Context(pathway=pathway, hintBudget=99)
        self.seq = 0
        self.log: list[tuple[dict[str, Any], dict[str, Any]]] = []

    def emit(self, ev: dict[str, Any]) -> dict[str, Any]:
        self.seq += 1
        e = {**ev, "seq": self.seq}
        r = engine.apply(self.m, self.st, e, self.ctx)
        self.log.append((e, r))
        return r

    def current(self):
        return engine.current_step(self.m, self.st, self.ctx)

    def step_once(self) -> dict[str, Any] | None:
        cur = self.current()
        if cur is None:
            return None
        return self.emit(synth(cur.trigger, self.m))

    def solve(self, max_events: int = 200) -> None:
        for _ in range(max_events):
            if self.st.state in engine.TERMINAL:
                return
            cur = self.current()
            if cur is None:
                return
            r = self.step_once()
            assert r is not None and r["outcome"] == "step_completed", f"{self.m.id}: step {cur.id} did not complete: {r}"
        raise AssertionError(f"{self.m.id}: solver did not finish")


def solution_events(mission: MissionDef) -> list[dict[str, Any]]:
    run = Run(mission)
    run.solve()
    return [e for e, _ in run.log]
