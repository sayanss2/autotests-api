from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """
    Структура запроса на создание файла.

    Поля:
        filename (str): Имя файла, которое будет сохранено на сервере.
        directory (str): Путь к каталогу, в котором будет размещён файл.
        upload_file (str): Путь к локальному файлу, который нужно отправить.
                          Путь должен указывать на существующий файл,
                          который будет открыт в режиме чтения в бинарном
                          формате и передан в multipart‑форму.
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")
    
    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        data = {
            "filename": request["filename"],
            "directory": request["directory"],
        }
        with open(request["upload_file"], "rb") as f:
            return self.post(
                "/api/v1/files",
                data=data,
                files={"upload_file": f}
            )
        
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")