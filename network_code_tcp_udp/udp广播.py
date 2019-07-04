#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
udp广播
"""


import socket
import sys

# 指定广播地址
dest = ('<broadcast>', 7788)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 以广播的形式发送数据到本网络的所有电脑
s.sendto('Hi', dest)

print("等待对方回复（按ctrl+c退出）")

while True:
	(buf, address) = s.recvfrom(2048)
	print(f"Received from {address}: {buf}")