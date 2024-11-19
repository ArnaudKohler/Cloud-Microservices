

def test_addition(client):
    response = client.get('/add?val1=1&val2=2')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "result" in json_data
    assert json_data["result"] == "1.00 + 2.00 = 3.00"

def test_subtraction(client):
    response = client.get('/subtract?val1=5&val2=3')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "result" in json_data
    assert json_data["result"] == "5.00 - 3.00 = 2.00"

def test_division_by_zero(client):
    response = client.get('/divide?val1=5&val2=0')
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data["error"] == "Cannot divide by 0!"

def test_invalid_operation(client):
    response = client.get('/invalid?val1=1&val2=2')
    assert response.status_code == 404  # Car l'endpoint n'existe pas
