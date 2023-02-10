#!/usr/bin/env python3
# 触发异常
# raise 语句支持强制触发指定的异常

# raise NameError("HiThere")

# raise ValueError

try:
    raise NameError("HiThere")
except NameError:
    print("An exception flew by!")
    raise
