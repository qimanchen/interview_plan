#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
udp应用：echo服务器
"""

import socket

# 创建套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定相关信息
bindAddr = ('', 7788)
udpSocket.bind(bindAddr)

num = 1 # 记录消息数

while True:
	# 等待接收对方发送的数据
	recvData = udpSocket.recvfrom(1024)
	
	# 反馈信息
	udpSocket.sendto(recvData[0], recvData[1])
	
	print(f"recvData[1] 说: recvData[0]")
	num += 1
	
# 关闭套接字
udpSocket.close()