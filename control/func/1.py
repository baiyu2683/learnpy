#!/usr/bin/env python3
def fib(n):
    """打印斐波那契数列"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(10)
# 定义函数名
f = fib
f(100)

print(fib(0))
