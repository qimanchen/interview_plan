#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用ChainMap实现，获取变量时通过
局部定义，全局定义，内置定义的顺序执行搜索
"""

from collections import ChainMap
import builtins


my_name = "孙大圣"


def test():
	my_name = 'yeeku'
	
	pylookup = ChainMap(locals(), globals(), vars(builtins))
	
	print(pylookup['my_name'])
	print(pylookup['len'])
	
	
if __name__ == '__main__':
	test()