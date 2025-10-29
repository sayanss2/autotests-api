from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import (
    CreateUserRequestSchema,
    GetUserResponseSchema
)
from clients.private_http_builder import AuthenticationUserSchema
from tools.fakers import get_random_email
from tools.assertions.schema import validate_json_schema

# 1. Создаём публичного клиента и создаём пользователя
public_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="Ivanov",
    first_name="Ivan",
    middle_name="Ivanovich"
)
create_user_response = public_client.create_user(create_user_request)
created_user_id = create_user_response.user.id

# 2. Аутентифицируемся и создаём приватного клиента
auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_client = get_private_users_client(auth_user)

# 3. Получаем данные о пользователе
get_user_response = private_client.get_user_api(created_user_id)
user_data_json = get_user_response.json()

# 4. Генерируем JSON‑схему из модели ответа
user_response_schema = GetUserResponseSchema.model_json_schema()

# 5. Валидируем ответ
try:
    validate_json_schema(instance=user_data_json, schema=user_response_schema)
    print("JSON schema validation passed for user data.")
except Exception as exc:
    print(f"Ошибка при проверке схемы JSON: {exc}")