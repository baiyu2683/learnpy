#!/usr/bin/env python3
# 预定义的清理操作
# 有一些对象定义了不需要该对象时要执行的清理操作。无论使用该对象的操作是否成功，都会执行清理操作。

# 这段代码没有执行f.close()操作关闭文件
# for line in open("myfile.txt"):
#     print(line, end="")
#

# with语句会自动执行
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
