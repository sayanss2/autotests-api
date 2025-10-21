import time

def get_random_email() -> str:
    """Генерирует случайную почту"""
    return f"test.{time.time()}@example.com"