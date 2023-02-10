#!/usr/bin/env python3
# 格式化输出

import reprlib

# 提供一个定制化repr(),缩略显示大型或者深层嵌套的容器对象
print(reprlib.repr(set("supercalifragilisticexpialidocious")))

import pprint

# pprint提供了更加复杂的打印控制
t = [[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]
pprint.pprint(t, width=20)

import textwrap

# 格式化文本段落，以适应给定的屏幕宽度
doc = "The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."
print(textwrap.fill(doc, width=20))

import locale

# 处理国际化
# locale.setlocale(locale.LC_ALL, "English_United States.1252")
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x)))
