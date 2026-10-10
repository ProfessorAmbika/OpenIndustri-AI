"""Admin demo mode: unlock every authored level without altering progress."""
from __future__ import annotations

from .conftest import login


def _levels(c):
    grid = c.get("/api/missions").json()
    return grid, [lv for cat in grid["categories"] for lv in cat["levels"] if lv["missionId"]]


def test_demo_unlock_all_levels(client, make_client):
    admin = make_client()
    assert login(admin, "admin.dev", "Admin#2026", "admin").status_code == 200
    assert admin.get("/api/admin/settings").json()["demoUnlockAll"] is False

    assert login(client).status_code == 200
    grid, levels = _levels(client)
    assert grid["demoUnlockAll"] is False
    locked = [lv for lv in levels if lv["status"] == "locked"]
    assert locked, "expected locked levels before demo mode"
    target = locked[-1]["missionId"]
    assert client.post("/api/sessions", json={"missionId": target}).status_code == 403

    r = admin.put("/api/admin/settings", json={"demoUnlockAll": True})
    assert r.status_code == 200 and r.json()["demoUnlockAll"] is True and r.json()["updatedBy"] == "admin.dev"

    grid, levels = _levels(client)
    assert grid["demoUnlockAll"] is True
    assert all(lv["status"] == "available" for lv in levels)
    assert client.post("/api/sessions", json={"missionId": target, "abandonOpen": True}).status_code == 201
    # Nothing is marked as passed by demo mode.
    assert all(not row["passed"] for row in client.get("/api/progress").json()["missions"])

    admin.put("/api/admin/settings", json={"demoUnlockAll": False})
    _, levels = _levels(client)
    assert any(lv["status"] == "locked" for lv in levels)


def test_demo_unlock_admin_only(trainee):
    assert trainee.put("/api/admin/settings", json={"demoUnlockAll": True}).status_code in (401, 403)
    assert trainee.get("/api/admin/settings").status_code in (401, 403)
