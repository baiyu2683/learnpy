#!/usr/bin/env python3
# 为了区分函数参数中的位置形参，关键字形参。让开发者仅通过函数定义就可以知道哪些参数需要怎么传递
# 引入了/和*两个符号
# 在/之前全部是位置形参,必须按位置传递，/之后可以是位置或关键字形参
# * 之后表示仅限关键字形参，*之前可以是位置或关键字形参


def standard_arg(arg):
    """可以按位置或者关键字传递"""
    print(arg)


def pos_only_arg(arg, /):
    """arg参数必须按位置传递"""
    print(arg)


def kwd_only_arg(*, arg):
    """arg必须按关键字传递"""
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    """post_only必须按位置传递，standard可以按照位置或关键字传递，kwd_only必须按关键字传递"""
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=20)

pos_only_arg(2)
# pos_only_arg(arg=2)

# kwd_only_arg(3)
kwd_only_arg(arg=3)

combined_example(1, 2, kwd_only=4)
combined_example(1, standard=2, kwd_only=4)


# 下面函数定义中name参数与kwd参数中name为键的参数可能发生冲突
def foo(name, **kwds):
    return "name" in kwds


# foo(10, name="zhang", age=10)

# 使用/分割位置参数和关键字参数就不会发生上述问题了
def foo2(name, /, **kwds):
    return "name" in kwds


foo2("zhang", name="zhang", age=10)
