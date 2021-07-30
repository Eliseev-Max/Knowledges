import os
from collections import defaultdict
import os.path as op
import re

PATH = r"~\Knowledges\log_analysis\mini_access.log"
filename = op.abspath(op.expanduser(PATH))

SAMPLE = r"[1-2]?[0-9]{1,2}"
regex = SAMPLE + r"\." + SAMPLE + r"\." + SAMPLE + r"\." + SAMPLE
ip = []
dict_of_ip = defaultdict(int)

# def get_rating(list_of_ip):
#     origin_ip_list = list(set(list_of_ip))
#     rating = dict()
#     for i in origin_ip_list:
#         rating.update({i:list_of_ip.count(i)})
#     return rating

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        ip_search = re.search(regex, line)
        if ip_search is not None:
            ip.append(ip_search.group())
    amount_of_requests = len(ip)

for elem in ip:
    dict_of_ip[elem] +=1

# ip_rating = get_rating(ip)


# for i in ip:
#     if i not in ip_addr:
#         print(f"Этого IP-адреса нет {i}")
#
# comparison_result = set(ip_addr+ip)
# print(len(comparison_result))
# for i in comparison_result:
#     print(i)


# print(len(ip_addr), ip_addr, sep="\n")

