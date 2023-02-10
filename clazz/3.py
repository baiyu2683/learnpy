#!/usr/bin/env python3
# 类和实例变量


class Dog:
    kind = "canine"
    # trick = []

    def __init__(self, name):
        self.name = name
        self.trick = []

    def add_trick(self, trick):
        self.trick.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

d.add_trick("roll over")
e.add_trick("play dead")
print(d.trick)
print(e.trick)
