import pytest
from typing import Any


# Фикстура, которая будет автоматически вызываться для каждого теста
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("\n[AUTOUSE] Отправляем даныне в сервис аналитики")


# Фикстура для инициализации настроек автотестов на уровне сессии
@pytest.fixture(scope="session")
def settings():
    print("\n[SESSION] Инициализируем настройки автотестов")


# Фикстура для создания данных пользователя, которая будет выполняться один раз на класс тестов
@pytest.fixture(scope="class")
def user():
    print("\n[CLASS] Создаем данные пользователя один раз на тестовый класс")


# Фикстура для инициализации API клиента, выполняющаяся для каждого теста
@pytest.fixture(scope="function")
def users_client(settings):
    print("\n[FUNCTION] Создаем API клиента на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass


@pytest.fixture
def user_data() -> Any:
    print("\nСоздаем данные пользователя до теста (setup)")
    yield {
        "name": "test",
        "email": "test@gmail.com"
    }
    print("\nУдаляем данные пользователя после теста (teardown)")


def test_user_email(user_data: dict):
    assert user_data["email"] == "test@gmail.com"


def test_user_name(user_data: dict):
    assert user_data["name"] == "test"
