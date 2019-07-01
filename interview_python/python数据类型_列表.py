#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
数据类型 - 列表
30-
"""

"""
30. 已知AList = [1,2,3,1,2],对AList元素去重,写出具体过程
	list(set(AList))
"""

"""
31. 如何实现 "1,2,3" 变成["1", "2", "3"]
	"1, 2, 3".split(",")
"""

"""
32. 给定两个list, A和B, 找出相同元素和不同元素
	setA = set(A)
	setB = set(B)
	sameList = setA & setB
	diffList = setA ^ setB
	
"""

"""
33. [[1,2], [3,4], [5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
	a = [[1,2], [3,4], [5, 6]]
	result = [i for midList in a for midList in a]
"""

"""
34. 合并列表[1,5,7,9] 和 [2,2,6,8]
	使用extend和+都可以

"""

"""
35. 如何打乱一个列表的元素
	import random
	random.shuffle(a)
"""