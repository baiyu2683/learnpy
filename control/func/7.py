#!/usr/bin/env python3

# 解包实参列表
print(list(range(3, 6)))

# *args解包元组、序列
args = [3, 6]
print(list(range(*args)))

# **args解包字典


def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.", end=" ")
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
