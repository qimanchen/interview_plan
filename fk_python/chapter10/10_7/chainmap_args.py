#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用ChainMap实现函数的参数范围的搜索顺序
python *.py -c arg1 -u arg2
执行顺序为 命令行输入的，系统环境，程序中的预设的
"""

from collections import ChainMap
import os, argparse

defaults = {'color': '蓝色', 'user': 'yeeku'}

# 创建程序的参数解析器
parser = argparse.ArgumentParser()

# 为参数解析器添加-u(--user) and -c(--color) 参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')

namespace = parser.parse_args()

command_line_args = {k:v for k,v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)

print(combined['color'])
print(combined['user'])
print(combined['PYTHONPATH'])