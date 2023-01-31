#!/usr/bin/env python3
def fib2(n):
    """返回到n的斐波那契数列的列表"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print(f100)
