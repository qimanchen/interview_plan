#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
单进程服务器
"""

import socket


def singleProcessServer():
	# 创建套接字
	serSocket = socket.socket(socket.AF_INET, socket.STREAM)
	
	# 重复使用绑定的信息（端口）
	serSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	# 绑定指定端口
	localAddr = ('', 7788)
	serSocket.bind(localAddr)
	
	# 开启监听
	serSocket.listen(5)
	
	while True:
		print("---- 主进程  等待新客户端的到来 -------")
		
		newSocket, desAddr = serSocket.accept()
		
		print("---- 主进程  接下来负责数据处理[%s] ------" % str(destAddr))
		
		try:
			while True:
				recvData = newSocket.recv(1024)
				if len(recvData) > 0:
					print('recv[%s]: %s' % (str(destAddr), recvData))
				else:
					print('[%s]客户端已经关闭'%str(destAddr))
					break
		finally:
			newSocket.close() # 防止socket未关闭
	serSocket.close() # 监听socket关闭
	