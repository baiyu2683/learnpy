#!/usr/bin/env python3
# 通过add_note(note)丰富异常信息, 标准异常处理渲染这些note

# try:
#     raise TypeError("bad type")
# except Exception as e:
#     e.add_note("Add some information")
#     e.add_note("Add some more information")
#     raise


def f():
    raise OSError("operation failed")


excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f"Happened in Iteration {i + 1}")
        excs.append(e)
raise ExceptionGroup("We have some problems", excs)
