#-*- coding: utf-8 -*-
import os, sys
print(__file__)     # Путь к исполняемому файлу вместе с именем файла
## Атрибут __file__ не всегда содержит полный путь к файлу
## Поэтому передаём значение атрибута в abspath()
##  os.path.abspath(__file__)
print("Файл: ", os.path.abspath(__file__))
print("Current work folder: ", os.getcwd())
print("Folder for import: ", sys.path[0])
input()
