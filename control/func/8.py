#!/usr/bin/env python3
# lambda表达式, 语法上，只能是单个表达式，语义上，只是常规函数的语法糖
# lambda a, b = a + b

# 返回lambda表达式
def make_increment(n):
    return lambda x: x + n


f = make_increment(42)
print(f(0))

print(f(1))

# 传递lambda表达式
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# 参数列表和常规函数一致，多个参数使用逗号隔开，位置参数关键字参数都可以
sum1 = lambda a, b: a + b
print(sum1(1, 2))
