#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counter一些方法的使用
elements() -- 返回所有元素的迭代器
most_common([n]) -- 返回Counter中出现最多的n各元素
substract([iterable-or-mapping]) -- 计算减去之后各元素出现的次数
"""

from collections import Counter

cnt = Counter()

print(cnt['Python']) # 0

for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
	cnt[word] += 1
print(cnt)

print(list(cnt.elements()))

chr_cnt = Counter('abracadabra')

print(chr_cnt.most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

c.subtract(d)
print(c)

e = Counter({'x': 2, 'y': 3, 'z': -4})

del e['y']
print(e)

print(e['w'])

del e['w']

print(e['w'])