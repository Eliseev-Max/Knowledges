#-*- coding: utf-8 -*-
"""Пример использования анонимных функций (лямбда-функций)"""
f1 = lambda: 10+20-5*8/4
f2 = lambda x, z, y=2: x**y-z
print(f1())
print(f2(8,26))
arr = ["единица1","Единый","Единица2"]
arr1 = arr.copy()
arr.sort(key=lambda s: s.lower())
for i in arr:
    print(i, end=" ")
arr1.sort()
print("\nметод sort() без функции: ")
for j in arr1:
    print(j, end = " ")
