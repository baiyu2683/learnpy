#!/usr/bin/env python3
# 生成器，用于创建迭代器的简单而强大的工具。
# 写法类似于标准函数，但当他们返回数据时会使用yield语句。每次在生成器上调用next()时，他会从上次离开的位置恢复执行


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse("golf"):
    print(char)
