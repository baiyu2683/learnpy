#!/usr/bin/env python3
# 格式化字符串字面值
# 简称f-字符串，在字符串前加f或F,通过{expression}表达式，把python表达式的值添加到字符串内。

import math

print(f"The value of pi is approximately {math.pi:.3f}")
# :后面传递证书，为该字段设置最小字符宽度

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

animals = "eels"
print(f"My hovercraft is full of {animals}")
print(f"My hovercraft is full of {animals!r}")

bugs = "roaches"
count = 13
area = "living room"
print(f"Debugging {bugs=!s} {count=} {area=}")
