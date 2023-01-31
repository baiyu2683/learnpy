#!/usr/bin/env python3
# 任意参数列表，参数数量可变时使用
# 用于采集传递给函数的剩余参数，通常位于参数列表末尾，其后面之可以有关键字参数


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
