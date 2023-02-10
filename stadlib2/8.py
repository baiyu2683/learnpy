#!/usr/bin/env python3
# 十进制浮点运算

from decimal import *

print(round(Decimal("0.70") * Decimal("1.05"), 2))
print(round(0.70 * 1.05, 2))
print(Decimal("0.70") * Decimal("1.05"))
print(0.70 * 1.05)

print(Decimal("1.00") % Decimal(".10"))
print(1.00 % 0.10)

# decimal精度高，可以执行对于浮点数来说不适用的末运算和相等性检测
print(sum([Decimal("0.1")] * 10) == Decimal("1.0"))
print(sum([0.1] * 10) == 1.0)
print(sum([Decimal("0.1")] * 10))
print(sum([0.1] * 10))

# 设置decimal的精度
print("default: ", getcontext().prec)
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
