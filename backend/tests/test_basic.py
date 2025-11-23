# backend/tests/test_basic.py
from app import app
import json

def test_health():
    client = app.test_client()
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_report_create():
    client = app.test_client()
    payload = {
        "user_id": "u001",
        "title": "Broken Well",
        "latitude": 20.59,
        "longitude": 78.96
    }
    res = client.post("/api/reports", json=payload)
    assert res.status_code == 201
    assert "report_id" in res.get_json()
