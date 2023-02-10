#!/usr/bin/env python3
# del语句
# del语句按照索引，而不是值从列表中移除元素
# 也可以从列表中移除切片，或清空整个列表

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# 也可以删除整个变量, print时报错，因为没有定义
del a
# print(a)
