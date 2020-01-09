#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fileinput既可以从标准输入中读入数据，也可以从文件中读取数据
cat /etc/passwd | python read_from_fileinput.py
python read_from_fileinput.py < /etc/passwd
python read_from_fileinput.py /etc/passwd
python read_from_fileinput.py /etc/passwd /etc/hosts

# fileinput读取多个文件时
	filename -- 当前正在读取的文件明
	fileno -- 文件描述符
	filelineno -- 文件第几行
	isfirstline -- 是否为文件的第一行
	isstdin fileinput正在读取文件还是标准输入
"""

from __future__ import print_function
import fileinput

for line in fileinput.input():
	print(line, end=" ")