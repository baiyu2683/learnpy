#!/usr/bin/env python3
# dict

tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)

print(tel["jack"])

del tel["sape"]
print(tel)

tel["irv"] = 4127
print(tel)

print(list(tel))
sorted(tel)
print("guido" in tel)
print("jack" not in tel)

# 接受键值对序列生成字典
a = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
print(a)

print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
