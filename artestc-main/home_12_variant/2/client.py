import socket
import os

socketvcli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
socketvcli.connect(server_address)
print('Connected to:', server_address)

variable = 'Shot'
socketvcli.send(variable.encode())

socketvcli.close()
