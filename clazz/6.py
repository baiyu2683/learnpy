#!/usr/bin/env python3
# 私有变量
# python中仅限从一个对象内部访问的私有变量是不存在的。
# 私有变量约定： 带有一个下划线名称(例如_spam)应当被当作是api的非公有部分（无论是函数、方法或者数据成员）
# 但是又存在对于类私有成员的有效使用场景(例如为了避免名称与子类所定义的名称相冲突)，因此存在对此种机制的
# 有限支持，成为*名称改写*。任何形式的__spam标识符(至少带有两个前缀下划线，至多一个后缀下划线)的文本将
# 被替换为_classname__spam, 其中classname为去除了前缀下划线的当前类名称


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    # 重写了update方法，但是不重写__init__方法
    # 也就是不改变父类mapping中的update访问
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
