from fastapi.testclient import TestClient

from ..main import app
from fastapi_pagination import add_pagination

client = TestClient(app)
add_pagination(app)

def test_read_main():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json()['items']
    assert len(response.json()['items']) > 0
