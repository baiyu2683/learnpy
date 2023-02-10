#!/usr/bin/env python3
# os模块, 系统相关的交互操作
# 一定要使用import os而不是from os import *。避免内建的open()函数被os.open()隐式替换掉
# import os

# print(os.getcwd())
# print(os.chdir("/home/crispr"))
# # 调用系统命令
# print(os.system("mkdir today"))


# dir() help()用作交互式辅助工具，用于处理大型模块

# print(dir(os))
# print(help(os))

# shutil模块提供日常文件和目录管理操作的高级别接口
import shutil

with open("file.db", "w") as file:
    file.write("asdf")

shutil.copyfile("file.db", "archive.db")
shutil.move("file.db", "/home/crispr/file.db")
