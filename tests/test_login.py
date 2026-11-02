
import requests

URL = "http://127.0.0.1:8001/login"


# TC-001：正确账号和密码
def test_login_success():
    data = {
        "username": "admin",
        "password": "123456"
    }

    response = requests.post(URL, json=data, timeout=5)

    assert response.status_code == 200
    assert response.json()["message"] == "login success"


# TC-002：错误密码
def test_login_wrong_password():
    data = {
        "username": "admin",
        "password": "wrong"
    }

    response = requests.post(URL, json=data, timeout=5)

    assert response.status_code == 401
    assert response.json()["message"] == "invalid credentials"


# TC-003：错误用户名
def test_login_wrong_username():
    data = {
        "username": "test",
        "password": "123456"
    }

    response = requests.post(URL, json=data, timeout=5)

    assert response.status_code == 401
    assert response.json()["message"] == "invalid credentials"


# TC-004：空密码
def test_login_empty_password():
    data = {
        "username": "admin",
        "password": ""
    }

    response = requests.post(URL, json=data, timeout=5)

    assert response.status_code == 401
    assert response.json()["message"] == "invalid credentials"
