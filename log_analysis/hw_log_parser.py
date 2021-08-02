import os
import argparse
import os.path as op
import re
import json
from collections import defaultdict, OrderedDict


OCTET = r"[1-2]?[0-9]{1,2}"
IP_ADDRESS = OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET
ip = []
dict_of_ip = defaultdict(int)

parser = argparse.ArgumentParser(description='Find and open file')
parser.add_argument('--path', '-p',
                    action='store',
                    required=True,
                    help='Enter file path or filename')
parser.add_argument('--all', '-a',
                    action='store_true',
                    help='Use this option, if you want to handle all files in directory')

args = parser.parse_args()


def prepare_file_to_read(path):
    if path[0] == '~':
        file = op.normpath(op.expanduser(path))
    else:
        file = op.abspath(path)
    if op.isfile(file):
        print(f"Выбран файл {file}")
        return file
    elif op.isdir(file):
        print(f"Указана директория {file}")
        if args.all:
            pass
        else:
            filename = input("Укажите имя файла ")
            full_name = op.abspath(path + '/' + filename)
            try:
                assert op.exists(full_name)
            except AssertionError as err:
                print(f'Файла по указанному пути: {full_name} не существует')
            else:
                return full_name
    else:
        print("Указанный файл или каталог не обнаружен")

# def parse_all_files(path):
#     target_directory = op.normpath(op.expanduser(path))
#     try:
#         assert op.isdir(target_directory),"Указанный каталог не обнаружен"
#         for logfile in os.scandir(target_directory):
#             print(logfile.name)
#     except AssertionError as err:
#         print(err)


idx = 0
with open(prepare_file_to_read(args.path), "r", encoding="utf-8") as f:
    for line in f:
        print(line)
        if idx>10:
            break
        idx+= 1

# duration = r"\d+$"    # Длительность запроса
#






