from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

from tools.fakers import fake

class CourseBaseSchema(BaseModel):
    """
    Базовая структура курса.

    Поля:
    - title (str): Название курса.
    - max_score (int): Максимальный балл, который можно набрать.
    - min_score (int): Минимальный балл, необходимый для прохождения.
    - description (str): Описание курса.
    - estimated_time (str): Оценка времени обучения (например, "2h 30m").
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CourseSchema(CourseBaseSchema):
    """
    Описание структуры курса.

    Поля:
     - id (str): Идентификатор курса.
     - preview_file  (FileSchema): Файл превью.
     - created_by_user  (UserSchema): Пользователь‑создатель курса.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    id: str
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseRequestSchema(CourseBaseSchema):
    """
    Создание нового курса.

    Поля:
    - preview_file_id (str): Идентификатор файла превью.
    - created_by_user_id (str): Идентификатор пользователя‑создателя.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )
    
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """

    course: CourseSchema


class UpdateCourseRequestSchema(CourseBaseSchema):
    """
    Обновление существующего курса.

    Поля (необязательные):
    - title (str | None): Новое название курса.
    - max_score (int | None): Новый максимальный балл.
    - min_score (int | None): Новый минимальный балл.
    - description (str | None): Новое описание.
    - estimated_time (str | None): Новое время обучения.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None  = Field(default_factory=fake.min_score, alias="minScore")
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None  = Field(default_factory=fake.estimated_time, alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """

    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Запрос списка курсов.

    Поля:
    - user_id (str): Идентификатор пользователя, для которого запрашиваются курсы.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )
    
    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка курсов.

    Поля:
     - courses (list[CourseSchema]): Список курсов.
    """

    courses: list[CourseSchema]


class GetCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения одного курса.

    Поля:
      - course  (CourseSchema): Курс.
     """

    course: CourseSchema