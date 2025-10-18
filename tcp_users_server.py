import socket

HOST = '127.0.0.1'
PORT = 12345
MAX_CONNECTIONS = 10

messages = []

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    print(f"Сервер запущен на {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Пользователь с адресом: {addr} подключился к серверу")

            try:
                data = client_socket.recv(1024).decode('utf-8')
                if data:
                    print(f"Пользователь с адресом: {addr} отправил сообщение: {data}")
                    messages.append(data)
                    response = '\n'.join(messages)
                    client_socket.send(response.encode('utf-8'))
            except Exception as e:
                print(f"Ошибка при обработке клиента {addr}: {e}")
            finally:
                client_socket.close()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()