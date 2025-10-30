from pydantic import BaseModel, EmailStr, Field

from tools.fakers import fake


class TokenSchema(BaseModel):  # Добавили структуру с токенами аутентификации
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel): # Добавили структуру запроса на аутентификацию
    """
    Описание структуры запроса на аутентификацию.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel): # Добавили структуру запроса на обновление токена
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)