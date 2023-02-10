#!/usr/bin/env python3
# dir()函数
#

import fibo, sys

print(dir(fibo))

# 没有a参数时，会列出当前定义的名称，比如下面会列出a和fib，sys
a = [1, 2, 3, 4, 5]
fib = fibo.fib
dir()


# dir不会列出内置函数和变量的名称。这些内容的定义在 标准模块duiltins里面
import builtins

dir(builtins)
