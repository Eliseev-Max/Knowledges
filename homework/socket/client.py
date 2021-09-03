# -*- coding: utf-8 -*-

import socket

"""
Клиент, созданный с помощью модуля socket
"""

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9090
# MESSAGE = b'hello, world!'
REQUEST = "GET /?status=202 HTTP/1.1\r\n\
Host: localhost:9090\r\n\
User-Agent: python3_socket_client\r\n\
Accept: */*\r\n\
Connection: keep-alive"
print(REQUEST)
# Создадим сокет (проинициализируем)
sock = socket.socket()
# Подключимся к серверу
sock.connect((SERVER_ADDRESS, SERVER_PORT))
# отправим серверу сообщение
sock.send(REQUEST.encode())

data = sock.recv(1024)
print(data.decode("utf-8"))
sock.close()


