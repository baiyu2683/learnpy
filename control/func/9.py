#!/usr/bin/env python3
# 文档字符串, 第一行为对象用途和简短摘要，保持简洁，大写字母开头，句号结尾
# 第二行为空白行
# 后面的行可包含若干段落，描述调用约定，副作用等


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything
    这是一个文档那个测试
    """
    pass


print(my_function.__doc__)
