#!/usr/bin/env python3
# 关键字参数 kwarg=value


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOOM")
parrot(action="VOOOOOM", voltage=1000000)
parrot("a million", "bereft of life", "jump")
parrot("a thousand", state="pushing up the daisies")

# **name形式的参数，接受字典，dict
# *name形式的参数可以与**name形式的参数一起使用，*name接受一个元组, 元组包含形参列表之外的位置参数,且必须在**name之前


print("===========")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Limburger",
    "It's very runny, sir",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
)
