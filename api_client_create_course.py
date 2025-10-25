from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import (
    CreateUserRequestDict, 
    get_public_users_client
)
from clients.files.files_client import (
    CreateFileRequestDict, 
    get_files_client
)
from clients.courses.courses_client import (
    CreateCourseRequestDict,
    get_courses_client
)

from tools.fakers import get_random_email
from tools.fakers_usr import get_random_filename
from tools.log_utils import log_response

# Инициализируем клиенты
public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
log_response(create_user_response, label="Create User")

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename=get_random_filename(),
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
#print('Create file data:', create_file_response)
log_response(create_file_response, label="Create file data:")

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
#print('Create course data:', create_course_response)
log_response(create_course_response, label="Create course data:")