#!/usr/bin/env python3
# 弱引用
# 跟踪对象时一般会创建一个令其永久化的引用，weakref模块提供的工具可以不必创建引用就能跟踪对象
# 当对象不再需要是，它将自动从弱引用表中被移除，并未弱引用对象出触发一个回调。

import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d["primary"] = a
print(d["primary"])

del a

gc.collect()
print(d["primary"])
