#!/usr/bin/env python3
# 嵌套的列表推导式
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print([[row[i] for row in matrix] for i in range(4)])
# 相当于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 实际应用中，最好使用内置函数替代复杂的流程语句, zip()更好用
print(list(zip(*matrix)))
