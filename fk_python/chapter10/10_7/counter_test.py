#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counter 自动统计容器中各元素出现的次数
Counter 初始化
字符串： 对字母的统计
list,tuple： 对每个点的统计
dict: 直接返回字典
"""


from collections import Counter

c1 = Counter()

# 如果初始化的对象为字符串，那么针对的则是字母个数的统计
c2 = Counter('hannah')
print(c2)

c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)

# 针对字典的统计，那么就是针对字典的输出
c4 = Counter({'red': 4, 'blue': 2})
print(c4)

c5 = Counter(Python=4, Swift=8)
print(c5)