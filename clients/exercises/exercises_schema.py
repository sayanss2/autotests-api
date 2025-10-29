from pydantic import BaseModel, Field, ConfigDict


class ExerciseBaseSchema(BaseModel):
    """
    Базовая структура задания.

    Поля:
        title (str): Заголовок.
        max_score (int): Максимальный балл.
        min_score (int): Минимальный балл.
        order_index (int): Порядковый номер.
        description (str): Описание.
        estimated_time (str): Оценка времени.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class ExerciseSchema(ExerciseBaseSchema):
    """
    Структура задания.

    Поля:
        id (str): Уникальный идентификатор.
        course_id (str): Идентификатор курса.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    id: str
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(ExerciseBaseSchema):
    """
    Структура запроса на создание задания.

    Поля:
        course_id (str): Идентификатор курса.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    course_id: str = Field(alias="courseId")


class CreateExerciseResponseSchema(BaseModel):
    """
    Ответ сервера при создании задания.
    """
    
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(ExerciseBaseSchema):
    """
    Структура запроса на обновление задания.

    Поля:
        title (str): Заголовок.
        max_score (int): Максимальный балл.
        min_score (int): Минимальный балл.
        order_index (int): Порядковый номер.
        description (str): Описание.
        estimated_time (str): Оценка времени.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    title: str | None = Field(default=None)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    order_index: int | None = Field(default=None, alias="orderIndex")
    description: str | None = Field(default=None)
    estimated_time: str | None = Field(default=None, alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Ответ сервера при обновлении задания.
    """

    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Параметры запроса списка заданий.

    Поля:
        course_id (str): Идентификатор курса, для которого запрашиваются задания.
    """
    model_config = ConfigDict(
        populate_by_name=True
    )

    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """
    Ответ сервера при запросе списка заданий.

    Поле:
        exercises  (list[ExerciseSchema]): Список найденных заданий.

    """

    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Ответ сервера при запросе конкретного задания.

    Поле:
        exercise (ExerciseSchema): Информация о задании.
    """
    
    exercise: ExerciseSchema