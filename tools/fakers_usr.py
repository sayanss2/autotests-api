import time

def get_random_email() -> str:
    """Генерирует случайную почту"""
    return f"test.{time.time()}@example.com"

def get_random_filename() -> str:
    """Генерирует случайное имя файла"""
    return f"test.{time.time()}image.png"