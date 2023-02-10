#!/usr/bin/env python3
# 斐波那契
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=",")
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 以脚本方式运行python模块
# python fibo.py arguments
# 会把__name__赋值为__main__
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
