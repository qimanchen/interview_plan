#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Path -- PurePath的子类，可以真正访问底层的文件系统
获取路径的各种属性，判断文件是否存在，对文件读写
"""

# is_xxx()判断该Path对应的路径中是否为xxx
# exists() 判断该Path中对应的目录是否存在
# iterdir() 判返回Path对应目录下所有子目录和文件
# glob()判断Path对应目录及其子目录下匹配指定模式的所有文件
from pathlib import *

p = Path('.') # 获取当前目录
for x in p.iterdir():
	print(x) # 遍历当前目录下的所有文件和子目录
	
p = Path('../') # 获取上一级目录
for x in p.glob('**/*.py'):
	print(x)
	
p = Path(r'H:\gitHub_project\interview_plan\fk_python\chapter12')
# 获取目录及其子目录下对应的所有的.py文件
for x in p.glob('**/*.py'):
	print(x)