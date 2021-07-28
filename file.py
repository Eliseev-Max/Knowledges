# -*- coding: utf-8 -*-

import argparse
import os.path

# Исправить косяки:
# Если не добавить \ или/ в конец директории, при вводе файла имена складываются и появляется ошибка
# Либо пофиксить, либо убрать функционал

# Добавить параметр - количество выводимых строк
parser = argparse.ArgumentParser(description='Find and open file')
parser.add_argument('--path', '-p',
                    action='store',
                    help='Enter file path or filename')

args = parser.parse_args()

# path = 'C:\\Users\\m.eliseev\\Knowledges\\mini_access.log'
# this_path = "~/Knowledges/mini_access.log"


def prepare_file_to_read(path):
    file = os.path.normpath(path)
    if os.path.isfile(file):
        print("Выбран файл")
        return file
    elif os.path.isdir(file):
        print("Вы указали директорию.")
        filename = input("Укажите имя файла ")
        full_name = os.path.abspath(path + filename)
        print(full_name)
        if os.path.exists(full_name):
            return full_name
    else:
        print("Указанный файл или каталог не найден")


# print(type(args),type(args.path),sep="\n")
print(args.path)
# print(os.path.normpath(args))
# os.path.expanduser(args)
# print(os.path.abspath(args))
idx = 0
with open(prepare_file_to_read(args.path), "r", encoding="utf-8") as f:
    for line in f:
        print(line)
        if idx>10:
            break
        idx+= 1
