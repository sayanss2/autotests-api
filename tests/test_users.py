#tests/test_users.py
from http import HTTPStatus

import pytest  # Импортируем библиотеку pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema
)
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
def test_create_user(
    public_users_client: PublicUsersClient
):
    # Инициализируем API-клиент для работы с пользователями
    # public_users_client = get_public_users_client() #убрали в фикстуру public_users_client

    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()

    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)

    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request=request, response=response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())