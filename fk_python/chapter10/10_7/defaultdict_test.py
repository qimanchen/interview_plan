#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
defaultdict -- dict的子类
程序试图根据不存在的key来访问dict，提供一个default_factory的属性
"""

from collections import defaultdict
my_dict = {}

# 以int函数的返回值为默认的值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a'])
print(my_dict['a'])
