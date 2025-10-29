from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    AuthenticationUserSchema, 
    get_private_http_client
)
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    GetCourseResponseSchema,
    GetCoursesResponseSchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema
)

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"/api/v1/courses/{course_id}")
    
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, 
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))
    
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.patch(
            f"/api/v1/courses/{course_id}", 
            json=request.model_dump(by_alias=True, exclude_unset=True))
    
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.delete(f"/api/v1/courses/{course_id}")
    
    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Создаёт новый курс на сервере и возвращает его данные.

        :param request: Схема с полями title, maxScore, minScore, description,
                        estimatedTime, previewFileId, createdByUserId.
        :return: Содержит информацию о созданном курсе в виде
                 CreateCourseResponseSchema.
        """

        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)
    
    def update_course(
            self, 
            course_id: str, 
            request: UpdateCourseRequestSchema
        ) -> UpdateCourseResponseSchema:
        """
        Обновляет существующий курс.

        :param course_id: Идентификатор курса.
        :param request: Схема с полями title, maxScore, minScore,
                        description, estimatedTime.
        :return: Обновлённые данные курса в виде
                 UpdateCourseResponseSchema.
        """

        response = self.update_course_api(course_id, request)
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        """
        Получает подробную информацию о курсе.

        :param course_id: Идентификатор курса.
        :return: Данные курса в виде GetCourseResponseSchema.
        """

        response = self.get_course_api(course_id)
        return GetCourseResponseSchema.model_validate_json(response.text)
    
    def get_courses(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        """
        Получает список курсов по заданному запросу.

        :param query: Схема запроса с параметром userId.
        :return: Список курсов в виде GetCoursesResponseSchema.
        """

        response = self.get_courses_api(query)
        return GetCoursesResponseSchema.model_validate_json(response.text)
    

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """

    return CoursesClient(client=get_private_http_client(user))