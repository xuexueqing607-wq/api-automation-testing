
import pytest
import requests

URL = "http://127.0.0.1:8001/login"

@pytest.mark.parametrize(
    "username,password,expected_status",
    [
        ("admin", "123456", 200),
        ("admin", "wrong", 401),
        ("test", "123456", 401),
        ("admin", "", 401),
        ("", "123456", 401),
        ("","",401),
    ],
    ids=[
        "TC-001-valid-login",
        "TC-002-wrong-password",
        "TC-003-wrong-username",
        "TC-004-empty-password",
        "TC-005-empty-username",
        "TC-006-empty-all",
    ]
)
def test_login(username, password, expected_status):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(URL, json=data, timeout=5)

    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json()["message"] == "login success"
    else:
        assert response.json()["message"] == "invalid credentials"


