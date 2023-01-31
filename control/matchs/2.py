#!/usr/bin/env python3

# 解包赋值

point = (1, 2)

match point:
    case (1, 2):
        print("Origin")
print("=================")
# 定义数据结构，并解包赋值


class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


p = Point()
p.x = 0
# p.y = 0
where_is(p)
