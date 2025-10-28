# test_public_users_client.py
from httpx import Client
from clients.users.public_users_client import PublicUsersClient, CreateUserRequestDict
from clients.authentication.authentication_client import AuthenticationClient, LoginRequestSchema
from clients.users.private_users_client import PrivateUsersClient, UpdateUserRequestDict
from clients.files.files_client import FilesClient, CreateFileRequestDict
from clients.courses.courses_client import (
    CoursesClient,
    GetCoursesQueryDict,
    CreateCourseRequestDict,
    UpdateCourseRequestDict
)
from clients.exercises.exercises_client import (
    ExercisesClient,
    GetExercisesQueryDict,
    CreateExerciseRequestDict,
    UpdateExerciseRequestDict
)

from tools import log_response, get_random_email, get_random_filename

# общий http‑клиент
http_client = Client(base_url="http://127.0.0.1:8000")

# 1. Публичный клиент – создание пользователя
public_client = PublicUsersClient(http_client)

#payload_user_create: CreateUserRequestDict = {
#    "email": get_random_email(),
#    "password": "string",
#    "lastName": "Ivanov",
#    "firstName": "Ivan",
#    "middleName": "Ivanovich"
#}

payload_user_create = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="Ivanov",
    firstName="Ivan",
    middleName="Ivanovich"
)

create_user_response = public_client.create_user_api(payload_user_create)
log_response(create_user_response, "Create user")

# 2. Аутентификационный клиент – логин
auth_client = AuthenticationClient(http_client)

payload_user_login = LoginRequestSchema(
    email=payload_user_create["email"],
    password=payload_user_create["password"]
)
user_login_response = auth_client.login_api(payload_user_login)
user_login_data = user_login_response.json()
log_response(user_login_response, "Login")

user_access_token = user_login_data["token"]["accessToken"]

# 3. Приватный клиент – запрос к /me
private_client = PrivateUsersClient(http_client)
private_client.client.headers.update({"Authorization": f"Bearer {user_access_token}"})

user_me_response = private_client.get_user_me_api()
user_me_data = user_me_response.json()
log_response(user_me_response, "Get user me")

user_get_response = private_client.get_user_api(user_me_data["user"]["id"])
log_response(user_get_response, "Get user_id data")

payload_user_update = UpdateUserRequestDict(
    email=get_random_email(),
    firstName="Alex",
    middleName="Smith"
)
user_update_response = private_client.update_user_api(user_me_data["user"]["id"], payload_user_update)
log_response(user_update_response, "Update user_id data")


user_get_response = private_client.get_user_api(user_me_data["user"]["id"])
log_response(user_get_response, "Get user_id data")

#4.1 Приватный клиент – запрос к /files
file_client = FilesClient(http_client)

file_payload = CreateFileRequestDict(
    filename=get_random_filename(),
    directory="test123",
    upload_file="./testdata/files/testfile.png"
)
file_create_response = file_client.create_file_api(file_payload)
file_create_data = file_create_response.json()
log_response(file_create_response, "Create file")

file_get_response = file_client.get_file_api(file_create_data["file"]["id"])
log_response(file_get_response, "Get file")


#4.2 Приватный клиент – запрос к /courses
course_client = CoursesClient(http_client)


course_payload = CreateCourseRequestDict(
    title="test123",
    maxScore=5,
    minScore=1,
    description="test123",
    estimatedTime="10min",
    previewFileId=file_create_data["file"]["id"],
    createdByUserId=user_me_data["user"]["id"]
)
courses_create_response = course_client.create_course_api(course_payload)
courses_create_data = courses_create_response.json()
log_response(courses_create_response,  "Create course")

course_update_payload = UpdateCourseRequestDict(
    title="test1234",
    description="test1234",
    estimatedTime="30min"
)
course_update_response = course_client.update_course_api(courses_create_data["course"]["id"], course_update_payload)
log_response(course_update_response,  "Update course")

course_client_params = GetCoursesQueryDict(
    userId=user_me_data["user"]["id"]
)
courses_get_response = course_client.get_courses_api(course_client_params)
courses_get_data = courses_get_response.json()
log_response(courses_get_response, "Get courses")

#5. Приватный клиент – запрос к /exercises
exercises_client = ExercisesClient(http_client)

#5.1 Создание задания
create_exercise_payload = CreateExerciseRequestDict(
    title="Tesr exercise 1",
    courseId=courses_get_data["courses"][0]["id"],
    maxScore=10,
    minScore=0,
    orderIndex=1,
    description="description 1",
    estimatedTime="15min",
)

exercises_create_response = exercises_client.create_exercise_api(create_exercise_payload)
exercises_create_data = exercises_create_response.json()
log_response(exercises_create_response,  "Create exercise")

#5.2 Получение списка заданий для курса
exercises_get_query = GetExercisesQueryDict(
    courseId=create_exercise_payload["courseId"]
)

exercises_get_response = exercises_client.get_exercises_api(exercises_get_query)
exercises_get_data = exercises_get_response.json()
log_response(exercises_get_response, "Get exercises")

#5.3 Получение конкретного задания
exercise_get_response = exercises_client.get_exercise_api(exercises_get_data["exercises"][0]["id"])
exercise_get_data = exercise_get_response.json()
log_response(exercise_get_response, "Get exercise")

#5.4 Обновление задания
update_exercise_payload = UpdateExerciseRequestDict(
    title= "Tesr exercise 123",
    description= "description 123456"
)

exercise_update_response = exercises_client.update_exercise_api(
    exercises_get_data["exercises"][0]["id"], 
    update_exercise_payload
)
exercise_update_data = exercise_update_response.json()
log_response(exercise_update_response, "Update exercise")

#6. Приватный клиент – запрос на удаление (курса и/или файла, задания и пользователя
#file_delete_response = file_client.delete_file_api(file_create_data["file"]["id"])
#log_response(file_delete_response, "Delete file")

exercise_delete_response = exercises_client.delete_exercise_api(exercises_get_data["exercises"][0]["id"])
log_response(exercise_delete_response, "Delete exercise")

course_delete_response = course_client.delete_course_api(courses_get_data["courses"][0]["id"])
log_response(course_delete_response,  "Delete course")

user_delete_response = private_client.delete_user_api(user_me_data["user"]["id"])
log_response(user_delete_response, "Delete user_id data")

http_client.close()