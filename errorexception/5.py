#!/usr/bin/env python3
# 异常链

# 默认情况下，异常的__context__会设置为先前的异常，
# 也可以通过wite_traceback()方法为异常设置上下文__context__属性
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# raise RuntimeError from exec


# def func():
#     raise ConnectionError


# # from 会设置异常的__cause__属性，用来说明异常是由谁引起的
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError("Failed to open database") from exc


# fromm None 通过设置异常的__suppress_context__属性来明确禁止异常关联
# 这样不会有异常链，仅显示当前异常
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError from None
