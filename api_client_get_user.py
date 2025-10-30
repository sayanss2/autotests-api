from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import CreateUserRequestSchema, get_public_users_client

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema() # Создаем запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response.model_dump())

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Используем метод get_user
get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response.model_dump_json(indent=2))