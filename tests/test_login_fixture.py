
import requests


def test_login_success(base_url):
    url = base_url + "/login"

    data = {
        "username": "admin",
        "password": "123456"
    }

    response = requests.post(url, json=data, timeout=5)

    assert response.status_code == 200
    assert response.json()["message"] == "login success"
