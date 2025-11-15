#tests/test_authentication.py
from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema
)

from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response

from tests.conftest import UserFixture


@pytest.mark.regression
@pytest.mark.authentication
def test_login(
    function_user: UserFixture,    # Используем фикстуру для создания пользователя
    authentication_client: AuthenticationClient    # Используем фикстуру для создания клиента аутентификации
):
    """
    Тест на аутентификацию пользователя.
    """
    
    # Формируем объект запроса на логин, используя данные созданного пользователя
    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )

    # Отправляем запрос на аутентификацию и получаем httpx.Response
    response = authentication_client.login_api(request)

    # Преобразуем тело ответа в модель LoginResponseSchema
    response_data = LoginResponseSchema.model_validate_json(response.text)
    
    # Проверяем, что JSON‑ответ соответствует схеме LoginResponseSchema
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    # Проверяем, что статус‑код ответа равен 200 (OK)
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что токены и тип токена корректны
    assert_login_response(response_data)