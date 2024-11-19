import pytest
from flask import Flask
from main import app  # Remplacez "your_flask_app" par le nom de votre fichier principal

# Configure le test client de Flask
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_addition(client):
    # Envoie une requête GET à l'endpoint /add avec les paramètres val1=1 et val2=2
    response = client.get('/add?val1=1&val2=2')
    
    # Vérifie que la réponse est valide (code HTTP 200)
    assert response.status_code == 200
    
    # Vérifie que le résultat dans la réponse est correct
    json_data = response.get_json()
    assert "result" in json_data
    assert json_data["result"] == "1.00 + 2.00 = 3.00"
