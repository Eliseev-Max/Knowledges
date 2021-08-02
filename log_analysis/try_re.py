import os
# from collections import defaultdict, OrderedDict
# import operator
import os.path as op
import re
from modules.functions import *

PATH = r"~\Knowledges\log_analysis\mini_access.log"
#PATH = r"~/Knowledges/log_analysis/access_500.log"
#filename = op.abspath(op.expanduser(PATH))
filename = op.normpath(op.expanduser(PATH))

OCTET = r"[1-2]?[0-9]{1,2}"
IP_ADDRESS = OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET
ip = []
dict_of_ip = defaultdict(int)
dict_ip = defaultdict(
    lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)
dict_method = defaultdict(
    lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        ip_search = re.search(IP_ADDRESS, line)
        if ip_search is not None:
            # В каждой строке найдём и соберём IP-адрес
            ip_assembled = ip_search.group()
            # Добавим найденный в строке IP-адрес в список
            ip.append(ip_assembled)
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
            if method is not None:
                dict_method["Количество запросов по методу:"][method.group(1)] += 1
    amount_of_requests = len(ip)


for elem in ip:
    dict_of_ip[elem] +=1

# for key in dict_of_ip:
#     print(f"Ключ {key}\t->\t Значение {dict_of_ip[key]}")

print(dict_method)
# for k in dict_method:
#     print(f"Ключ {k}\t->\t Значение {dict_method[k]}")

sorted_ip = sort_ip_dict(dict_of_ip, display=3)

print(f"Всего было выполнено {amount_of_requests} запросов\n"
      f"Топ 3 IP-адресов,  с которых выполнялись запросы:")
for key in sorted_ip:
    print(f"с IP-адреса: {key}\t-\t{sorted_ip[key]} запросов ")

total_report = dict({
    "Всего выполнено запросов": amount_of_requests,

})




