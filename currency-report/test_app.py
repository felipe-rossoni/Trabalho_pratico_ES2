import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['status'] == 'UP'

def test_quote_structure(client):
    rv = client.get('/quote')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'price' in json_data
    assert json_data['from'] == 'USD'