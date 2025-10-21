import httpx

from tools import log_response
from tools import get_random_email

SERVER = "http://127.0.0.1:8000"

client = httpx.Client()

user_create_endpoint = SERVER + "/api/v1/users"

req_body = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

user_create_response = client.post(user_create_endpoint, json = req_body)

log_response(user_create_response, "User create")