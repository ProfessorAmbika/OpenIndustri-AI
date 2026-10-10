"""Mission authoring DSL.

Missions are authored once, in Python, with every player-facing string given
in English, Tamil and Hindi side by side (`T(en, ta, hi)`). `build_content.py`
compiles them into:

* shared/missions/<id>.json        — the validated mission definition (keys only)
* shared/content/questions.generated.json — mission-specific MCQs
* frontend/src/i18n/locales/missions/<lang>.json — lazily loaded text bundles

Gameplay logic is never duplicated per language: all languages map to the same
mission ids, steps and evaluation rules.

Content rules (enforced by review, partly by validation):
* No invented standard clauses, numeric thresholds, exposure limits or
  machine-specific procedures. Scenarios teach awareness-level principles
  (verify, stop, report, escalate) and say so.
* Every document shown in game is a fictional training document.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

LANGS = ("en", "ta", "hi")


@dataclass(frozen=True)
class T:
    en: str
    ta: str
    hi: str

    def __post_init__(self) -> None:
        for lang in LANGS:
            v = getattr(self, lang)
            if not isinstance(v, str) or not v.strip():
                raise ValueError(f"missing {lang} text: {self.en!r}")


# Shared roster of recurring fictional characters. Name/role text lives in the
# base locale (npc.<role>.name / npc.<role>.role) so it is identical everywhere.
ROSTER = ("supervisor", "safety_officer", "senior_tech", "operator", "coordinator", "contractor")

# Default briefing-phase events (the player may walk, talk and look around before acknowledging).
BRIEFING_EVENTS = ["world_entered", "zone_entered", "npc_interacted", "checklist_opened", "hint_requested", "object_inspected"]

# Difficulty model (section 4/11): assistance and hint budgets by level. Safety
# rules, critical classifications and required authorisations never change.
HINTS = {1: (99, 4, 2), 2: (99, 3, 1), 3: (6, 3, 1), 4: (4, 2, 1), 5: (3, 1, 0)}


def assistance_for(level: int) -> dict[str, Any]:
    def prof(detail: str, world: bool, mini: bool, auto: int | None) -> dict[str, Any]:
        return {"objectiveDetail": detail, "worldMarkers": world, "minimapMarkers": mini, "autoHintSeconds": auto}

    if level == 1:
        return {"fresher": prof("full", True, True, 75), "mid": prof("standard", False, True, None), "senior": prof("minimal", False, False, None)}
    if level == 2:
        return {"fresher": prof("full", True, True, 90), "mid": prof("standard", False, True, None), "senior": prof("minimal", False, False, None)}
    if level == 3:
        return {"fresher": prof("full", False, True, 120), "mid": prof("standard", False, True, None), "senior": prof("minimal", False, False, None)}
    if level == 4:
        return {"fresher": prof("standard", False, True, None), "mid": prof("minimal", False, True, None), "senior": prof("minimal", False, False, None)}
    return {"fresher": prof("standard", False, True, None), "mid": prof("minimal", False, False, None), "senior": prof("minimal", False, False, None)}


DEFAULT_REFS = {
    "og_hazard_recognition": ["REF-OISD-STD-154", "REF-HSE-HSG253"],
    "og_ppe": ["REF-OISD-STD-154", "REF-OSHA-1910-132"],
    "og_permit_to_work": ["REF-OISD-STD-105", "REF-HSE-HSG250"],
    "og_loto": ["REF-OSHA-1910-147", "REF-HSE-HSG253"],
    "og_confined_space": ["REF-OSHA-1910-146", "REF-HSE-INDG258", "REF-OISD-STD-105"],
    "og_hot_work": ["REF-OSHA-1910-252", "REF-OISD-STD-105", "REF-HSE-HSG250"],
    "og_fire_hazard": ["REF-OISD-STD-116", "REF-OSHA-1910-157", "REF-OSHA-1910-38"],
    "og_equipment_inspection": ["REF-EMPLOYER-SOP", "REF-OISD-STD-154"],
    "og_emergency_response": ["REF-OSHA-1910-38", "REF-OISD-STD-154"],
}

# The campaign follows a newly inducted mechanical maintenance technician; its nine
# categories are exactly that designation's catalogue. (Offering later levels to other
# designations would leave them locked behind a Level 1 they cannot play.)
CAMPAIGN_DESIGNATIONS = ["og_mech_maint"]


class Mission:
    def __init__(self, *, code: str, id: str, category: str, level: int, minutes: int, title: T, subtitle: T, description: T,
                 location: T, site: str, time: str = "day", spawn: tuple[float, float, float], work_point: tuple[float, float, float],
                 designed_for: list[str] | None = None) -> None:
        self.code = code
        self.id = id
        self.category = category
        self.level = level
        self.texts: dict[str, T] = {}
        self.questions: list[dict[str, Any]] = []
        self.d: dict[str, Any] = {
            "schemaVersion": 2,
            "id": id,
            "version": 1,
            "industry": "oil_gas",
            "department": "plant_maintenance",
            "designations": CAMPAIGN_DESIGNATIONS,
            "roleTitleKey": "mission.common.roleTrainee",
            "designedFor": designed_for or (["fresher"] if level <= 2 else ["fresher", "mid"] if level <= 3 else ["mid", "senior"]),
            "category": category,
            "level": level,
            "estimatedMinutes": minutes,
            "titleKey": self.k("title", title),
            "subtitleKey": self.k("subtitle", subtitle),
            "descriptionKey": self.k("description", description),
            "briefingKeys": [],
            "assignmentKeys": {},
            "learningObjectiveKeys": [],
            "debriefKeys": {},
            "ruleSet": {"status": "provisional", "noticeKey": "mission.common.provisionalNotice"},
            "contentReview": {"status": "draft_unreviewed", "translationStatus": "demonstration_only", "lastModified": "2026-10-09"},
            "referenceIds": DEFAULT_REFS[category],
            "safetyReferences": [],
            "safetyReferencesNoteKey": "mission.common.noReviewedReferences",
            "prerequisites": {"missions": []},
            "scene": {
                "id": "complex",
                "site": site,
                "time": time,
                "spawn": {"x": spawn[0], "z": spawn[1], "heading": spawn[2]},
                "workPoint": {"x": work_point[0], "z": work_point[1], "heading": work_point[2]},
                "cinematic": {"dayKey": f"chapter.{category}.{level}", "locationKey": self.k("location", location), "titleKey": f"m.{code}.title"},
                "restrictedZones": [],
                "environmentIndicators": [],
                "props": [],
            },
            "briefingPhase": {"allowedEvents": BRIEFING_EVENTS},
            "zones": [],
            "npcs": [],
            "dialogues": {},
            "consequencePanels": {},
            "debriefRules": [],
            "interactables": [],
            "evidence": [],
            "decisions": [],
            "decisionGroups": [],
            "inventory": [],
            "tools": [],
            "steps": [],
            "criticalErrors": [],
            "criticalPolicy": {"failAfterTotal": 2},
            "mistakes": [],
            "worldEvents": [],
            "variants": [{"id": "A", "labelKey": "mission.common.variantA", "overrides": {"interactables": {}, "evidence": {}}}],
            "variantPolicy": {"rule": "rotate_by_attempt", "order": ["A"]},
            "mcq": {"questionIds": [], "passFraction": 0.75},
            "hints": {"budget": dict(zip(("fresher", "mid", "senior"), HINTS[level])), "penalty": 2},
            "assistance": assistance_for(level),
            "scoring": {"mistakePenalty": 5, "invalidActionPenalty": 3, "hintPenalty": 2, "criticalPenalty": 25, "masteryThreshold": 90, "passThreshold": 70},
            "authoring": {},
        }

    # ------------------------------------------------------------ text registry
    def k(self, path: str, text: T) -> str:
        if not isinstance(text, T):
            raise TypeError(f"{self.code}.{path}: expected T(...)")
        key = f"m.{self.code}.{path}"
        if key in self.texts:
            raise ValueError(f"duplicate text key {key}")
        prefix = key + "."
        for existing in self.texts:
            if existing.startswith(prefix) or key.startswith(existing + "."):
                raise ValueError(f"text key {key} collides with {existing}")
        self.texts[key] = text
        return key

    def _params(self, base: str, params: dict[str, Any]) -> dict[str, Any]:
        """Register any T found inside prop params; replace it with its key."""
        counter = [0]

        def conv(v: Any) -> Any:
            if isinstance(v, T):
                counter[0] += 1
                return self.k(f"{base}.{counter[0]}", v)
            if isinstance(v, list):
                return [conv(x) for x in v]
            if isinstance(v, tuple):
                return [conv(x) for x in v]
            if isinstance(v, dict):
                return {kk: conv(vv) for kk, vv in v.items()}
            return v

        return conv(params)

    # ------------------------------------------------------------ narrative
    def brief(self, *, lines: list[T], task: T, equipment: T, objective: T, information: T, objectives: list[T]) -> None:
        self.d["briefingKeys"] = [self.k(f"briefing.{i + 1}", t) for i, t in enumerate(lines)]
        self.d["assignmentKeys"] = {
            "assignment": self.k("assignment.task", task),
            "equipment": self.k("assignment.equipment", equipment),
            "objective": self.k("assignment.objective", objective),
            "information": self.k("assignment.information", information),
        }
        self.d["learningObjectiveKeys"] = [self.k(f"objectives.{i + 1}", t) for i, t in enumerate(objectives)]

    def npc(self, role: str, x: float, z: float, heading: float = 180, talk: list[tuple[str, dict[str, Any] | None]] | None = None, max_distance: float = 3.0, hidden_until: str | None = None, briefing: bool = True) -> str:
        """NPC heading: 180 = faces south (towards a player arriving from the gate)."""
        assert role in ROSTER, role
        self.d["npcs"].append({
            "id": role, "nameKey": f"npc.{role}.name", "roleKey": f"npc.{role}.role", "portrait": role,
            "x": x, "z": z, "heading": heading, "maxDistance": max_distance,
            "talk": [{"dialogue": name, **({"when": when} if when else {})} for name, when in (talk or [])],
            **({"hiddenUntil": hidden_until} if hidden_until else {}),
        })
        if briefing and self.d["scene"].get("briefingNpc") is None:
            self.d["scene"]["briefingNpc"] = role
        return role

    def dialogue(self, name: str, lines: list[tuple]) -> str:
        """lines: (speaker, mood, T) or (speaker, mood, T, [(label T, group, value, next|None), ...])."""
        out = []
        for i, ln in enumerate(lines):
            speaker, mood, text = ln[0], ln[1], ln[2]
            entry: dict[str, Any] = {"speaker": speaker, "textKey": self.k(f"dlg.{name}.{i + 1}", text), "mood": mood}
            if len(ln) > 3:
                entry["choices"] = [
                    {"labelKey": self.k(f"dlg.{name}.{i + 1}c{j + 1}", lab), "group": grp, "value": val, **({"next": nxt} if nxt else {})}
                    for j, (lab, grp, val, nxt) in enumerate(ln[3])
                ]
            out.append(entry)
        self.d["dialogues"][name] = out
        return name

    # ------------------------------------------------------------ world
    def decor(self, type: str, x: float, z: float, heading: float = 0, state: str | None = None, key: str | None = None, **params: Any) -> None:
        if key:
            params["key"] = key
        prop: dict[str, Any] = {"type": type, "x": x, "z": z, "heading": heading, "params": self._params(f"prop.{key or len(self.d['scene']['props'])}", params)}
        if state:
            prop["state"] = state
        self.d["scene"]["props"].append(prop)

    def obj(self, id: str, prop: str, x: float, z: float, heading: float = 0, *, name: T | str, details: list[T], kind: str = "equipment",
            panel: str = "inspect", prompt: str = "inspect", groups: list[str] | None = None, hidden_until: str | None = None,
            doc_kind: str | None = None, state: str | None = None, max_distance: float = 3.0, **params: Any) -> str:
        name_key = name if isinstance(name, str) else self.k(f"obj.{id}.name", name)
        self.d["interactables"].append({
            "id": id, "nameKey": name_key, "type": kind, "actions": ["inspect"], "maxDistance": max_distance,
            "promptKey": f"world.prompt.{prompt}",
            "detailKeys": [self.k(f"obj.{id}.d{i + 1}", t) for i, t in enumerate(details)],
            "panel": panel, "groups": groups or [], "hiddenUntil": hidden_until, "docKind": doc_kind,
        })
        p: dict[str, Any] = {"id": id, "type": prop, "x": x, "z": z, "heading": heading, "params": self._params(f"prop.{id}", params)}
        if state:
            p["state"] = state
        self.d["scene"]["props"].append(p)
        return id

    def zone(self, id: str, name: T, rect: tuple[float, float, float, float], restricted: bool = False) -> str:
        min_x, max_x, min_z, max_z = rect
        self.d["zones"].append({"id": id, "nameKey": self.k(f"zone.{id}", name), "minX": min_x, "maxX": max_x, "minZ": min_z, "maxZ": max_z})
        if restricted:
            self.d["scene"]["restrictedZones"].append(id)
        return id

    def evidence(self, id: str, label: T, value: T, complete: bool, doc: str | None = None) -> str:
        e: dict[str, Any] = {"id": id, "labelKey": self.k(f"ev.{id}.label", label), "statusKey": self.k(f"ev.{id}.value", value), "complete": complete}
        if doc:
            e["doc"] = doc
        self.d["evidence"].append(e)
        return id

    def item(self, id: str, at: str, icon: str, name: T, detail: T, defect: bool = False) -> str:
        self.d["inventory"].append({"id": id, "nameKey": self.k(f"item.{id}.name", name), "icon": icon, "detailKey": self.k(f"item.{id}.detail", detail), "at": at, "defect": defect})
        return id

    def group(self, id: str, prompt: T, options: list[tuple], ui: str = "choice") -> str:
        """options: (value, label T) or (value, label T, desc T) or (value, label T, desc T|None, route)."""
        self.d["decisionGroups"].append({"id": id, "promptKey": self.k(f"grp.{id}.prompt", prompt), "ui": ui})
        for opt in options:
            value, label = opt[0], opt[1]
            d: dict[str, Any] = {"value": value, "labelKey": self.k(f"grp.{id}.{value}", label), "group": id}
            if len(opt) > 2 and opt[2] is not None:
                d["descKey"] = self.k(f"grp.{id}.{value}_desc", opt[2])
            if len(opt) > 3:
                d["route"] = [list(p) for p in opt[3]]
            self.d["decisions"].append(d)
        return id

    def tools(self, *ids: str, flashlight: list[str] | None = None) -> None:
        defs = {
            "flashlight": {"id": "flashlight", "nameKey": "tool.flashlight.name", "descKey": "tool.flashlight.desc", "allowedTargets": flashlight or [], "requiresTarget": True},
            "spanner": {"id": "spanner", "nameKey": "tool.spanner.name", "descKey": "tool.spanner.desc", "allowedTargets": [], "requiresTarget": True},
            "radio": {"id": "radio", "nameKey": "tool.radio.name", "descKey": "tool.radio.desc", "allowedTargets": ["*"], "requiresTarget": False},
        }
        self.d["tools"] = [defs[i] for i in ids]

    def event(self, id: str, when: dict[str, Any], actions: list[dict[str, Any]], delay: float = 0) -> None:
        conv = []
        for i, a in enumerate(actions):
            a = dict(a)
            if a.get("type") == "banner":
                a["textKey"] = self.k(f"evt.{id}.{i + 1}", a.pop("text"))
            if a.get("type") == "details":
                a["detailKeys"] = [self.k(f"evt.{id}.{i + 1}d{j + 1}", t) for j, t in enumerate(a.pop("details"))]
            conv.append(a)
        self.d["worldEvents"].append({"id": id, "when": when, "delay": delay, "actions": conv})

    # ------------------------------------------------------------ rules
    def meet(self, npc: str, scene: str = "meet", points: int = 5) -> str:
        sid = f"meet_{npc}"
        self.d["steps"].append({
            "id": sid, "titleKey": f"story.step.meet.{npc}", "trigger": {"type": "npc_interacted", "target": npc}, "requires": [],
            "points": points, "marker": npc, "concept": "situational_awareness", "outOfOrder": "ignore", "scene": scene,
            "hintKeys": [f"story.hint.meet.{npc}"],
        })
        return sid

    def briefing(self, requires: str, points: int = 5) -> str:
        self.d["steps"].append({
            "id": "briefing", "titleKey": "story.step.briefing", "trigger": {"type": "briefing_acknowledged"}, "requires": [requires],
            "points": points, "concept": "situational_awareness", "outOfOrder": "ignore", "scene": "briefing", "hintKeys": ["story.hint.briefing"],
        })
        return "briefing"

    def step(self, id: str, *, title: T, instruction: T, trigger: dict[str, Any], requires: list[str], points: int, concept: str,
             hints: list[T], scene: str, marker: str | None = None, optional: bool = False, mistake_if_early: T | None = None,
             condition: dict[str, Any] | None = None) -> str:
        s: dict[str, Any] = {
            "id": id, "titleKey": self.k(f"step.{id}", title), "trigger": trigger, "requires": requires, "points": points,
            "marker": marker, "concept": concept, "outOfOrder": "mistake" if mistake_if_early else "ignore", "scene": scene,
            "hintKeys": [self.k(f"hint.{id}.{i + 1}", h) for i, h in enumerate(hints)], "optional": optional,
        }
        self.k(f"instruction.{id}", instruction)
        if mistake_if_early:
            s["outOfOrderKey"] = self.k(f"early.{id}", mistake_if_early)
        if condition:
            s["condition"] = condition
        self.d["steps"].append(s)
        return id

    def critical(self, id: str, *, trigger: dict[str, Any], concept: str, explanation: T, missing: T, dialogue: str | None = None,
                 condition: dict[str, Any] | None = None, flag: str = "unsafe_attempt") -> str:
        c: dict[str, Any] = {
            "id": id, "trigger": trigger, "response": "block", "setsFlag": flag, "concept": concept,
            "explanationKey": self.k(f"crit.{id}.why", explanation), "missingKey": self.k(f"crit.{id}.missing", missing),
        }
        if dialogue:
            c["dialogue"] = dialogue
        if condition:
            c["condition"] = condition
        self.d["criticalErrors"].append(c)
        return id

    def mistake(self, id: str, *, trigger: dict[str, Any], kind: str, feedback: T, concept: str, condition: dict[str, Any] | None = None) -> str:
        m: dict[str, Any] = {"id": id, "trigger": trigger, "kind": kind, "feedbackKey": self.k(f"fb.{id}", feedback), "concept": concept}
        if condition:
            m["condition"] = condition
        self.d["mistakes"].append(m)
        return id

    def debrief(self, *, success: T, critical: T, failed: T, lines: list[tuple[dict[str, Any], T]]) -> None:
        self.d["debriefKeys"] = {"success": self.k("debrief.success", success), "critical": self.k("debrief.critical", critical), "failed": self.k("debrief.failed", failed)}
        self.d["debriefRules"] = [{"when": w, "textKey": self.k(f"debrief.l{i + 1}", t)} for i, (w, t) in enumerate(lines)]

    def comic(self, title: T, panels: list[tuple[str, T]]) -> None:
        self.d["consequencePanels"]["principle"] = {
            "titleKey": self.k("comic.title", title),
            "panelKeys": [self.k(f"comic.p{i + 1}", t) for i, (_, t) in enumerate(panels)],
            "art": [a for a, _ in panels],
        }

    def report(self, evidence: list[str], decisions: list[str]) -> None:
        self.d["report"] = {"evidenceSteps": evidence, "decisionSteps": decisions}

    def mcq(self, n: int, *, concept: str, stem: T, options: list[T], correct: str, explanation: T, refs: list[str] | None = None) -> None:
        qid = f"{self.code.upper()}-Q{n}"
        letters = "abcd"
        self.questions.append({
            "id": qid, "version": 1, "missionIds": [self.id], "concept": concept,
            "stemKey": self.k(f"q{n}.stem", stem),
            "options": [{"id": letters[i], "textKey": self.k(f"q{n}.{letters[i]}", o)} for i, o in enumerate(options)],
            "correct": correct, "explanationKey": self.k(f"q{n}.why", explanation),
            "referenceIds": refs or self.d["referenceIds"][:1], "reviewStatus": "draft_unreviewed",
        })
        self.d["mcq"]["questionIds"].append(qid)

    def spec(self, **fields: Any) -> None:
        """Trainer-facing scenario specification (English; not shown to trainees)."""
        self.d["authoring"] = {
            "language": "en",
            "note": "Trainer-facing scenario specification. Conceptual training scenario; not an industrial SOP. All content awaits subject-matter-expert review.",
            **fields,
        }

    def variants(self, variants: list[dict[str, Any]]) -> None:
        """variants: [{id, label T, interactables: {id: [T...]}, evidence: {id: T}}]."""
        out = []
        for v in variants:
            ov_i = {oid: {"detailKeys": [self.k(f"var{v['id']}.{oid}.d{j + 1}", t) for j, t in enumerate(ts)]} for oid, ts in v.get("interactables", {}).items()}
            ov_e = {eid: {"statusKey": self.k(f"var{v['id']}.{eid}", t)} for eid, t in v.get("evidence", {}).items()}
            out.append({"id": v["id"], "labelKey": self.k(f"variant.{v['id']}", v["label"]), "overrides": {"interactables": ov_i, "evidence": ov_e}})
        self.d["variants"] = out
        self.d["variantPolicy"] = {"rule": "rotate_by_attempt", "order": [v["id"] for v in out]}

    def build(self) -> dict[str, Any]:
        assert self.d["mcq"]["questionIds"], f"{self.code}: no MCQ"
        assert self.d["debriefKeys"], f"{self.code}: no debrief"
        assert self.d["consequencePanels"], f"{self.code}: no comic"
        assert self.d["authoring"], f"{self.code}: no spec"
        return self.d


# Trigger helpers ---------------------------------------------------------------
def inspect(target: str) -> dict[str, Any]:
    return {"type": "object_inspected", "target": target}


def inspect_any(*targets: str) -> dict[str, Any]:
    return {"type": "object_inspected", "targets": list(targets)}


def flag(target: str) -> dict[str, Any]:
    return {"type": "evidence_flagged", "target": target}


def any_flag() -> dict[str, Any]:
    return {"type": "evidence_flagged"}


def decide(group: str, value: str) -> dict[str, Any]:
    return {"type": "decision_made", "target": group, "value": value}


def select(item: str) -> dict[str, Any]:
    return {"type": "item_selected", "target": item}


def enter(zone: str) -> dict[str, Any]:
    return {"type": "zone_entered", "target": zone}


def talk(npc: str) -> dict[str, Any]:
    return {"type": "npc_interacted", "target": npc}


def tool(tool_id: str, *targets: str) -> dict[str, Any]:
    t: dict[str, Any] = {"type": "tool_used", "value": tool_id}
    if len(targets) == 1:
        t["target"] = targets[0]
    elif targets:
        t["targets"] = list(targets)
    return t


def done(*steps: str) -> dict[str, Any]:
    return {"completed": list(steps)}


def not_done(*steps: str) -> dict[str, Any]:
    return {"notCompleted": list(steps)}
