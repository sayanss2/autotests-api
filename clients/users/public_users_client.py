from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class CreateUserRequestDict(TypedDict):
    """
    Структура запроса на создание пользователя.

    Поля:
        email (str): Адрес электронной почты.
        password (str): Пароль.
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными эндпоинтами /api/v1/users.

    Публичные методы не требуют авторизации, например, создание пользователя.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт нового пользователя.

        Выполняет POST‑запрос к эндпоинту /api/v1/users.

        :param request: Словарь, содержащий поля email, password,
                        lastName, firstName, middleName.
        :return: httpx.Response, содержащий ответ сервера.
        """
        return self.post("/api/v1/users", json=request)
    
    # Добавили новый метод
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())