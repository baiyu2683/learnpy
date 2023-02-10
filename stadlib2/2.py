#!/usr/bin/env python3
# 模板
# string模块包含一个Template类，具有适用于最终用户的简化语法
# 通过占位符($)实现格式化操作，占位符由$加上合法的python标识符（字符数字下划线)构成，一旦
# 使用花括号将占位符括起来，就可以在后面直接跟上更多的字母和数字而无需空格分割。
# $$ 将被转译成单个字符$

from string import Template

t = Template("${village}folk send $$10 to $cause")
s = t.substitute(village="Notingham", cause="the ditch fund")
print(s)

# 如果字典或者关键字参数没有提供某个占位符的值，那么substitute()将抛出KeyError.
# 用户提供的数据有可能不是完整的，此时使用safe_substitute()方法更加合适--如果数据缺失
# 它会直接将占位符原样保留

t = Template("Return the $item to $owner")
d = dict(item="unladen swallow")
try:
    print(t.substitute(d))
except KeyError as e:
    print("异常", e)

print(t.safe_substitute(d))

import time, os.path

photofiles = ["img_1074.jpg", "img_1076.jpg", "img_1077.jpg"]


class BatchRename(Template):
    delimiter = "%"


fmt = input("Enter rename style (%d-date %n-seqnum %f-format): ")

t = BatchRename(fmt)
date = time.strftime("%d%b%y")
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print("{0} --> {1}".format(filename, newname))
