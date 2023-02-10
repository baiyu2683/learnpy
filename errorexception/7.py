#!/usr/bin/env python3
# finally子句，用于定义在所有情况下都必须要执行的清理操作。
# 和else子句不同的是，else子句是在没有异常触发时执行的
# finally子句不管有没有都触发，也就是说else执行后也要触发finally

"""
不论 try 语句是否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：
如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。
except 或 else 子句执行期间也会触发异常。 同样，该异常会在 finally 子句执行之后被重新触发。
如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。
如果执行 try 语句时遇到 break,、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。
如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，而不是来自 try 子句的 return 语句的返回值。
"""


def bool_return():
    """
    只返回False
    """
    try:
        return True
    finally:
        return False


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
print("=")
divide(2, 0)
print("=")
divide("2", "1")
