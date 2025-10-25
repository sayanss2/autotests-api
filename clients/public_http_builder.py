from httpx import Client


# Общий кэш клиентов (и для public, и для private)
_http_clients_cache: dict[str, Client] = {}


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    #return Client(timeout=100, base_url="http://localhost:8000")
    client_key = "public"
    client = _http_clients_cache.get(client_key)

    if client is None:
        client = Client(timeout=100, base_url="http://localhost:8000")
        _http_clients_cache[client_key] = client

    return client