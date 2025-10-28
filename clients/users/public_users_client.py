from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import (
    CreateUserRequestSchema, 
    CreateUserResponseSchema
)


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными эндпоинтами /api/v1/users.

    Публичные методы не требуют авторизации, например, создание пользователя.
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создаёт нового пользователя.

        Выполняет POST‑запрос к эндпоинту /api/v1/users.

        :param request: Словарь, содержащий поля email, password,
                        lastName, firstName, middleName.
        :return: httpx.Response, содержащий ответ сервера.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))
    
    # Добавили новый метод
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Создаёт нового пользователя и возвращает его данные из ответа
        """
        response = self.create_user_api(request)
        #return response.json()
        return CreateUserResponseSchema.model_validate_json(response.text)


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())