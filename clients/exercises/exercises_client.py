# clients/exercises/exercises_client.py
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    AuthenticationUserSchema, 
    get_private_http_client
)
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с эндпоинтами /api/v1/exercises.

    Предоставляет методы для получения списка заданий, получения конкретного
    задания, создания, обновления и удаления заданий.
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с параметрами запроса (courseId).
        :return: Ответ от сервера в виде httpx.Response.
        """

        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде httpx.Response.
        """

        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание нового задания.

        :param request: Словарь с данными нового задания.
        :return: Ответ от сервера в виде httpx.Response.
        """

        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(
        self, 
        exercise_id: str, 
        request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Обновление данных существующего задания.

        :param exercise_id: Идентификатор задания, которое нужно обновить.
        :param request: Словарь с полями, которые необходимо изменить.
        :return: Ответ от сервера в виде httpx.Response.
        """
        
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", 
            json=request.model_dump(by_alias=True, exclude_unset=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания по его идентификатору.

        :param exercise_id: Идентификатор задания, которое нужно удалить.
        :return: Ответ от сервера в виде httpx.Response.
        """

        return self.delete(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение списка заданий для определенного курса с возвратом JSON.

        :param query: Параметры запроса.
        :return: Словарь с ключом 'exercises'.
        """

        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получение информации о задании по его идентификатору с возвратом JSON.

        :param exercise_id: Идентификатор задания.
        :return: Словарь с ключом 'exercise'.
        """

        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создание нового задания с возвратом JSON.

        :param request: Данные нового задания.
        :return: Словарь с ключом 'exercise'.
        """

        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestSchema,
    ) -> UpdateExerciseResponseSchema:
        """
        Обновление существующего задания с возвратом JSON.

        :param exercise_id: Идентификатор задания.
        :param request: Данные для обновления.
        :return: Словарь с ключом 'exercise'.
        """

        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)
    

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создание экземпляра клиента с авторизацией.

     :param user: Словарь с данными пользователя для авторизации.
     :return: Экземпляр класса ExercisesClient.
    """

    return ExercisesClient(client=get_private_http_client(user))