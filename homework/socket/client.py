# -*- coding: utf-8 -*-

import socket

"""
Клиент, созданный с помощью модуля socket
"""

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9090
MESSAGE = b'hello, world!'
# Создадим сокет (проинициализируем)
sock = socket.socket()
# Подключимся к серверу
sock.connect((SERVER_ADDRESS, SERVER_PORT))
# отправим серверу сообщение
sock.send(MESSAGE)

data = sock.recv(1024)
sock.close()

print(data)
