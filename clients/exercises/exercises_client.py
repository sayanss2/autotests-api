# clients/exercises/exercises_client.py
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


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


class Exercise(TypedDict):
    """
    Структура задания, возвращаемая сервером.

    Поля:
        id (str): Уникальный идентификатор.
        title (str): Заголовок.
        courseId (str): Идентификатор курса.
        maxScore (int): Максимальный балл.
        minScore (int): Минимальный балл.
        orderIndex (int): Порядковый номер.
        description (str): Описание.
        estimatedTime (str): Оценка времени.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Ответ сервера при запросе списка заданий.

    Поле:
        exercises (list[Exercise]): Список найденных заданий.
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Ответ сервера при запросе конкретного задания.

    Поле:
        exercise (Exercise): Информация о задании.
    """
    exercise: Exercise


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
    
    # --- Методы, возвращающие JSON-ответы ---------------------------------
    
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получение списка заданий для определенного курса с возвратом JSON.

        :param query: Параметры запроса.
        :return: Словарь с ключом 'exercises'.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получение информации о задании по его идентификатору с возвратом JSON.

        :param exercise_id: Идентификатор задания.
        :return: Словарь с ключом 'exercise'.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExerciseResponseDict:
        """
        Создание нового задания с возвратом JSON.

        :param request: Данные нового задания.
        :return: Словарь с ключом 'exercise'.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestDict,
    ) -> GetExerciseResponseDict:
        """
        Обновление существующего задания с возвратом JSON.

        :param exercise_id: Идентификатор задания.
        :param request: Данные для обновления.
        :return: Словарь с ключом 'exercise'.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()
    

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Создание экземпляра клиента с авторизацией.

     :param user: Словарь с данными пользователя для авторизации.
     :return: Экземпляр класса ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))