# -*- coding: utf-8 -*-

"""
Сервер, созданный с помощью модуля socket
"""
import socket
import re
from collections import defaultdict
from http import HTTPStatus

SERVER_IP = 'localhost'
PORT = 9090
# Зададим максимальное количество соединений в очереди
QUEUED_CONNECTIONS = 1

# Регулярные выражения для поиска нужных значений в HTTP-запросе клиента
METHOD = re.compile(r"(GET|POST|PUT|HEAD|DELETE|OPTIONS|CONNECT)")
STATUS = re.compile(r"\?status=([1-5][0-9]{2})")
HEADERS = defaultdict(str)

sock = socket.socket()
sock.bind((SERVER_IP, PORT))
sock.listen(QUEUED_CONNECTIONS)

# Принимаем подключение
conn, client_address = sock.accept()      # метод возвращает кортеж (новый_сокет, адрес_клиента)

print(f"Connected: {client_address}")

while True:
    data = conn.recv(1024)      # чтение информации порциями по 1024 байта
    if not data:
        break
    else:
        request = data.decode().split("\r\n")
        general = request[0]
        headers = request[1:]
        method = METHOD.search(general)
        if method is not None:
            request_method = method.group()
            print(request_method)

        if general.find('status=') != -1:
            status_value = STATUS.search(general)

            if status_value is not None:
                status_code = status_value.group(1)
                print(status_code)
            else:
                status_code = 200
                print(f"Incorrect status, substituded value = {status_code}")
        else:
            status_code = 200
            print(f"Parameter \"status\" wasn\'t sent, substituded value = {status_code}")

        dict_status = dict({"Status code":status_code})
        print(dict_status)

        for line in headers:
            if line:
                hdr = line.split(":", 1)
                HEADERS[hdr[0]] = hdr[1]
        for key in HEADERS:
            print(f"{key} -> {HEADERS[key]}")
        # conn.send(b"request has processed")
conn.close()
