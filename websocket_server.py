import asyncio
import websockets
from websockets import ServerConnection


async def echo(wesocket: ServerConnection):
    async for message in wesocket:
        print(f"Получнео сообщение: {message}")
        response = f"Сервер получил: {message}"

        for _ in range(5):
            await wesocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())