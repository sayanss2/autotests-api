#tests/test_authentication.py
from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema
)

from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response


def test_login():
    # Инициализируем клиент для публичных операций с пользователями
    public_users_client = get_public_users_client()

    # Инициализируем клиент для аутентификации
    auth_client = get_authentication_client()

    # Создаём объект запроса на создание нового пользователя
    create_user_request = CreateUserRequestSchema()

    # Отправляем запрос на создание пользователя
    public_users_client.create_user(create_user_request)
    
    # Формируем объект запроса на логин, используя данные созданного пользователя
    login_user_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    # Отправляем запрос на аутентификацию и получаем httpx.Response
    login_response = auth_client.login_api(login_user_request)

    # Преобразуем тело ответа в модель LoginResponseSchema
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    
    # Проверяем, что JSON‑ответ соответствует схеме LoginResponseSchema
    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())

    # Проверяем, что статус‑код ответа равен 200 (OK)
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # Проверяем, что токены и тип токена корректны
    assert_login_response(login_response_data)