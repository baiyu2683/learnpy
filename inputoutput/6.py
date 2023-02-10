#!/usr/bin/env python3
# 文件对象相关方法

# file.read(size) 读取文件内容，并返回字符串（文本模式）或者字符串对象（二进制模式）
# size可选，如果不写或者为负数，表示读取整个文件内容。
# 到达文件末尾，f.read()返回空字符串('')

# f = open("1.py", mode="r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()


# f.readline() 读取但行数据; 字符串末尾保留换行符(\n)， 只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。
# f.readline()返回空字符串，就表示已经到达了文件末尾，空行使用'\n'表示，该字符串只包含一个换行符
# f = open("empty.txt", mode="r", encoding="utf-8")
# content = f.readline()
# print(content)
# content = f.readline()
# print("{0!r}".format(content))
# f.close()

# 从文件中拂去多行时，可以遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单。
# f = open("1.py", mode="r", encoding="utf-8")
# for line in f:
#     print(line, end="")

# f.close()

# 使用列表形式读取文件所有行, 使用list(f), f.readlines()
# f = open("1.py", mode="r", encoding="utf-8")
# # content = list(f)
# content = f.readlines()
# print(content)
# f.close()

# 写文件, f.write(string), 返回写入的字符数
# f = open("writefile.txt", mode="w", encoding="utf-8")
# value = ("the answer", 42)
# s = str(value)
# count = f.write(s)
# print(count)
# f.close()

# f.tell() 返回整数，给出文件对象在文件中的当前位置,表示二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字
# f.seek(offset, whence) 可以改变文件对象的位置, 通过向草考点添加offset计算位置
# 参考点whence为0,从文件开头计算，1使用当前文件位置，2文件末尾。省略是，默认为0
f = open("workfile", "rb+")
count = f.write(b"0123456789abcdef")
print("写入字数: {}".format(count))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()

# 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2) 搜索到文件末尾是个例外），
# 唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为。
