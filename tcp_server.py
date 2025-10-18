import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    
    server_socket.listen(5)
    print("Сервер запущен и ждет подключений...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Получено сообщение: {data}")

        # Отправляем 5 сообщений, каждый заканчивается '\n'
        for i in range(5):
            response = f"Ответ от сервера: {i+1}\n"
            client_socket.send(response.encode('utf-8'))

        client_socket.close()


if __name__ == "__main__":
    try:
        server()
    except KeyboardInterrupt:
        print("Сервер остановлен пользователем")
        

        

    
    