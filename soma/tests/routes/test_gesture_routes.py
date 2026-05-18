import pytest 
from fastapi.testclient import TestClient
from app.main import api


@pytest.fixture
def client():
    return TestClient(api)

def test_gesture_detection_route(client: TestClient):
  response = client.post("/v1/gesture-detection/detect")
  assert response.status_code == 200
  
def test_gesture_detection_health_check(client: TestClient):
  response = client.get("/v1/gesture-detection/health")
  assert response.status_code == 200  