#!/usr/bin/env python3
# 集合 {} 或者 set()

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)

print("orange" in basket)
print("crabgrass" in basket)
a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print(a - b)
print(a & b)
print(a ^ b)

print("=================")
# 集合和列表一样也支持推导式
a = {x for x in "abracadabra" if x not in "abc"}
print(a)
