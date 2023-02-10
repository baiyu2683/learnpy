#!/usr/bin/env python3
# 处理多个异常没有关联的异常
# ExceptionGroup可以封装多个异常列表


def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


f()

# try:
#     f()
# except Exception as e:
#     print(f"caught {type(e)}: e")
