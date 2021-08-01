import os
# from collections import defaultdict, OrderedDict
# import operator
import os.path as op
import re
from modules.functions import *

#PATH = r"~\Knowledges\log_analysis\mini_access.log"
PATH = r"~/Knowledges/log_analysis/access_500.log"
#filename = op.abspath(op.expanduser(PATH))
filename = op.normpath(op.expanduser(PATH))

OCTET = r"[1-2]?[0-9]{1,2}"
IP_ADDRESS = OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET
ip = []
dict_of_ip = defaultdict(int)

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        ip_search = re.search(IP_ADDRESS, line)
        if ip_search is not None:
            ip.append(ip_search.group())
    amount_of_requests = len(ip)

for elem in ip:
    dict_of_ip[elem] +=1

sorted_ip = sort_ip_dict(dict_of_ip, display=3)

print(f"Всего было выполнено {amount_of_requests} запросов\n"
      f"Топ 3 IP-адресов,  с которых выполнялись запросы:")
for key in sorted_ip:
    print(f"с IP-адреса: {key}\t-\t{sorted_ip[key]} запросов ")

# .groups() !!!!
# https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python


