from fastapi.testclient import TestClient
from ..main import app
from fastapi_pagination import add_pagination

client = TestClient(app)
add_pagination(app)

def test_read_main():
    response = client.get("/api/v1/vehicle_data/")
    assert response.status_code == 200
    assert response.json()['items']
    assert len(response.json()['items']) > 0

def test_with_param():
    response = client.get("api/v1/vehicle_data/"+"f212b271-f033-444c-a445-560511f95e9c")
    assert response.status_code == 200
    assert response.json()['items']
    assert len(response.json()['items']) > 0

    allIds = []
    for row in response.json()['items']:
        allIds.append(row['vehicle_id'])

    for vehicle_id in allIds:
        assert vehicle_id == "f212b271-f033-444c-a445-560511f95e9c"


