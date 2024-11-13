import sys
import socket
import subprocess

def check_exit(command):
    return command.strip() == "exit"

def handle_client(client_socket, first_connection):
    # Получаем команду от клиента
    command = client_socket.recv(1024).decode().strip()
    print(f"Received command: {command}")

    if check_exit(command):
        print("Exiting...")
        client_socket.close()
        exit(0)

    try:
        # Выполняем команду и получаем результат
        output = subprocess.check_output(command, shell=True).decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        output = str(e.output)

    # Отправляем результат обратно клиенту
    client_socket.sendall(output.encode())

    client_socket.close()

def main():
    if len(sys.argv) < 3:
        print("Usage: python server.py <ip_address> <port>")
        return

    ip_address = sys.argv[1]
    port = int(sys.argv[2])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip_address, port))
    server_socket.listen(1)

    first_connection = True

    print(f"Server started. Listening on {ip_address}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        if first_connection:
            print(f"Client connected: {address[0]}:{address[1]}")
            first_connection = False

        handle_client(client_socket, first_connection)

if __name__ == "__main__":
    main()