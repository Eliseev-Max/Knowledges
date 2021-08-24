import subprocess as sp
import os
import time
from collections import defaultdict

MAX_CPU = 0.0
MAX_MEM = 0.0
total_mem = 0.0
total_cpu = 0.0
ps_result = []
mem_list = []
cpu_list = []
user_proc = defaultdict(int)

def report_writer(report):
    pass

def handle_ps_aux():

    NAME = "bufferfile.txt"
    result = sp.run(["ps", "aux"], stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    with open(NAME, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    with open(NAME) as line:
        for i in line:
            ps_result.append(i.split(None, 10))
    os.remove(os.path.normpath(os.getcwd() + '/' + NAME))
    return ps_result[1:]

for elem in handle_ps_aux():
    user_proc[elem[0]] +=1
    total_mem += float(elem[4])
    cpu_list.append(float(elem[2]))
    if MAX_CPU < float(elem[2]):
        MAX_CPU = float(elem[2])
        process_using_max_cpu = elem

    if MAX_MEM < float(elem[3]):
        MAX_MEM = float(elem[3])
        process_using_max_mem = elem

system_users = ', '.join((user_proc.keys()))

report = (
    "Отчёт о состоянии системы:\n"
    f"Пользователи системы: {system_users}\n"
    f"Всего процессов запущено: {len(handle_ps_aux())}\n"
    f"Всего памяти используется: {int(total_mem/1000)} Мб\n"
    f"Всего CPU используется: {round(sum(cpu_list),2)} %\n"
    f"Больше всего памяти использует:\n\tUSER: {process_using_max_mem[0]}\n"
    f"\tPID: {process_using_max_mem[1]}\n"
    f"\t%MEM({MAX_MEM} %)\n"
    f"Больше всего CPU использует:\n\tUSER: {process_using_max_cpu[0]}\n"
    f"\tPID: {process_using_max_cpu[1]}\n"
    f"\t%CPU({MAX_CPU} %)"
)

print(report)
print("Пользовытельские процессы:")
for key in user_proc:
    print(f"\tПользователь {key}:\tзапущено процессов: {user_proc[key]} ")

# print(f"Total memory used (Mb): {int(total_mem/1000)}\n"\
#       f"Total CPU (%) used: {round(sum(cpu_list),2)}\n"\
#       f"Uses the most memory (%): {MAX_MEM}\n"\
#       f"Uses the most CPU (%): {MAX_CPU}\n")