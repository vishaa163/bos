import socket
import os

socketser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 12345)
socketser.bind(address)

socketser.listen(1)

print('waiting for a connection...')

socketvcli, client_address = socketser.accept()
print('Connected to:', client_address)

data = socketvcli.recv(1024)
print(data.decode(), 'killed')

# Получение PID сервера
server_pid = os.getpid()
print("PID сервера:", server_pid)

socketvcli.close()
socketser.close()
