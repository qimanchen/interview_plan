#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
argparse

# 显示设置
$ python test_argparse.py --host=127.0.0.1 -t
# 使用默认值
$ python test_argparse.py
"""

from __future__ import print_function
import argparse


def _argparse():
	"""
	add_argument(name or flags, action, nargs, const, default, type, choices, required, help, metavar, dest)
	name or flags -- 参数符号
	action 默认store,动作
	nargs 参数个数
	const 需要的常量
	default 不指定参数时的默认值
	type 参数类型
	choices 参数允许的值
	required 可选参数是否可以省略
	help 参数的帮助信息
	metavar 在useage说明中参数的名称
	dest 参数解析后的名称
	"""
	parser = argparse.ArgumentParser(description="This is description")
	parser.add_argument('--host', action='store',
	dest='server', default="localhost", help='connect to host')
	
	parser.add_argument('-t', action='store_true', default=False, dest='boolean_switch', help='Set a switch to true')
	
	# 解析参数
	return parser.parse_args()
	
def main():
	parser = _argparse()
	print(parser)
	print('host =', parser.server)
	print('boolean_switch=', parser.boolean_switch)
	
	
if __name__ == "__main__":
	main()
