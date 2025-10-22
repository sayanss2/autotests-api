import httpx

from tools import log_response


login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
login_responce_data = login_response.json()
log_response(login_response)

client = httpx.Client(
    base_url="http://127.0.0.1:8000", 
    timeout=100,
    headers={"Authorization": f"Bearer {login_responce_data['token']['accessToken']}"}
)

get_user_me_response = client.get("/api/v1/users/me")
#get_user_me_response_data = get_user_me_response.json()
log_response(get_user_me_response)

client.close()