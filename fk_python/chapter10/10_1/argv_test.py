#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sys 模块中的argv说明
"""

from sys import argv

print(len(argv))
# argv第一参数为python程序本身 -- argv[0]
# 如果参数中包含空格，需要用双引号("")括起来 -- python *.py "Python Swift"

# 打印出对应的参数
for arg in argv:
	print(arg)