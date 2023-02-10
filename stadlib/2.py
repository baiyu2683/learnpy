#!/usr/bin/env python3
# 文件通配符
# glob模块提供磊哥在目录中使用通配符搜索创建文件列表的函数

import glob

print(glob.glob("*.py"))
files = glob.glob("/home/crispr/Projects/learnpy/**/*", recursive=True)
print(len(files))
print(files[-1])
