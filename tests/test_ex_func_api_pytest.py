# tests/test_example_api_pytest.py
import pytest
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema, 
    GetUserResponseSchema
)


@pytest.fixture
def public_client() -> PublicUsersClient:
    """Возвращает публичного клиента для создания пользователей."""
    return get_public_users_client()


@pytest.fixture
def create_user_request() -> CreateUserRequestSchema:
    """Генерируем данные запроса на создание пользователя."""
    return CreateUserRequestSchema()


@pytest.fixture
def created_user(
    public_client: PublicUsersClient, 
    create_user_request: CreateUserRequestSchema
) -> CreateUserResponseSchema:
    """Создаём пользователя через PublicUsersClient и возвращаем ответ."""

    response = public_client.create_user(create_user_request)
    # Проверяем, что пользователь успешно создан
    assert response is not None
    assert hasattr(response, "user")
    return response


@pytest.fixture
def private_client(create_user_request: CreateUserRequestSchema) -> PrivateUsersClient:
    """Возвращаем приватного клиента для авторизованного пользователя."""
    auth_user = AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password
)
    return get_private_users_client(auth_user)


# Тесты
#@pytest.mark.skip(reason="Для тестового запуска")
def test_create_and_get_user(created_user: CreateUserResponseSchema, private_client: PrivateUsersClient):
    """Сценарий: создаём пользователя и получаем его через приватный API."""
    user_id = created_user.user.id

    # Используем метод get_user
    #get_user_response: GetUserResponseSchema = private_client.get_user(user_id)
    get_user_response = private_client.get_user(user_id)

    # Проверки
    assert get_user_response is not None
    assert get_user_response.user.id == user_id
    assert get_user_response.user.email is not None
    # Проверяем наличие хотя бы одного из полей имени
    assert get_user_response.user.first_name is not None
    assert get_user_response.user.last_name is not None

    # Опционально: вывод в консоль (для локального дебага)
    print("Create user data:", created_user.model_dump())
    print("Get user data:", get_user_response.model_dump_json(indent=2))