#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
数据类型-字典
36-
"""

"""
36. 字典操作中del和pop有什么区别
	del可以根据索引来删除元素，没有返回值
	pop可以根据索引弹出一个值，然后接收它的返回值
"""

"""
37. 按字典内的年龄排序
	d1 = [
				{'name': 'alice', 'age':38},
				{'name': 'bob', 'age':18},
				{'name': 'Carl', 'age':28}
	]
	
	sorted(d1, key=lambda x: x['age'])
"""

"""
38. 请合并下面两个字典 a={"A":1,"B":2},b={"C":3,"D":4}
	a.update(b)
	或者
	{**a, **b} -- 解包的方式
"""

"""
39. 如何使用生成式的方式生成一个字典，写一段功能代码
	d = {'a':'1', 'b':'2'}
	print({v:k for k, v in d.items()})
"""