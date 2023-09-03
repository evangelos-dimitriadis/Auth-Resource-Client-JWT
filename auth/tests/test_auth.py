def test_register_correct(client):
    data = {'username': 'test', 'password': 'test'}
    response = client.post('/register', json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 201
    assert response.json.get('auth_token') is not None


def test_login_no_user(client):
    data = {'username': 'test', 'password': 'test'}
    response = client.post('/login', json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 404


def test_register_login(client):
    # Register a new user
    data = {'username': 'test', 'password': 'test'}
    response = client.post('/register', json=data)
    assert response.status_code == 201

    # Try to login with newly created user
    response = client.post('/login', json=data)
    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert response.json.get('auth_token') is not None
