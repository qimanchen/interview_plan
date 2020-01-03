#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
purepath的几点注意
"""
from pathlib import *

# UNIX风格的路径区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO')) # False

# Windows风格的路径不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO')) # True

# 不同风格的路径可以判断是否相等 -- 一直为False
# 不同风格的路径不可以比较大小 -- TypeError
# UNIX和Windows都可以用斜杠“/”作为连接运算符

# PurePath的实质是string，可以用str转换为字符串对象（恢复为对应平台的风格）

PurePath.as_posix() # 转换成UNIX分割的字符串
PurePath.as_url() # 将绝对路径转换成url