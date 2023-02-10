#!/usr/bin/env python3
# 只存储数据的类型，类似c中的结构体
# 通过dataclass实现

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


john = Employee("john", "computer lab", 1000)
print(john.dept)
print(john.name)
print(john.salary)
