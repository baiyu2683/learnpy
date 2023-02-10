#!/usr/bin/env python3
# json保存结构化数据

import json

# 对字符串操作，序列化反序列化
x = [1, "simple", "list", "中文"]
xj = json.dumps(x, ensure_ascii=False)
print(xj)

y = json.loads(xj)
print(y, type(y))


# 序列化到文件，从文件反序列化
f = open("json.txt", mode="w", encoding="utf-8")
x = {"name": "zhangsan", "age": "34", "籍贯": "河南"}
json.dump(x, f)
f.close()

f = open("json.txt", mode="r", encoding="utf-8")
y = json.load(f)
print(y, type(y))
f.close()
