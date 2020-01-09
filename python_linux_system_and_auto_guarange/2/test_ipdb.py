#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdb调试命令
	break/b 设置断点
	continue/cont/c 继续执行至下一个断点
	next/n 执行下一行，如果下一行是子程序，不会进入子程序
	step/s 执行下一行，如果下一行是子程序，进入子程序
	where/bt/w 打印堆栈轨迹
	enable 启用禁用的断点
	disable 禁用启用的断点
	pp/p 打印变量或表达式
	list/l 根据参数值打印源码 -- 行数
	up/u 移动到上一层堆栈
	down/d 移动到下一层堆栈
	restart/run 重新开始调试
	args/a 打印函数参数
	clear/cl 清除所有的断点
	return/r 执行到当前函数结束
"""


from __future__ import print_function
import ipdb


def sum_nums(n):
    """
    在代码中设置set_trace()来设置断点进行调试
    """
    s = 0
    for i in range(n):
        ipdb.set_trace()
        s += i
        print(s)


if __name__ == "__main__":
    sum_nums(5)
