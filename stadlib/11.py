#!/usr/bin/env python3
# 质量控制
# doctest, 允许在文档中嵌入测试
def average(values):
    """mean of a list of numbers
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()
