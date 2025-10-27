# pydantic_create_user.py
"""
В файле определены четыре модели:
* ``UserBaseSchema`` – базовая модель пользователя с общими полями
* ``UserSchema`` – главная сущность пользователя с уникальным идентификатором 
* ``CreateUserRequestSchema`` – схема запроса для создания нового пользователя
* ``CreateUserResponseSchema`` - схема ответа с данными созданного пользователя
"""

import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from pydantic.alias_generators import to_camel


class UserBaseSchema(BaseModel):
    """
    Базовая модель пользователя с общими полями.
    Переиспользуется в запросах и главной сущности.
    """
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = Field(default="user@example.com")
    first_name: str = Field(alias="firstName", default="first_name")
    last_name: str = Field(alias="lastName", default="last_name")
    middle_name: str = Field(alias="middleName", default="middle_name")


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

    password: str = Field(default="secret123", min_length=8)


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа с данными созданного пользователя.
    """
    model_config = UserBaseSchema.model_config

    user: UserSchema = Field(default_factory=UserSchema)
