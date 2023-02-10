#!/usr/bin/env python3
# 用列表实现队列效率很低，使用collections.deque实现

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

head = queue.popleft()
print(head)
head = queue.popleft()
print(head)
print(queue)
