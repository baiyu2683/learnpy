#!/usr/bin/env python3
# 迭代器
# 调用对象的iter()方法，该方法返回一个定义了__next()__方法的迭代器对象，此方法将逐一访问容器中的元素。
# 当元素用尽时，__next()__将引发StopIteration异常来统治终止for循环。
# 可以使用next()内置函数来调用__next()__

s = "abc"
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
