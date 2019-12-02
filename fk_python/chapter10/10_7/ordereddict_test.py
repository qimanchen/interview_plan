#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OrderedDict -- 按添加顺序进行排序
比较两个dict是否相同时，尽管值一样，但顺序不同也不同

popitem(last=True): 默认弹出最后加入的key-value，last=False弹出最先加入的

move_to_end(key, last=True): 默认将指定的key-value移动到最右边，反之则移动到最左边
"""
from collections import OrderedDict

dx = OrderedDict(b=5, c=2, a=7)
print(dx)

d = OrderedDict()
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
d['Python'] = 89

for k, v in d.items():
	print(k,v)