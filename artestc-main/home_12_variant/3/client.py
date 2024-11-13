import socket
import sys

def send_command(server_ip, server_port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(command.encode())

        response = client_socket.recv(4096).decode()
        print("Response from server:")
        print(response)

    finally:
        client_socket.close()

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <server_ip> <server_port> <command>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    command = sys.argv[3]

    send_command(server_ip, server_port, command)

if __name__ == "__main__":
    main()
