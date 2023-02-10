#!/usr/bin/env python3
# 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例


class Warehouse:
    purpose = "storage"
    region = "west"

    def print(self):
        print(Warehouse.purpose, Warehouse.region)


w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
# 定义实例属性，则有限查找实例属性
# 并且不会影响类中函数对类属性的访问
w2.region = "east"
print(w2.purpose, w2.region)
w2.print()
