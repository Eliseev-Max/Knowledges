import argparse
import os.path
import re
import json
from collections import defaultdict



parser = argparse.ArgumentParser(description='Process access.log')

parser.add_argument('-f', dest='file',
                          action='store',
                          help='Path to logfile')  # искомые директория или файл


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





