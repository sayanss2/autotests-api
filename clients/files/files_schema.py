from pydantic import BaseModel, HttpUrl


class FileBaseSchema(BaseModel):
    """
    Описание структуры файла.

    Поля:
        filename (str): Имя файла, которое будет сохранено на сервере.
        directory (str): Путь к каталогу, в котором будет размещён файл.
    """

    filename: str
    directory: str


class FileSchema(FileBaseSchema):
    """
    Описание структуры файла.
    Поля:
        id  (str): Идентификатор файла на сервере.
        url  (str): URL для загрузки файла.
    """

    id: str
    url: HttpUrl


class CreateFileRequestSchema(FileBaseSchema):
    """
    Структура запроса на создание файла.

    Поля:
        upload_file (str): Путь к локальному файлу, который нужно отправить.
                          Путь должен указывать на существующий файл,
                          который будет открыт в режиме чтения в бинарном
                          формате и передан в multipart‑форму.
    """

    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    
    Поля:
        file  (FileSchema): Объект, описывающий созданный файл.
    """

    file: FileSchema