import argparse
import os.path
import re
import json
from collections import defaultdict

"""
Требования к реализации
    Должна быть возможность указать директорию где искать логи или конкретный файл
    Должна быть возможность обработки всех логов внутри одной директории

"""

# parser = argparse.ArgumentParser(description='Process access.log')
#
# parser.add_argument('-f', dest='file',
#                           action='store',
#                           help='Path to logfile')  # искомые директория или файл

# os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
# os.path.abspath(path) - возвращает нормализованный абсолютный путь
# os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
# os.path.isfile(path) - является ли путь файлом
# os.path.isdir(path) - является ли путь директорией.
# os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории.
#                          На Windows преобразует прямые слеши в обратные.

# parser.add_argument('-a', action='store_true', help='Handle all logfiles')   # Обработка всех логов внутри одной дир.

# parser.add_argument('--method', '-m',
#                     action='store',
#                     help='Method to make request',
#                     default='GET',
#                     choices=['GET', 'POST'])

# args = parser.parse_args()
file = "mini_access.log"

with open(file) as f:
    idx = 0
    for line in f:
        if idx > 10:
            break
        print(line)
        idx +=1


"""
    Для access.log должна собираться следующая информация:

    общее количество выполненных запросов
    количество запросов по типу: GET - 20, POST - 10 и т.п.
    топ 3 IP адресов, с которых были сделаны запросы
    топ 3 самых долгих запросов, должно быть видно метод, url, ip, время запроса

    Собранная статистика должна быть сохранена в json файл и выведена в терминал в свободном (но понятном!) формате
    Должен быть README.md файл, который описывает как работает скрипт

"""
# 83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" 4743

# dict_ip = defaultdict(
#     lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
# )