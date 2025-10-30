import httpx

from tools import log_response
from tools.fakers import fake

SERVER = "http://127.0.0.1:8000"

client = httpx.Client()

user_create_endpoint = SERVER + "/api/v1/users"
create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

user_create_response = client.post(user_create_endpoint, json = create_user_payload)
user_create_data = user_create_response.json()
log_response(user_create_response, "User create")
user_id = user_create_data["user"]["id"]


user_login_endpoint = SERVER + "/api/v1/authentication/login"
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

user_login_response = client.post(user_login_endpoint, json = login_payload)
user_login_data = user_login_response.json()
log_response(user_login_response, "User login (tokens)")


get_user_endpoint = SERVER + "/api/v1/users/" + str(user_id)
headers_credentials = {
        "Authorization": f'Bearer ' + user_login_data["token"]["accessToken"]
    }

get_user_response = client.get(get_user_endpoint, headers = headers_credentials)
get_user_data = get_user_response.json()
log_response(get_user_response, "Get user") 

client.close()