import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200

def test_history_list(client):
    rv = client.get('/history?from=USD&to=BRL')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert isinstance(json_data['values'], list)
    assert len(json_data['values']) > 0