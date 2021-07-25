import argparse
import re
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process access.log')
# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/library/argparse.html#the-add-argument-method
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')  # искомые директория или файл
# parser.add_argument('-a', action='storeTrue', help='Handle all log-files')             # Обработка всех логов внутри одной дир.

"""
    Для access.log должна собираться следующая информация:

    общее количество выполненных запросов
    количество запросов по типу: GET - 20, POST - 10 и т.п.
    топ 3 IP адресов, с которых были сделаны запросы
    топ 3 самых долгих запросов, должно быть видно метод, url, ip, время запроса

    Собранная статистика должна быть сохранена в json файл и выведена в терминал в свободном (но понятном!) формате
    Должен быть README.md файл, который описывает как работает скрипт

"""

args = parser.parse_args()

dict_ip = defaultdict(
    lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)