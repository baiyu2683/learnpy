#!/usr/bin/env python3
# 元组和序列
#
# 元组由多个用逗号隔开的值组成, 不可变，不能更改
t = 12345, 54321, "hello!"
print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

v = [1, 2, 3], [3, 2, 1]
print(v)

empty = ()
# 在元素后面加逗号表示仅有一个元素的元组
singleton = ("hello",)
print(len(empty))
print(len(singleton))

print(singleton)
# 解包
x, y, z = t
print(x, y, z)
