#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
namedtuple的使用
namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
typename -- tuple子类的名称
field_names: 字段
verbose, rename, module -- 打印，预设字段不合法自动重命名，__module__

方法：
_make(iterable): 类方法，通过序列来创建命名元组对象 -- 依次个每个字段给与value
_asdict():将命名元组对象转换为OrderedDict对象
_replace(**kwargs):替换命名元组中一个或多个字段的值 -- ！！好像没啥用。。。。
_source：返回定义该命名元组的源代码
_fields:返回该命名元组中所有字段名组成的元组
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)
print(p[0] + p[1])
a, b = p
print(a, b)

# namedtuple的特定用法
print(p.x, p.y)
print(p)

# 方法示例
my_data = ['East', 'North']

p2 = Point._make(my_data)
print(p2)
print(p2._asdict())
p2._replace(y='South')
print(p2)
print(p2._fields)

color = namedtuple('color', 'red green blue') # 同样实际上命名可以这样实现
pixel = namedtuple('pixel', Point._fields+color._fields)
pix = pixel(11,22,128,255,0)

print(pix)
print(pix._source)