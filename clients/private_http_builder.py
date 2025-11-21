from pydantic import BaseModel, EmailStr

from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema

# Импортируем общий кэш
from clients.public_http_builder import _http_clients_cache
#from functools import lru_cache #Альтернатива _http_clients_cache


# Добавили суффикс Schema вместо Dict
class AuthenticationUserSchema(BaseModel, frozen=True):  # Структура данных пользователя для авторизации
    email: EmailStr
    password: str


# @lru_cache(maxsize=None)  # Кешируем возвращаемое значение. Альтернатива _http_clients_cache
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    email = user.email
    # Если уже есть приватный клиент для пользователя — возвращаем сразу
    if email in _http_clients_cache:
        return _http_clients_cache[email]

    
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    # Значения теперь извлекаем не по ключу, а через атрибуты
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    client = Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        # Значения теперь извлекаем не по ключу, а через атрибуты
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )

    # Сохраняем клиент под email
    _http_clients_cache[email] = client
    return _http_clients_cache[email]