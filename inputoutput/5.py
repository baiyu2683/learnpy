#!/usr/bin/env python3
# open()返回一个文件对象，经常使用的参数open(filename, mode, encoding=None)
# filename: 文件名字符串
# mode： 打开模式， r: 只读  w： 只写  a： 追加内容，写入到文件末尾  r+: 读写. 默认: r
# mode后面可以加b,表示读取二进制文件，例如:rb
# encoding: 读写编码，默认和平台相关，尽量使用utf-8

# 在文本模式下读取文件，平台的换行符(unix为\n, windows为\r\n)会转换为\n。\n写入时会转换为对应平台的换行符
# 这个特性在读取jpeg或exe等二进制文件时会破坏文件结构，所以一定要用二进制模式读取此类文件

with open('1.py', encoding='utf-8') as f:
    read_data = f.readline()

print(read_data)
# 查看文件关闭状态
print(f.closed)

# with关键字会自动关闭文件，如果没有使用with关键字，需要调用f.close()方法关闭文件
