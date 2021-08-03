import json
import os
# from collections import defaultdict, OrderedDict
# import operator
import os.path as op
import re
from modules.functions import *

PATH = r"~\Knowledges\log_analysis\mini_access.log"
filename = op.normpath(op.expanduser(PATH))
# PATH = r"~/Knowledges/log_analysis/access_500.log"
# filename = op.abspath(op.expanduser(PATH))


OCTET = r"[1-2]?[0-9]{1,2}"
IP_ADDRESS = OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET
dict_of_ip = defaultdict(int)
dict_method = defaultdict(
    int, {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)

with open(filename, "r", encoding="utf-8") as file:
    ip = []
    for line in file:
        ip_search = re.search(IP_ADDRESS, line)
        if ip_search is not None:
            # В каждой строке найдём и соберём IP-адрес
            ip_assembled = ip_search.group()
            # Добавим найденный в строке IP-адрес в список
            ip.append(ip_assembled)
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
            if method is not None:
                dict_method[method.group(1)] += 1

# Составляем словарь DefaultDict: {"IP-адрес":количество_запросов}
for elem in ip:
    dict_of_ip[elem] +=1

# sorted_ip = sort_ip_dict(dict_of_ip, display=3)

# print(f"Всего было выполнено {len(ip)} запросов\n"
#       f"Топ 3 IP-адресов,  с которых выполнялись запросы:")
# for key in sorted_ip:
#     print(f"с IP-адреса: {key}\t-\t{sorted_ip[key]} запросов ")

# Сформируем словарь для последующей сериализации статистики в json-файл
total_report = dict({
    "Всего выполнено запросов": len(ip),
    "Количество запросов по методу": dict_method,
    "Топ 3 адреса, с которых выполнялись запросы": sort_ip_dict(dict_of_ip, display=3)
})
# Вывод сериализованного JSON-объекта
print(json.dumps(total_report, indent=4, ensure_ascii=False))




