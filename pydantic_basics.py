"""
{
  "courses": [
    {
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
  ]
}
"""


import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel


# Добавили модель FileSchema
class FileSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: HttpUrl = Field(default="http://localhost:8000")
    filename: str = Field(default="file.png")
    directory: str = Field(default="courses")


# Добавили модель UserSchema
class UserSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(default="user@example.com")
    last_name: str = Field(alias="lastName", default="Bond")
    first_name: str = Field(alias="firstName", default="Zara")
    middle_name: str = Field(alias="middleName", default="Alise")


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    #max_score: int = Field(alias='maxScore', ge=1, le=100, default=1000)
    max_score: int = Field(ge=1, le=100, default=1000)
    min_score: int = Field(alias='minScore', ge=0, le=99, default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias='previewFile', default_factory=FileSchema)
    estimated_time: str = Field(alias='estimatedTime', default="2 weeks")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(default_factory=UserSchema)


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id = "string",
    title = "string",
    #maxScore = 100,
    max_score = 100,
    #minScore = 10,
    min_score = 10,
    description = "string",
    preview_file = FileSchema(
        id = "string",
        url = "https://example.com/",
        filename = "string",
        directory = "string"
    ),
    #estimatedTime = "string",
    estimated_time = "string",
    created_by_user = UserSchema(
        id = "string",
        email = "user@example.com",
        last_name = "string",
        first_name = "string",
        middle_name = "string"
    )
)
print('Course default model:', course_default_model)
print(course_default_model.model_dump())

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    'id': 'string1',
    'title': 'string1',
    'maxScore': 100,
    'minScore': 10,
    'description': 'string1',
    # Добавили ключ previewFile
    'previewFile': {
        'id':  "string1",
        'url':  "https://example.com/",
        'filename':  "string1",
        'directory':  "string1"
    },
    'estimatedTime': 'string1',
    # Добавили ключ createdByUser
    'createdByUser': {
        'id':   "string1",
         'email':   "user@example.com",
         'lastName':   "string1",
         'firstName':   "string1",
         'middleName':   "string1"
    }
}

course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())

# Инициализируем модель CourseSchema через JSON
course_json = """{
    "id": "string2",
    "title": "string2",
    "maxScore": 100,
    "minScore": 10,
    "description": "string2",
    "previewFile": {
        "id":  "string2",
         "url":  "https://example.com/",
          "filename":  "string2",
           "directory":  "string2"
    },
    "estimatedTime": "string2",
    "createdByUser": {
        "id":   "string2",
         "email":   "user@example.com",
          "lastName":   "string2",
           "firstName":   "string2",
            "middleName":   "string2"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course json model:', course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True, indent=2))

# Создадим объект модели без передачи параметров
course = CourseSchema()
print(course.model_dump_json(by_alias=True, indent=2))

# Создадим несколько объектов модели
course1 = CourseSchema()
course2 = CourseSchema()

print(course1.id)
print(course2.id)


# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())