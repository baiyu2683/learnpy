#!/usr/bin/env python3
# 数据压缩
import zlib

s = b"which which has which witches wrist watch"
print(len(s))

t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(t))
