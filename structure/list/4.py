#!/usr/bin/env python3
# 列表推导式

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)

x = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(x)
# 等价于下面这种写法
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

print("=============")
vec = [-4, -2, 0, 2, 4]
l = [x * 2 for x in vec]
print(l)
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ["   banana", "   loganberry", "passion fruit   "]
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

import math

print([str(round(math.pi, i)) for i in range(1, 6)])
