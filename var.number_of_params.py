#-*- coding: utf-8 -*-
import random
def AAP_func(*t):
    """Arbitrary amount of parameters, функция, принимающая произвольное число параметров"""
    print("The number of received parameters is ", len(t))
    summa = []
    for i, arr in enumerate(t):
        print("Parameter {0} has index {1}".format(arr, i))
    msg = input("If you want to add all this parameters, write 'yes' ")
    message = msg.lower()
    res = 0
    if message == "yes" or message == "y":
        for y in t:
            res += y
        print(res)
n = random.randrange(5, 20)
print(n)
li = []
co = 0
while co <n:                # Создадим список из случайного количества (n) случайных чисел
    a = random.randrange(-10,11)
    li.append(a)
    co += 1
AAP_func(*li)
