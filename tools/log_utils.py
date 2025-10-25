# log_utils.py
import json
from typing import Any

def log_response(response: Any, label: str = "Response") -> None:
    """
    Выводит на печать ответ с метками.
    Принимает либо объект httpx.Response, либо уже распарсенный словарь.
    """
    # Если пришёл словарь, просто печатаем его
    if isinstance(response, dict):
        print(f"{label} (dict):")
        print(json.dumps(response, indent=2))
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
        print(f"{label}:", json.dumps(data, indent=2))

    print("=" * 80)