#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
语言特性
1-6
"""

"""
1. 谈谈python与其他语言的区别
	python语法简洁优美，应用领域广泛，拥有强大的第三发库
	他是一门强类型的可移植、可拓展、可嵌入的解释型语言，
	属于动态语言；
	与c语言比：
		python代码简洁，少量代码，
		但python的运行速度相对较慢
"""

"""
2. 简述解释型和编译型语言
	解释型语言：
		运行程序的时候才翻译，每执行一次，要翻译一次，效率低；
	编译型语言：
		直接编译成机型可以执行的，只翻译一次，所以效率相对较高
"""

"""
3. python的解释器种类以及相关特性
	CPython：
		c语言开发，使用最广的解释器；
	IPython： 	基于cPython之上的一个交互式计时器，交互方式增强功能和cPython一样；
	PyPy：
	目标是执行效率，采用JIT技术，对python代码进行动态编译，
	提高执行效率；
	JPython：
	运行在Java上的解释器，直接把Python代码编译成Java字节码执行
	IronPython：
	运行在微软.NET平台上的解释器，把Python编译成.NET的字节码
"""

"""
4. Python3 和 Python2的区别
	1. print在Python3中是函数必须加括号，Python2中是class
	2. python2中使用xrange，python3使用range
	3. python2中默认的字符串类型是ASCII，python3中默认是Unicode
	4. python2中/的结果是整形，python3中是浮点型
	5. python2中声明元类：_metaclass=MetaClass,
		 python3中声明元类：class newclass(metaclass=MetaClass):pass

"""

"""
5. python3与python2中int和long区别
	1. python2有int和long类型，int类型最大值不能超过sys.maxint
	而这个最大值是平台相关的，可以通过在数字末尾附上一个L来定义长整形
	比int更大的数字范围；
	2. python3只有一种整数类型int，大多数情况下与python2的长整型类似
"""

"""
6. xrange与range的区别
	xrange是python2中的用法，python3中只有range
	xrange和range的用法完全相同，不同的是前者生成的不是一个list对象，
	而是一个生成器；
"""