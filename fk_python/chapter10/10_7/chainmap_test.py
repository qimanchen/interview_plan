#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChainMap -- 工具类
实现将多个 ”dict”链接到一起
实际上底层并未合并
"""
from collections import ChainMap

a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}

# 将多个dict链成一个
cm = ChainMap(a,b,c)
# 那么你可以直接像使用一个dict一样使用它
