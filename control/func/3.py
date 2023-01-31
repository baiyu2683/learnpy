#!/usr/bin/env python3
# 默认值参数
def ask_ok(prompt, retries=4, reminder="Please try again"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


# ask_ok("Do you really want to quit?")
# ask_ok("OK to overwrite the file?", 2)
# ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")

# 默认值只能计算一次，如果默认值为列表等可变对象，会产生与规则不同的结果
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# 不想共享默认值，使用下面例子


def f2(a, L=None):
    if L == None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
