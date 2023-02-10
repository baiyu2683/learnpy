#!/usr/bin/env python3
# format方法, str.format()

print('We are the {} who say "{}!"'.format("knights", "Ni"))

print("{0} and {1}".format("spam", "eggs"))
print("{1} and {0}".format("spam", "eggs"))

print(
    "This {food} is {adjective}.".format(food="spam", adjective="absolutely horrible")
)

print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other="Georg"))

# 字典参数
# 0是位置参数,例子中第0个参数是table, 0[key]表示在字段中取key的值
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab:{0[Dcab]:d}".format(table))

# 使用**对字段进行解包，然后按照关键字访问
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))
