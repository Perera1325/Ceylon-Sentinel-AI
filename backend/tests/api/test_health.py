import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/v1/health")
    # Our health endpoint might return 503 if DB is down, or 200 with stats.
    # We just ensure it responds with a known JSON structure or status.
    assert response.status_code in [200, 503]
    if response.status_code == 200:
        assert "status" in response.json()
