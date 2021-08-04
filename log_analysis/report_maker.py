import os.path as op
import re
import operator
import json
from collections import defaultdict, Counter

# PATH = r"~\Knowledges\log_analysis\mini_access.log"
# filename = op.normpath(op.expanduser(PATH))
# PATH = r"~/Knowledges/log_analysis/access_500.log"
# filename = op.abspath(op.expanduser(PATH))

# Скомпилированные регулярные выражения
OCTET = r"[12]?[0-9]{1,2}"
IP_ADDRESS = re.compile(OCTET + r"\." + OCTET + r"\." + OCTET + r"\." + OCTET)
METHODS = re.compile(r"\] \"(POST|GET|PUT|DELETE|HEAD)")
DURATION = re.compile(r"\" (\d+$)")
URL = re.compile(r"\"http://.*?\"")

# "Хранилища"
ip, all_requests = [], []
duration_dict = defaultdict(int)
dict_method = defaultdict(
    int, {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
)
duration_of_request = dict()

def parse_logfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            request_params = []
            ip_search = IP_ADDRESS.search(line)
            method = METHODS.search(line)
            url_search = URL.search(line)
            duration_search = DURATION.search(line)

            if ip_search is not None:
                ip_assembled = ip_search.group()
                ip.append(ip_assembled)
                request_params.append(ip_assembled)

                if method is not None:
                    dict_method[method.group(1)] += 1
                    request_params.append(method.group(1))

                if url_search is not None:
                    url_assembled = url_search.group().strip('"')
                    request_params.append(url_assembled)
                else:
                    request_params.append("NOT SPECIFIED")

                if duration_search is not None:
                    dur_assembled = duration_search.groups()[0]
                    request_params.append(int(dur_assembled))

            if request_params != []:
                all_requests.append(request_params)

    for request in sorted(all_requests, key=operator.itemgetter(-1), reverse=True):
        if len(duration_of_request) == 3:
            break
        duration_of_request.update({
            request[0]:{
                "HTTP-метод":request[1],
                "URL": request[2],
                "Продолжительность": request[3]
            }
        })

    top_3_ip = dict(Counter(ip).most_common(3))

    # Сформируем словарь для последующей сериализации статистики в json-файл
    total_report = dict({
        "Всего выполнено запросов": len(ip),
        "Количество запросов по методу": dict_method,
        "Топ 3 адреса, с которых выполнялись запросы": top_3_ip,
        "Топ 3 самых долгих запросов": duration_of_request
    })

    # # Вывод сериализованного JSON-объекта
    with open("Statistics.json", "a+") as write_file:
        json.dump(total_report, write_file)

    print(json.dumps(total_report, indent=4, ensure_ascii=False))

