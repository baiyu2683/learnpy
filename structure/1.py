#!/usr/bin/env python3
# 循环的技巧

# items()方法可同时取出键和对应的值
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# enumerate()函数可以同时取出位置索引和对应的值
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# 同时循环两个或多个序列时，用zip()函数可以将其内的元素一一匹配
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]

for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))

# 逆向循环序列时，先正向定位序列，然后调用reversed()函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 按指定顺序循环序列，可以用sorted函数, 在不改动原序列的基础上，返回一个新序列
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for i in sorted(basket):
    print(i)

# 在循环中修改列表的内容时，创建新列表比较简单，且安全
import math

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filter_data = []
for value in raw_data:
    if not math.isnan(value):
        filter_data.append(value)

print(filter_data)
