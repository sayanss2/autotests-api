import socket

HOST = 'localhost'
PORT = 12345

def main():
    print("Выберите сообщение для отправки:")
    print("1. Привет, сервер! (по умолчанию)")
    print("2. Ввести своё сообщение")
    
    choice = input("Ваш выбор (1 или 2, Enter для выбора 1): ").strip()
    
    if choice == "2":
        message = input("Введите ваше сообщение: ")
    else:
        message = "Привет, сервер!"
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        client_socket.send(message.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print("\nПолучена история сообщений от сервера:")
        print(response)
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()