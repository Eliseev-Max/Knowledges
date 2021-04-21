#-*- coding: utf-8 -*-
"""рассмотрим способы создания словарей в Python 3"""
#1. Создание словаря с помощью записи пар: "ключ":"значение" в фигурных скобках
d_1 = {"a":1,"b":2, "c":3}
print(type(d_1))
#2. Создание словаря с помощью функции dict(key_1=val_1,key_2=val_2)
d_2 = dict(first_name="Max",second_name="Eliseev",age="32",sex="male")
print(f"Объект: {d_2}, тип: {type(d_2)}")
#3. Создание словаря из списка кортежей с парами значений
listOfTuples = [("IP-address","10.1.31.254"),("subnet mask","255.255.255.0"),("gateway","10.1.31.1")]
d_3 = dict(listOfTuples)
print(f"Объект: {d_3}, тип: {type(d_3)}")
#4. Создание словаря из списка списков с парами значений
lol = [["First Name","Max"],["Last Name","Eliseev"],["age",31]]
d_4 = dict(lol)
print(d_4, type(d_4), sep="\n")
#5. Создание словаря из двух списков, keys и values, с помощью функции zip()
keys = ["A", "B", "C", "D", "E"]
values = ["модуль источника питания","модуль главного процессора","модуль дискретных выходов","модуль дискретных входов","модуль интерфейсов"]
d_5 = dict(zip(keys, values))
print(d4,type(d4), sep="\n")
#6. Создание словаря с помощью метода dict.fromkeys(<Последовательность>,[<Значение>])
li = ["first","second","third"]
d51 = dict.fromkeys(li, 0)
print(d51, type(d51), sep="\n")
v = [1,2,3]
d52 = dict.fromkeys(li,v)
print(d52, type(d52), sep="\n")
j = 0
for i in v:
    d52[li[j]] = i
    j+=1
print(d52)
