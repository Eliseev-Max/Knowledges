#-*- coding: utf-8-*-

class Mixin:
    attr = 0
    def mixin_method(self):
        print("Вызван метод примеси")
class Class1(Mixin):
    def method1(self):
        print("Метод класса Class1")
class Class2(Class1):
    def method2(self):
        print("Метод класса Class2")
class Class3(Class1):
    def method3():
        print("I'm the Class3 method")
class Class4(Class2,Class1):
    def method4():
        print("Fuck you!!")
        
c1 = Class1()
c1.method1()
c1.mixin_method()
print("Attention!!!")
c2 = Class2()
c2.mixin_method()
print(Class4.mro())
