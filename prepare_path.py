import os
import os.path as op
import argparse


working_dir = os.getcwd()
abs_path = op.abspath(working_dir)
file_location = op.abspath(__file__)

parser = argparse.ArgumentParser(description='Find and open file')
parser.add_argument('--path', '-p',
                    action='store',
                    required=True,
                    help='Enter file path or filename')

args = parser.parse_args()

print(f"Текущий рабочий каталог: {working_dir}\n"
      f"Расположение файла: {file_location}\n"
      f"Абсолютный путь до рабочего каталога: {abs_path}\n"
      f"Введённый путь: {args.path}\n"
      f"Обработанный введённый путь: {op.abspath(args.path)}")
