import httpx
import json

login_payload = {
  "email": "test@test.loc",
  "password": "123456789"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("URL:", login_response.url,  "\n")
print("Login response:", json.dumps(login_response_data, indent=2), "\n")
print("Status code:", login_response.status_code, "\n")

refresh_payload = {
  "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("URL:", refresh_response.url,  "\n")
print("Refresh response:", json.dumps(refresh_response.json(), indent=2))
print("Status code:", refresh_response.status_code, "\n")