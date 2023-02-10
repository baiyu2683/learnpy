#!/usr/bin/env python3
# 手动格式化字符串
# str.rjust()方法在左侧填充空格
# 类似还有str.ljust() str.center()
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    print(repr(x * x * x).rjust(4))


# str.zfill() 在数字字符差u能左边填充零，且能识别正负号
print("-12".zfill(5))
print("asdf".zfill(10))
