from pydantic import BaseModel, EmailStr, Field, ConfigDict

from tools.fakers import fake


class UserBaseSchema(BaseModel):
    """
    Структура базового класса для всех моделей.

    Поля:
        email (EmailStr): Адрес электронной почты.
        last_name (str): Фамилия пользователя.
        first_name (str): Имя пользователя.
        middle_name (str): Отчество пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class UserSchema(UserBaseSchema):
    """
    Описание структуры пользователя.

    Схема, представляющая пользователя в ответах API.
    Добавлено поле `id`, уникальный идентификатор пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str


class CreateUserRequestSchema(UserBaseSchema):
    """
    Структура запроса на создание пользователя.

    Поля:
        email (EmailStr): Адрес электронной почты.
        password (str): Пароль.
        last_name (str): Фамилия пользователя.
        first_name (str): Имя пользователя.
        middle_name (str): Отчество пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    password: str = Field(default_factory=fake.password)
    
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.

    Ответ сервера после успешного создания пользователя.
    Содержит объект `user` с полной информацией о созданном пользователе.
    """
    model_config = ConfigDict(populate_by_name=True)

    user: UserSchema


class UpdateUserRequestSchema(UserBaseSchema):
    """
    Описание структуры запроса на обновление пользователя.

    Поля:
    - email (EmailStr | None): Электронная почта пользователя.
    - last_name (str | None): Фамилия пользователя.
    - first_name (str | None): Имя пользователя.
    - middle_name (str | None): Отчество пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Структура ответа обновления пользователя.

    Ответ сервера после обновления пользователя.
    Возвращает обновлённый объект `user`.
    """
    model_config = ConfigDict(populate_by_name=True)

    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.

    Ответ сервера при запросе информации о пользователе.
    Содержит объект `user` с актуальными данными.
    """
    model_config = ConfigDict(populate_by_name=True)

    user: UserSchema