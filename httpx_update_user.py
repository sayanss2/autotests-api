import httpx

import json
from tools import get_random_email

# Функция для вывода ответа на печать
def log_response(response, label="Response"):
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"Method: {response.request.method}")
    try:
        data = response.json()
        if data is None or data == {} or data == []:
            print(f"{label}: <нет данных>")
        else:
            print(f"{label}:", json.dumps(data, indent=2))
    except Exception:
        print(f"{label}: <не JSON>")
    print("="*80)

SERVER = "http://127.0.0.1:8000"

client = httpx.Client()

# 1. Создание пользователя
user_create_endpoint = SERVER + "/api/v1/users"
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
user_create_response = client.post(user_create_endpoint, json = create_user_payload)
user_create_data = user_create_response.json()
log_response(user_create_response, "User create")
user_id = user_create_data["user"]["id"]

# 2. Авторизация
user_login_endpoint = SERVER + "/api/v1/authentication/login"
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
user_login_response = client.post(user_login_endpoint, json = login_payload)
user_login_data = user_login_response.json()
log_response(user_login_response, "User login (tokens)")

# 3. Обновление пользователя
user_update_endpoint = SERVER + "/api/v1/users/" + str(user_id)
headers_credentials = {
        "Authorization": f'Bearer ' + user_login_data["token"]["accessToken"]
    }
update_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
user_update_response = client.patch(user_update_endpoint, json = update_payload, headers = headers_credentials)
user_update_data = user_update_response.json()
log_response(user_update_response, "User update")

client.close()