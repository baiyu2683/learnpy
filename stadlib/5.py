#!/usr/bin/env python3
# 字符串模式匹配

import re

c = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(c)
# 将字符串(第三个参数)中使用正则表达式(第一个参数)匹配到的内容，使用给定的参数(第二个参数)替换
c = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")
print(c)
# 简单功能使用字符串方法简单明了
print("tea for too".replace("too", "two"))
