#!/usr/bin/env python3
# 作用域和命名空间例子


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        # nonlocal表明赋值应该在外层作用域中绑定
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)


scope_test()
print("In global scope: ", spam)
