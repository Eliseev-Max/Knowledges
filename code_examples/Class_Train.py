#-*- coding: utf-8 -*-
import datetime
class C(object):
    """Documentation"""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def message(self):
        """First message to user"""
        byear = datetime.datetime.today().year - int(self.age)
        return "Hello, {0} {1}! You are {2} years old! It means, you've born in {3} year".format(self.surname, self.name, str(self.age), byear)
    
while True:
    n = input("Введите Ваше имя: ")
    if not n.isalpha():
        print("Вы ввели чепуху! ")
        continue
    break

while True:
    sn = input("Введите Вашу фамилию: ")
    if not sn.isalpha():
        print("Вы ввели чепуху! ")
        continue    
    break

while True:
    age = input("Введите Ваш возраст: ")
    if not age.isdigit():
        print("Вы ввели чепуху! ")
        continue    
    break
n = n.capitalize()
sn = sn.capitalize()
age = int(age)

msg = C(n, sn, age)
print(msg.message())
