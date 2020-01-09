#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PurePath
"""
from pathlib import *

# PurePath根据环境返回对应的path类型
pp = PurePath('setup.py')
print(type(pp))

pp = PurePath('crazyit', 'some/path', 'info')
print(pp)

pp = PurePath(Path('crazyit'), Path('info'))
print(pp)

# 指定为UNIX类型路径
pp = PurePosixPath('crazyit', 'some/path', 'info')
print(pp)

# 当前路径
pp = PurePath()
print(pp)

# 多个根路径，最后一个根路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)

pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp)

# 在windows路径下，只有盘符才算根路径
pp = PureWindowsPath('c:/Windows', '/Program Files')
print(pp)

pp = PurePath("/etc")
print(pp)

# 多个斜杠和点号，系统会自动忽略
pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp)