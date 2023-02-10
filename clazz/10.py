#!/usr/bin/env python3
# 生成器表达式
# 某些a金丹的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。
# 这种表达式被设计用于生成器将立即被外层函数所使用的情况

print(sum(i * i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x * y for x, y in zip(xvec, yvec))

data = "golf"
print(list(data[i] for i in range(len(data) - 1, -1, -1)))
