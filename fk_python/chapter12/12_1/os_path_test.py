#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
os.path

# exists()判断目录是否存在

getctime() 创建时间
getmtime() 最后一次修改时间
getatime() 最后一次访问时间
"""
import os
import time

print(os.path.abspath("abc.txt")) # 获取绝对路径

print(os.path.commonprefix(['/usr/lib', '/usr/local/lib'])) # 获取共同前缀名

print(os.path.commonpath(['/usr/lib', '/usr/local/lib'])) # 获取共同路径

print(os.path.dirname('abc/xyz/README.txt')) # 获取目录

print(os.path.exists('abc/xyz/README.txt')) # 判断文件是否存在

# print(time.ctime(os.path.getatime('os_path_test.py'))) # 时间格式

print(os.path.getsize('os_path_test.py')) # 获取文件大小

print(os.path.isfile('os_path_test.py')) # 判断是否为文件

print(os.path.isdir('os_path_test.py')) # 判断是否为目录

print(os.path.samefile('os_path_test.py', './os_path_test.py')) # 判断是否为同一个文件