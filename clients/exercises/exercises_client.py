# clients/exercises/exercises_client.py
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Параметры запроса списка заданий.

    Поля:
        courseId (str): Идентификатор курса, для которого запрашиваются задания.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Структура запроса на создание задания.

    Поля:
        title (str): Заголовок.
        courseId (str): Идентификатор курса.
        maxScore (int): Максимальный балл.
        minScore (int): Минимальный балл.
        orderIndex (int): Порядковый номер.
        description (str): Описание.
        estimatedTime (str): Оценка времени.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Структура запроса на обновление задания.

    Поля (необязательные):
        title (str | None): Новый заголовок задания.
        maxScore (int | None): Новый максимальный балл.
        minScore (int | None): Новый минимальный балл.
        orderIndex (int | None): Новый порядковый номер.
        description (str | None): Новое описание задания.
        estimatedTime (str | None): Новая оценка времени.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с эндпоинтами /api/v1/exercises.

    Предоставляет методы для получения списка заданий, получения конкретного
    задания, создания, обновления и удаления заданий.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с параметрами запроса (courseId).
        :return: Ответ от сервера в виде httpx.Response.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде httpx.Response.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание нового задания.

        :param request: Словарь с данными нового задания.
        :return: Ответ от сервера в виде httpx.Response.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(
        self, 
        exercise_id: str, 
        request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Обновление данных существующего задания.

        :param exercise_id: Идентификатор задания, которое нужно обновить.
        :param request: Словарь с полями, которые необходимо изменить.
        :return: Ответ от сервера в виде httpx.Response.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания по его идентификатору.

        :param exercise_id: Идентификатор задания, которое нужно удалить.
        :return: Ответ от сервера в виде httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")