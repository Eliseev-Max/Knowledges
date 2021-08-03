import json
import os
from collections import defaultdict, OrderedDict, Counter
# import operator
import os.path as op
import re
from modules.functions import *

PATH = r"~\Knowledges\log_analysis\mini_access.log"
filename = op.normpath(op.expanduser(PATH))
# PATH = r"~/Knowledges/log_analysis/access_500.log"
# filename = op.abspath(op.expanduser(PATH))

# Regular expressions
OCTET = r"[12]?[0-9]{1,2}"
IP_ADDRESS = re.compile(OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET)
METHODS = r"\] \"(POST|GET|PUT|DELETE|HEAD)"
DURATION = re.compile(r"\" (\d+$)")         # Длительность запроса
URL = re.compile(r"\"http://.*?\"")
duration_dict = defaultdict(int)
dict_method = defaultdict(
    int, {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)
dict_of_ip = defaultdict(int)
params = ()
url, duration = [], []
idx = 0

with open(filename, "r", encoding="utf-8") as file:
    ip = []
    # print(IP_ADDRESS + URL + DURATION)
    for line in file:
        idx += 1
        ip_search = IP_ADDRESS.search(line)
        url_search = URL.search(line)
        duration_search = DURATION.search(line)
        if ip_search is not None:
            # В каждой строке найдём и соберём IP-адрес
            ip_assembled = ip_search.group()
            ip.append(ip_assembled)
            # print(ip_assembled)
        if url_search is not None:
            url_assembled = url_search.group()
            #print(url_assembled)
        if duration_search is not None:
            dur_assembled = duration_search.groups()[0]
            # print(dur_assembled)
            # ip_assembled = ip_search.groups()[0]
            # Добавим найденный в строке IP-адрес в список
            # ip.append(ip_assembled)
            # url.append(url_assembled)
            # duration.append()
            # method = re.search(METHODS, line)
            # if method is not None:
            #     dict_method[method.group(1)] += 1
            # duration_of_request = re.search(DURATION, line)
            # if duration_of_request is not None:
            #     #duration_dict[ip_assembled][duration_of_request.groups()[0]] +=1
            #     duration_dict[ip_assembled] = int(duration_of_request.groups()[0])

print(Counter(ip).most_common(3))
# Составляем словарь DefaultDict: {"IP-адрес":количество_запросов}
# for elem in ip:
#     dict_of_ip[elem] +=1
#
# print(url)
# print(duration)
#
# print(idx)
# print(len(ip))
# print(len(duration_dict))

# for el in duration_dict:
#     print(f"Key = {el} -> Value = {duration_dict[el]}")

# sorted_ip = sort_ip_dict(dict_of_ip, display=3)

# print(f"Всего было выполнено {len(ip)} запросов\n"
#       f"Топ 3 IP-адресов,  с которых выполнялись запросы:")
# for key in sorted_ip:
#     print(f"с IP-адреса: {key}\t-\t{sorted_ip[key]} запросов ")

# Сформируем словарь для последующей сериализации статистики в json-файл
# total_report = dict({
#     "Всего выполнено запросов": len(ip),
#     "Количество запросов по методу": dict_method,
#     "Топ 3 адреса, с которых выполнялись запросы": sort_ip_dict(dict_of_ip, display=3)
# })
# # Вывод сериализованного JSON-объекта
# print(json.dumps(total_report, indent=4, ensure_ascii=False))

# https://proglib.io/p/ne-izobretat-velosiped-ili-obzor-modulya-collections-v-python-2019-12-15
# https://pythonworld.ru/moduli/modul-collections.html
# https://python-scripts.com/import-collections
# https://medium.com/nuances-of-programming/%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-collections-%D0%B2-python-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80-%D1%82%D0%B8%D0%BF%D0%BE%D0%B2-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-b5a7fdfef918
# https://habr.com/ru/post/319164/
