#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
数据类型 - 综合
41-
"""

"""
41. 下列字典对象键类型不正确的是？
	只有可hash的对象才能做字典的键，
	列表是可变类型，不可hash
"""

"""
42. 如何交换字典{"A":1, "B":2}的键和值
	a = {"A":1, "B":2}
	{v: k for k, v in a.items()}
	dict(zip(s.values(), s.keys()))
"""

"""
43. python里面如何实现tuple和list的转换
	通过类型强制转换
	tuple -> list list()
	list -> tuple tuple()

"""

"""
44. 如何对生成器类型的对象实现切片实现部分元素的选择
	对itertools模块的考察
	使用islice()方法来实现
	from itertools import islice
	gen = iter(range(10)) # iter()是用来生成迭代器
	# 第一个参数是迭代器，第二参数是起始索引，第三个参数结束索引
	for i in islice(gen, 0, 4):
		print(i)

"""

"""
45. 请将[i for i in range(3)] 改成生成器
	(i for i in range(3)) -- 使用小括号就是生成器了
"""

"""
46. a="hello"和b="你好"编码成bytes类型
	1. 在字符串前面加 b -> a = b"hello"
	2. 使用bytes方法 -> b = bytes("你好", "utf-8")
	3. 使用字符串encode方法 -> c = "hello".encode("utf-8")
"""

"""
47. 下面代码输出结果是什么
	a = (1,2,3,[4,5,6,7], 8)
	a[2] = 2
	
	结果：
		结果出错，元组是不能改变的
"""

"""
48. 下面代码输出结果是什么
	a = (1,2,3,[4, 5,6,7],8)
	a[3][0] = 2
	
	结果：
		a = (1,2,3,[2,5,6,7],8)
	元组内的内存地址是不变的，但内部元素如果是可变类型，那么还是可变的
	
"""