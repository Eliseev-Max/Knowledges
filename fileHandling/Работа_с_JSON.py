#-*-coding:utf-8 -*-
import json
data = {"ip" : "ip-адрес",
        "port" : "TCP-порт",
        "login" : "admin",
        "pass" : "admin",
        "timeout" : "Таймаут в сек"
        }
#with open("MyFirstJSON.json", "w") as write_file:
#    json.dump(data, write_file)
json_string = json.dumps(data, ensure_ascii=False, indent=4)
jss = json_string
print(jss,"\nтип данных: ",type(json_string))
input()