# log_utils.py
import json

def log_response(response, label="Response") -> None:
    """Выводит на печать ответ с метками"""
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    try:
        print(f"{label}:", json.dumps(response.json(), indent=2))
    except Exception:
        print(f"{label}: <не JSON>")
    print("="*80)