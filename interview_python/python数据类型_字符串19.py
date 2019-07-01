#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
数据类型-字符串
19-
"""

"""
19. 列举python中的基本数据类型
	python3中六个标准的数据类型：
	字符串(string)
	数字(digit)
	列表(list)
	元组(tuple)
	集合(sets)
	字典(dictionary)
	
"""

"""
20. 如何区分可变数据类型和不可变数据类型
	从对象内存地址来看：
		1. 可变数据类型，在内存地址不变的情况下，值可以改变
		列表和字典都死可变类型，但字典中的key值必须是不可变类型
		2. 不可变数据类型，内存改变，值也跟着变
		数字，字符串，布尔类型，都是不可变类型
	可以通过id()方法进行内存地址检测
"""

"""
21. 将“hello world”转换成首字母大写"Hello World"
	"hello world".title()
"""

"""
22. 如何检测字符串中只含有数字
	string.isdigit()
"""

"""
23. 将字符串'ilovechina'进行反转
	'ilovechina'[::-1]

"""

"""
24. python中字符串格式化方式你知道哪些
	%s， format，fstring(python3.6才开始支持)
"""

"""
25. 有一个字符串开头和末尾都有空格，请求写一个函数把这个空格去除
	" abcde ".strip()
	
	def strip_function(s1):
		return s1.strip()
"""

"""
26. 获取字符串"123456"最后两个字符
	"123456"[-2:]
	
"""

"""
27. 一个编码为GBK的字符串S，要将其转成UTF-8编码的字符串，如何？
	a = "S".encode("gbk").decode("utf-8","ignore")
"""

"""
28. (1) s="info: xiaoZhang 33 shandong",用正则切分字符串输出
		['info', 'xiaoZhang', '33', 'shandong']
		(2) a = "你好 中国", 去除多余的空格，只留一个空格
	(1)
		import re
		s = "info: xiaoZhang 33 shandong"
		res = re.split(r": | ",s)
	(2)
		s = "你好   中国"
		print(" ".join(s.split()))
		
"""

"""
29. 怎样将字符串转换为小写；单引号、双引号、三引号的区别
	1. 通过字符串方法 lower()实现
	2. 单引号和双引号实际没啥区别，就是嵌套使用时需要注意两者的组合
	三引号（单双）两个都可以声明长字符串时使用，如果使用docstring就
	需要使用双引号；
"""