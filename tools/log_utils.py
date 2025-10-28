import json
from httpx import Response
from typing import Union
from pydantic import BaseModel, HttpUrl  # <-- добавлено

def log_response(response: Union[Response, dict, str, BaseModel, HttpUrl], label: str = "Response") -> None:
    """
    Выводит на печать ответ с метками.
    Принимает либо объект httpx.Response, либо уже распарсенный словарь,
    либо строку в формате JSON, либо Pydantic‑модель.
    """
    # Если пришёл Pydantic‑модель, преобразуем её в словарь
    if isinstance(response, BaseModel):
        response = response.model_dump()

    # Если пришёл JSON‑строка, распарсим её в словарь
    if isinstance(response, str):
        try:
            response = json.loads(response)
        except json.JSONDecodeError:
            # Если строка не является валидным JSON, просто печатаем как есть
            print(f"{label} (str): {response}")
            print("=" * 80)
            return

    # Если пришёл словарь, просто печатаем его
    if isinstance(response, dict):
        # json.dumps не умеет сериализовать типы pydantic, например HttpUrl,
        # поэтому используем default=str
        print(f"{label} (dict):")
        print(json.dumps(response, indent=2, default=str))
        print("=" * 80)
        return

    # Если пришёл объект Response
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"Method: {response.request.method}")

    try:
        data = response.json()
    except Exception:
        data = None

    if data is None or data == {} or data == []:
        print(f"{label}: <нет данных>")
    else:
        print(f"{label}:", json.dumps(data, indent=2, default=str))

    print("=" * 80)