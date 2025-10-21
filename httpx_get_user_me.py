import httpx
import json

SERVER = "http://127.0.0.1:8000"

login_payload = {
  "email": "test@test.loc",
  "password": "123456789"
}

def log_response(response, label="Response"):
    """Выводит на печать ответ с метками"""
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    try:
        print(f"{label}:", json.dumps(response.json(), indent=2))
    except Exception:
        print(f"{label}: <не JSON>")
    print("="*80)


with httpx.Client() as client:
    login_endpoint = SERVER + "/api/v1/authentication/login"
    login_response = client.post(login_endpoint, json=login_payload)
    login_response_data = login_response.json()

    log_response(login_response, "Login response")

    headers_credentials = {
        "Authorization": f'Bearer ' + login_response_data["token"]["accessToken"]
    }

    me_endpoint = SERVER + "/api/v1/users/me"
    users_me_response = client.get(me_endpoint, headers = headers_credentials)
    user_me_data = users_me_response.json()

    log_response(users_me_response, "Users me response")