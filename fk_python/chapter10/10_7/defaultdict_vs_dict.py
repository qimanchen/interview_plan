#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dict 和 defaultdict 针对新建key-value时，当查询值不存在时如何处理
"""
# dict使用setdefault来实现预设值
s = [('Python',1), ('Swift', 2), ('Python',3), ('Swift', 4),  ('Python', 9)]
d = {}
for k, v in s:
	# setdefault -- 当访问dict中的某个key不存在时，使用value预设值
	d.setdefault(k, []).append(v)
	
print(list(d.items()))

del d

# 而使用defaultdict可以直接实现
from collections import defaultdict

d = defaultdict(list)
for k, v in s:
	d[k].append(v)
	
print(list(d.items()))
