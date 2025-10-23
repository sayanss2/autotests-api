from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """
    Запрос списка курсов.

    Поля:
    - userId (str): Идентификатор пользователя, для которого запрашиваются курсы.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Создание нового курса.

    Поля:
    - title (str): Название курса.
    - maxScore (int): Максимальный балл, который можно набрать.
    - minScore (int): Минимальный балл, необходимый для прохождения.
    - description (str): Описание курса.
    - estimatedTime (str): Оценка времени обучения (например, "2h 30m").
    - previewFileId (str): Идентификатор файла превью.
    - createdByUserId (str): Идентификатор пользователя‑создателя.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict, total=False):
    """
    Обновление существующего курса.

    Поля (необязательные):
    - title (str | None): Новое название курса.
    - maxScore (int | None): Новый максимальный балл.
    - minScore (int | None): Новый минимальный балл.
    - description (str | None): Новое описание.
    - estimatedTime (str | None): Новое время обучения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")
    
    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, 
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)
    
    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)
    
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")