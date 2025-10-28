import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl, IPvAnyAddress, FilePath
from pydantic.alias_generators import to_camel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True  # Значение по умолчанию

user1 = User(
    id=1, 
    name="Alice", 
    email="alice@example.com",
    address=Address(city="New York", zip_code="10001")
)
print(user1)

user2 = User(
    id="123", 
    name="Alice", 
    email="alice@example.com", 
    address={"city": "New York", "zip_code": "10001"}
)
print(user2.id)  # 123 (автоматически преобразован в int)
print(user2.model_dump_json())  # Выводит JSON-строку


class ConfigSchema(BaseModel):
    email: EmailStr
    site: HttpUrl
    ip: IPvAnyAddress
    file: FilePath

# Пример успешной валидации
cfg = ConfigSchema(
    email="admin@example.com",
    site="https://example.com",
    ip="192.168.0.1",
    file="C:/Windows/explorer.exe"
)
print(cfg)


class UserBaseSchema(BaseModel):
    """
    Базовая модель пользователя с общими полями.
    Переиспользуется в запросах и главной сущности.
    """
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(default="user@example.com")
    first_name: str = Field(alias="firstName", default="First")
    last_name: str = Field(alias="lastName", default="Last")
    middle_name: str = Field(alias="middleName", default="Middle")


class UserSchema(UserBaseSchema):
    """
    Главная сущность пользователя с уникальным идентификатором.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class CreateUserRequestSchema(UserBaseSchema):
    """
    Схема запроса для создания нового пользователя.
    """
    model_config = UserBaseSchema.model_config

    password: str = Field(min_length=8)


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа с данными созданного пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user: UserSchema

user_json_request = """
{
  "email": "user@example.com",
  "password": "string123",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
"""
user_request_json_model = CreateUserRequestSchema.model_validate_json(user_json_request)
print(user_request_json_model.model_dump_json(indent=2))

user_json_response = """
{
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}
"""
user_response_json_model = CreateUserResponseSchema.model_validate_json(user_json_response)
print(user_response_json_model.model_dump_json(indent=2))