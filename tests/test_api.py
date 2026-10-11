from fastapi.testclient import TestClient

from backend.main import app


def test_health():
    c = TestClient(app)
    assert c.get("/api/health").json()["ok"]


def test_sun():
    c = TestClient(app)
    j = c.get("/api/sun?lat=13.08&lon=80.27").json()
    assert -90 <= j["solar_elevation_deg"] <= 90


def test_brief_fallback():
    c = TestClient(app)
    j = c.post(
        "/api/brief",
        json={"pocket": {"name": "T", "lat": 1, "lon": 1}, "weather": {"current": {}}, "minutes": 20, "needs": []},
    ).json()
    assert "text" in j and len(j["text"]) > 20
