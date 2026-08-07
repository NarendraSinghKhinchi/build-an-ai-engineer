from starlette.testclient import TestClient as TestClient
from talk_to_pdf.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data =  response.json()
    assert data["status"] == "healthy"
    assert "version" in data