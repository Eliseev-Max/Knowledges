import subprocess as sp
from collections import defaultdict

NAME = "bufferfile.txt"
user_proc = defaultdict(int)

def func1():
    result = sp.run(["ps", "aux"], stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    with open(NAME, "w", encoding="utf-8") as f:
        f.write(result.stdout)


def handler(filename):
    ps_result = []
    with open(filename) as line:
        for i in line:
            ps_result.append(i.split(None, 10))
    return ps_result[1:]

func1()

for elem in handler(NAME):
    user_proc[elem[0]] +=1

system_users = ', '.join(list(user_proc.keys()))
print(f"Users: {system_users}")
for key in user_proc:
    print(f"Пользователь {key}: запущено {user_proc[key]} процессов")
