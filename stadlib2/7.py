#!/usr/bin/env python3
# 操作列表的工具

# array，只能存储一种数据类型且数据密集度更高
from array import array

a = array("H", [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])


# collections提供了一种deque()对象，双端队列，从左边添加和弹出速度较快

from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
print(d.pop())

# bisect操作有序列表
import bisect

scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
bisect.insort(scores, (300, "ruby"))
print(scores)

# heapq 实现基于常规列表来实现堆的函数。最小值的条目总是保持在位置零。
# 这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print(data)
[heappop(data) for i in range(3)]
