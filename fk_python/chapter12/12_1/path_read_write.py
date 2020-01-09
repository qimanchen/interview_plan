#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Path读写文件
read_bytes() # 读取二进制数据
read_text(encoding=None, errors=None) # 读取文本数据

write_bytes(data) # 写入字节数据
write_text(data, encoding=None, errors=None) # 写入文本数据
"""

from pathlib import *

p = Path('a_test.txt')

# 返回输入的字符数
result = p.write_text('''有一个美丽的新世界
它在远方等我
哪里有天真的孩子
还有姑娘的酒窝''', encoding="GBK")
print(result)

# 读对应的数据
content = p.read_text(encoding='GBK')
print(content)

# 读取字节内容
bb = p.read_bytes()
print(bb)