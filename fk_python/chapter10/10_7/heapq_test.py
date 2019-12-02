#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heapq模块说明

python中对 -- 堆 这个数据结构的支持
"""
from heapq import *

my_data = list(range(10))
my_data.append(0.5)

# 对my_data应用堆属性
heapify(my_data) # 无返回值
# heappush -- 向堆中加入新的元素
heappush(my_data, 7.2)

# heappop -- 弹出堆中最小元素
heappop(my_data)

# heapreplace 弹出最小元素，压入指定元素
heapreplace(my_data, 8.1)

# !!! 这两个方法，不会改变原数组
# nlargest获取最大或最小的n个元素
nlargest(3, my_data)

# nsmallest获取最小的n个元素
nsmallest(4,my_data)