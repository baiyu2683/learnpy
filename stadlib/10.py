#!/usr/bin/env python3
# 性能测量
from timeit import Timer

print(Timer("t=1; a=b; b=t", "a=1; b=2").timeit())

print(Timer("a,b = b,a", "a=1; b=2").timeit())
