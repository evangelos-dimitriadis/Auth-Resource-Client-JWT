from flask import g
from server.routes import get_user


OLD_TOKEN = """eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2OTM0OTA4ODQsImlhdCI6MTY5MzQ5MDU4NCwic3ViIjo4fQ.ZFbA4Dt9RCVTCLbnax2ZJAb95LLmNI0CVw-BIcFDY6TNjjcnu4DF-eGQ3g41dqXl_hLM_vWLTWNzuG_SFFjVzwWfwdx4czD08VmFCkANA_ksd7bhztlSIjN-Wd5xqduM1dx_9KDCmB-HwYZpgdN4_brP3aa7cu2RvJa8VOfyjNzCu8nSvEu-bT9dNZPdN0kEf9T6ZR7trI-7O_BhIH3NZ_YeXz7mcltZI8jDk0Mx2fgBckeXFPzqi5wWT_u0aAhf8qicuvJGZNNX7ZNk_Izvspc1FyaClCWg9902Vugq9RmEiOtAH_2hVoIA5di124vyYtoJEm8MrVKEJn5mti4duAcL52HLrHmQwdVxezqPYs3WJS5J7kv9sBtZZGF9LBMh5NB9M8j3LKHEXuQqL4Q_Hn_4TYCG9Vaobid0X7XWmr8xRDK5MDTxLqbN8SJ7pP6P0FAkJvk022EUce2ec_MCeyM_imwE8KbH4KOvXIMBK8_r8s1RVVcVRgTa6sAv73JnL76gpRFxPqaraVDHQW1Ymi3mn-IB4eAB6XEV13ioteCcsFaH1tyeS3_T1kkyT0QDJhVLKcCJIisBVlkA1Y7L_aK-J_7O2h1yiVaFcZu5scHozYO33Pv8_3HDWy1z_zvUNJOODpmNnt7JiZ0BeEGqVjctpU0dB_YnkMHVogXVXlM"""


def test_jwt_token_needed(client):
    response = client.get('/user')
    assert response.status_code == 404


def test_get_user(app):
    with app.test_request_context():
        g.user_info = 'test'
        response = get_user()
    assert response.json == {'result': 'test'}


def test_jwt_expired_token(client):
    headers = {'Authorization': f'Bearer {OLD_TOKEN}'}
    response = client.get('/user', headers=headers)
    assert response.content_type == 'application/json'
    assert response.status_code == 403
    assert response.json == {'Error': 'Signature expired. Please login again.'}


def test_jwt_invalid_token(client):
    headers = {'Authorization': 'Bearer Invalid-Token'}
    response = client.get('/user', headers=headers)
    assert response.content_type == 'application/json'
    assert response.status_code == 403
    assert response.json == {'Error': 'Invalid token. Please login.'}
