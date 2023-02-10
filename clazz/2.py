#!/usr/bin/env python3
# class对象
# 类对象支持两种操作： 属性引用和实例化


class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


x = MyClass()
print(x.i)
print(x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)
