from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    GetExercisesQuerySchema
)
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema

from tools.fakers import fake

# Инициализируем клиенты
public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename=f"test_{fake.email()}_image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем задание
create_exercise_request = CreateExerciseRequestSchema(
    title="Test exercise 1",
    course_id=create_course_response.course.id,
    max_score=10,
    min_score=0,
    order_index=1,
    description="Description 1",
    estimated_time="15min",
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

#Обновляем задание
update_exercise_request = UpdateExerciseRequestSchema(
    title= "Test exercise 123",
    description= "description 123456"
)
update_exercise_response = exercise_client.update_exercise(
    create_exercise_response.exercise.id,
    update_exercise_request
)
print('Update exercise data:', update_exercise_response)

#Получаем задания
get_exercises_response = exercise_client.get_exercises(
    GetExercisesQuerySchema(course_id=create_course_response.course.id)
)
print('Get exercises data:', get_exercises_response)

get_exercise_response = exercise_client.get_exercise(create_exercise_response.exercise.id)
print('Get exercise data:', get_exercise_response)