#!/usr/bin/env python3
# 通过从Exception类派生，可以创建新的异常类命名自己的异常。
# 大多数异常命名都以Error结尾, 类似标准异常命名


class MyError(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise MyError("This is my custom exception")
except MyError as e:
    print("MyError occurred:", e.message)
