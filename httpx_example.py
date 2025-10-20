import httpx

import json
import time
from functools import wraps

client_jsonplaceholder = httpx.Client()
client_httpbin = httpx.Client()

def log_response(func):
    """Декоратор для логирования HTTP-запросов и ответов с обработкой ошибок"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)

            print("=" * 80)
            print(f"➡️ URL: {response.url}")
            print(f"➡️ Method: {response.request.method}")
            print(f"➡️ Status: {response.status_code}")
            print(f"➡️ Request headers: {response.request.headers}")

            # безопасная проверка тела запроса
            try:
                if response.request.is_stream_consumed and response.request.content:
                    print(f"➡️ Request body: {response.request.content[:200]}")
                else:
                    print("➡️ Request body: <streamed or unavailable>")
            except Exception:
                print("➡️ Request body: <not accessible>")

            print("-" * 80)

            # обработка HTTP ошибок
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                print(f"❌ HTTP error: {exc}")
            else:
                # выводим JSON или текст
                try:
                    print("📦 Response JSON:")
                    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
                except Exception:
                    print("📜 Response text:")
                    print(response.text[:500])

            print("=" * 80 + "\n")
            return response

        # отдельная обработка таймаута
        except httpx.TimeoutException as exc:
            print(f"⏰ Timeout error: {exc}")
            return None

        # отдельная обработка сетевых ошибок
        except httpx.NetworkError as exc:
            print(f"🌐 Network error: {exc}")
            return None

        # все остальные ошибки запросов
        except httpx.RequestError as exc:
            print(f"❌ Request error: {exc}")
            return None

    return wrapper

def retry(max_retries=3, delay=1):
    """
    Декоратор для повторных попыток HTTP-запросов.
    Используется отдельно от логирования.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except (httpx.TimeoutException, httpx.NetworkError, httpx.RequestError) as exc:
                    attempt += 1
                    if attempt > max_retries:
                        print(f"❌ All {max_retries} retries failed: {exc}")
                        return None
                    print(f"⚠️ Attempt {attempt} failed: {exc}, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


#response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def get_jsonplaceholder_todos_1():
    return client_jsonplaceholder.get("https://jsonplaceholder.typicode.com/todos/1")
get_jsonplaceholder_todos_1()



#data = {
#    "title": "Новая задача",
#    "completed": False,
#    "userId": 1
#}

#response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def post_jsonplaceholder_todos():
    data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
    }
    return client_jsonplaceholder.post("https://jsonplaceholder.typicode.com/todos/", json=data)
post_jsonplaceholder_todos()



#data = {
#    "username": "test_user",
#    "password": "12345"
#}

#response = httpx.post("https://httpbin.org/post", data=data)
#
#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def post_httpbin_data():
    data = {
    "username": "test_user",
    "password": "12345"
    }
    return client_httpbin.post("https://httpbin.org/post", data=data)
post_httpbin_data()



#headers = {
#    "Authorization": "Bearer test_token"
#}

#response = httpx.get("https://httpbin.org/get", headers=headers)

#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def get_httpbin_headers():
    headers = {
    "Authorization": "Bearer test_token"
    }
    return client_httpbin.get("https://httpbin.org/get", headers=headers)
get_httpbin_headers()



#params = {
#    "userId": 1,
#}

#response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def get_jsonplaceholder_todos_params():
    params = {
    "userId": 1
    }
    return client_jsonplaceholder.get("https://jsonplaceholder.typicode.com/todos", params=params)
get_jsonplaceholder_todos_params()



#files = {
#    "file": ("xml_example.xml", open('xml_example.xml', 'rb'))
#}

#response = httpx.post("https://httpbin.org/post", files=files)
#
#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#print(json.dumps(response.json(), indent=2))

@log_response
def post_httpbin_files():
    files = {
    "file": ("xml_example.xml", open('xml_example.xml', 'rb'))
    }
    return client_httpbin.post("https://httpbin.org/post", files=files)
post_httpbin_files()



#with httpx.Client() as client:
#    response1 = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#    response2 = httpx.get("https://jsonplaceholder.typicode.com/todos/2")
#print(json.dumps(response1.json(), indent=2))
#print(json.dumps(response2.json(), indent=2))

@log_response
def get_jsonplaceholder_todos_id(todo_id):
    return client_jsonplaceholder.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
for i in range(1,3):
    get_jsonplaceholder_todos_id(i)



client_httpbin_headers = httpx.Client(headers={"Authorization": "Bearer test_token"})
@log_response
def get_httpbin_headers():
    return client_httpbin_headers.get("https://httpbin.org/get")
get_httpbin_headers()


#response = httpx.get("https://jsonplaceholder.typicode.com/todos/invalid")
#print(response.url)
#print(response.status_code)
#print(response.request.headers)
#try:
#    response.raise_for_status()
#except httpx.HTTPStatusError as exc:
#    print("❌ HTTP error:", exc)
#else:
#    print(json.dumps(response.json(), indent=2))

@log_response
def get_jsonplaceholder_todos_invalid():
    return client_jsonplaceholder.get("https://jsonplaceholder.typicode.com/todos/invalid")
get_jsonplaceholder_todos_invalid()


@log_response
def get_httpbin_timeout():
    return client_httpbin.get("https://httpbin.org/delay/5", timeout=1)
get_httpbin_timeout()


@retry(max_retries=3, delay=1)
@log_response
def get_httpbin_timeout():
    return client_httpbin.get("https://httpbin.org/delay/2")
get_httpbin_timeout()


client_jsonplaceholder.close()
client_httpbin.close()
client_httpbin_headers.close()

#client.close()