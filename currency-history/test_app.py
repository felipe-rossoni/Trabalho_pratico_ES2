import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Testa se /health responde 200"""
    rv = client.get('/health')
    assert rv.status_code == 200

def test_history_list(client):
    """Testa se /history retorna uma lista"""
    rv = client.get('/history?from=USD&to=BRL')
    assert rv.status_code == 200
    
    json_data = rv.get_json()
    # Verifica se existe a chave 'values' e se é uma lista
    assert 'values' in json_data
    assert isinstance(json_data['values'], list)