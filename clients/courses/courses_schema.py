from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


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
    
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


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

    title: str | None = Field(default=None)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None  = Field(default=None, alias="minScore")
    description: str | None = Field(default=None)
    estimated_time: str | None  = Field(default=None, alias="estimatedTime")


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