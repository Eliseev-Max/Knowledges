#-*- coding: utf-8-*-
def func(x,y):
    """Возводит в степень y каждый элемент диапазона от 1 до x включительно"""
    for i in range(1,x+1):
        yield i**y
for j in func(8,2):
    print(j)

del j

def gen(z):
    for e in z:
        yield from range(1, e+1)
z = [4,11, 8, 3]
n = (5,10)
for i in gen(z):
    print(i, end=" ")
print()
for p in gen(n):
    print(p, end=" ")
