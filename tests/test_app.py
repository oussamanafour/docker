from app import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, IFIAG" in response.data

def test_status_route():
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'
                            