from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

# Импортируем общий кэш
from clients.public_http_builder import _http_clients_cache

class AuthenticationUserDict(TypedDict):  # Структура данных пользователя для авторизации
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    email = user["email"]
    # Если уже есть приватный клиент для пользователя — возвращаем сразу
    if email in _http_clients_cache:
        return _http_clients_cache[email]

    
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    client = Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )

    # Сохраняем клиент под email
    _http_clients_cache[email] = client
    return _http_clients_cache[email]