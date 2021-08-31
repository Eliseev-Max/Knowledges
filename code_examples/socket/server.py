# -*- coding: utf-8 -*-

"""
Сервер, созданный с помощью модуля socket
"""
import socket

# Создадим сокет (проинициализируем)
sock = socket.socket()

SERVER_IP = 'localhost'
PORT = 9090
QUEUED_CONNECTIONS = 1      # максимальное количество соединений в очереди

sock.bind((SERVER_IP, PORT))
sock.listen(QUEUED_CONNECTIONS)

# принимаем подключение
conn, client_addr = sock.accept()      # метод возвращает кортеж (новый_сокет, адрес_клиента)

print(f"Connected: {client_addr}")

while True:
    data = conn.recv(1024)      # чтение информации порциями по 1024 байта
    print(f'Получено: {data.decode()}')
    if not data:
        break
    conn.send(data.upper())

conn.close()