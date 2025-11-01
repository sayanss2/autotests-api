#tests/test_users.py
from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema
)
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


def test_create_user():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()

    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()

    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)

    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    #assert response.status_code == HTTPStatus.OK, 'Некорректный статус-код ответа'
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    #assert response_data.user.email == request.email, 'Некорректный email пользователя'
    #assert_equal(response_data.user.email, request.email, "email")
    #assert response_data.user.last_name == request.last_name, 'Некорректный last_name пользователя'
    #assert_equal(response_data.user.last_name, request.last_name, "last_name")
    #assert response_data.user.first_name == request.first_name, 'Некорректный first_name пользователя'
    #assert_equal(response_data.user.first_name, request.first_name,  "first_name")
    #assert response_data.user.middle_name == request.middle_name, 'Некорректный middle_name пользователя'
    #assert_equal(response_data.user.middle_name, request.middle_name,  "middle_name")#

    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request=request, response=response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())