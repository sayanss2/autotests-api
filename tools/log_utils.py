# log_utils.py
import json

def log_response(response, label="Response") -> None:
    """Выводит на печать ответ с метками"""
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"Method: {response.request.method}")
    try:
        data = response.json()
    # Если тело ответа пустое или равно null, выводим более понятное сообщение
        if data is None or data == {} or data == []:
            print(f"{label}: <нет данных>")
        else:
            print(f"{label}:", json.dumps(data, indent=2))
    except Exception:
        print(f"{label}: <не JSON>")
    print("="*80)