#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
udp应用聊天室
"""


import socket
from time import ctime


udpSocket = socket.socket(AF_INET, SOCK_DGRAM)

bindAddr = ('', 7788)
udpSocket.bind(bindAddr)

while True:
	recvData = udpSocket.recvfrom(1024)
	# (Data, (ip, port))
	print(recvData)
	
udpSocket.close() # 关闭