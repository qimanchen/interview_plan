#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python面试问题
操作类题目
49-
"""

"""
49. python交换两个变量的值
	a,b = b, a
	这并不是元组解包，通过dis模块可以发现，
	这是交换操作的字节码ROT_TWO，在栈顶做两个值得互换操作
"""

"""
50. 在读文件操作时会使用read、readline、readlines简述它们各自的作用
	read: 每次读取整个文件，通常将用于将文件内容放到一个字符串变量中
	readline：一行一行输出，该方法会将文件内容加载到内存中，消耗资源
	readlines: 将文件的句柄生成一个生成器，然后去读就可以了
"""

"""
51. json序列化时，可以处理的数据类型有哪些，如何定制支持datetime类型
	可以处理类型：
		str、int、list、tuple、dict、bool、None
		datetime类不支持json序列化，所以需要进行拓展
		
"""