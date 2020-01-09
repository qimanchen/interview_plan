#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fnmatch 支持类似Unix Shell的文件名匹配

fnmatch.fnmatch(filename, pattern): 判断指定文件是否匹配指定pattern

规则：
	* -- 任意个数的任意字符
	? -- 一个任意字符
	[] -- 字符序列 [a-z]
	[!字符序列] -- 不存在的
"""
from pathlib import *
import fnmatch

for file in Path(r'H:\gitHub_project\interview_plan\fk_python\chapter12\12_2').iterdir():
	# file对应着绝对路径
	if fnmatch.fnmatch(file, '*_test.py'): 
		# 不区分大小写
		# fnmatch.fnmatchcase(filename, pattern) # 区分大小写
		print(file)
		
		
name = ['a.py', 'b.py', 'c.py', 'd.py']
# 对name列表进行过滤
sub = fnmatch.filter(name, '[ac].py')
print(sub)