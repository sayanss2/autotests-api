import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

message = "Привет, сервер!"
client_socket.send(message.encode())

# Читаем 5 строк из сокета
file = client_socket.makefile('rb')
for _ in range(5):
    line = file.readline().rstrip(b'\n')
    print(f"Ответ от сервера: {line.decode('utf-8')}")
file.close()
client_socket.close()