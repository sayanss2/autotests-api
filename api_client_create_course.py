from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import (
    UpdateCourseRequestSchema,
    CreateCourseRequestSchema,
    GetCoursesQuerySchema
)

from tools.fakers import fake

# Инициализируем клиенты
public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema() # Создаем запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

#Обновляем курс
update_course_request = UpdateCourseRequestSchema(
    description=fake.text()
)
update_course_response = courses_client.update_course(
    create_course_response.course.id, 
    update_course_request
)
print('Update course data:', update_course_response)

# Получаем курсы
get_courses_response = courses_client.get_courses(
    GetCoursesQuerySchema(user_id=create_user_response.user.id)
)
print('Get course data by user id:', get_courses_response)

get_course_response = courses_client.get_course(create_course_response.course.id)
print('Get course data by id:', get_course_response)