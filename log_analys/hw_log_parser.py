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

parser = argparse.ArgumentParser(description='Process access.log')

parser.add_argument('-f', dest='file',
                          action='store',
                          help='Path to logfile')  # искомые директория или файл

# os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
# os.path.abspath(path) - возвращает нормализованный абсолютный путь
# os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
# os.path.isfile(path) - является ли путь файлом
# os.path.isdir(path) - является ли путь директорией.
# os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории.
#                          На Windows преобразует прямые слеши в обратные.


args = parser.parse_args()
file = "mini_access.log"

# dict_ip = defaultdict(
#     lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}

with open(args.file) as file:
    idx = 0
    for line in file:           # Не readline, который считывает из файла одну строку при каждом вызове
                                # а перебор строк
        if idx > 99:
            break

        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match is not None:
            ip = ip_match.group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
            # Соответствует последовательности символов: СКОБКА ПРОБЕЛ КАВЫЧКА POST или GET или PUT...
            if method is not None:
                dict_ip[ip][method.groups()[0]] += 1
        idx += 1


"""
    Для access.log должна собираться следующая информация:

    общее количество выполненных запросов           >> попробуй len(file)
    количество запросов по типу: GET - 20, POST - 10 и т.п.     >> готовый инструмент, осталось убрать |
    топ 3 IP адресов, с которых были сделаны запросы
    топ 3 самых долгих запросов, должно быть видно метод, url, ip, время запроса

    Собранная статистика должна быть сохранена в json файл и выведена в терминал в свободном (но понятном!) формате
    Должен быть README.md файл, который описывает как работает скрипт

"""
# 83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" 4743


# )
# https://docs-python.ru/standart-library/modul-re-python/sintaksis-reguljarnogo-vyrazhenija/
# https://tproger.ru/translations/regular-expression-python/
# https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python