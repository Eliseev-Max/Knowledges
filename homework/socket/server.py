# -*- coding: utf-8 -*-

"""
Сервер, созданный с помощью модуля socket
"""
import socket
import re
import json
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
report = dict()

# Создаём объект сокета
sock = socket.socket()
# Осуществляем привязку IP-адреса и порта к сокету
sock.bind((SERVER_IP, PORT))
sock.listen(QUEUED_CONNECTIONS)
sock.settimeout(120)
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
            dict_method = {"Request method": request_method}
            method_string = f"Request method: {request_method}\n"

        if general.find('status=') != -1:
            status_value = STATUS.search(general)

        # Определение/назначение кода статуса
            if status_value is not None:
                status_code = status_value.group(1)
                print(status_code)
            else:
                status_code = 200
                print(f"Incorrect status, substituded value = {status_code}")
        else:
            status_code = 200
            print(f"Parameter \"status\" wasn\'t sent, substituded value = {status_code}")

        dict_status = dict({"Status code": status_code})
        status_string = f"Status code: {status_code}\n"
        # print(dict_status)

        # Создание словаря заголовков
        for line in headers:
            if line:
                hdr = line.split(":", 1)
                HEADERS[hdr[0]] = hdr[1]
        for key in HEADERS:
            print(f"{key} -> {HEADERS[key]}")

    rep_str = method_string + status_string + headers
    # report.update(dict_method)
    # report.update(dict_status)
    # report.update(HEADERS)
    with open("response.txt", "w+", encoding="utf-8") as f:
        w.write(rep_str)

    conn.send(rep_str.encode())
    # conn.send(json.dumps(report, ensure_ascii=False, indent=4))
conn.close()
