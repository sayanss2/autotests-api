# tests/test_example_api_pytest_class.py
import pytest
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import (
    CreateUserRequestSchema, 
    GetUserResponseSchema
)


# Фикстуры
@pytest.fixture(scope="class")
def public_client():
    """Возвращает публичного клиента для создания пользователей."""
    return get_public_users_client()


@pytest.fixture(scope="class")
def create_user_request():
    """Генерируем данные запроса на создание пользователя."""
    return CreateUserRequestSchema()


@pytest.fixture(scope="class")
def created_user(public_client, create_user_request):
    """Создаём пользователя через PublicUsersClient и возвращаем ответ."""
    response = public_client.create_user(create_user_request)
    # Проверяем, что пользователь успешно создан
    assert response is not None
    assert hasattr(response, "user")
    return response


@pytest.fixture(scope="class")
def private_client(create_user_request):
    """Возвращаем приватного клиента для авторизованного пользователя."""
    auth_user = AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    return get_private_users_client(auth_user)


# Класс с тестами
@pytest.mark.usefixtures("public_client", "create_user_request", "created_user", "private_client")
class TestUserAPI:
    """Тесты для сценария создания и получения пользователя."""

    def test_create_and_get_user(self, created_user, private_client):
        """Сценарий: создаём пользователя и получаем его через приватный API."""
        user_id = created_user.user.id

        # Используем метод get_user
        get_user_response: GetUserResponseSchema = private_client.get_user(user_id)

        # Проверки
        assert get_user_response is not None
        assert get_user_response.user.id == user_id
        assert get_user_response.user.email is not None
        assert get_user_response.user.first_name is not None
        assert get_user_response.user.last_name is not None

        # Опционально: вывод в консоль
        print("Create user data:", created_user.model_dump())
        print("Get user data:", get_user_response.model_dump_json(indent=2))