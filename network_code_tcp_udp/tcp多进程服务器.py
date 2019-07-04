#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多进程服务器
"""

import socket
from multiprocessing import *
from time import sleep


# 处理客服端请求
# 设置每个进程
def dealWithClient(newSocket, destAddr):
	"""
	"""
	while True:
		recvData = newSocket.recv(1024)
		if len(recvData) >0:
			# 检测客户端是否已经关闭
			print('recv[%s]: %s' % (str(destAddr), recvData))
		else:
			print('[%s] 客户端已经关闭' % str(destAddr))
			break
	# 关闭当前服务套接字
	newSocket.close()
	

def main()
	# 主程序
	
	serSocket = socket.socket(socket.AF_INEt, socket.STREAM)
	# 设置端口复用 -- 避免 2MSL
	serSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	# 绑定窗口
	localAddr = ('', 7788)
	serSocket.bind(localAddr)
	
	serSocket.listen(5)
	
	try:
		while True:
			print("等待新客户端的到来")
			
			newSocket, destAddr = serSocket.accept()
			
			print("处理一个到来的客户端[%s]" % str(destAddr))
			
			client = Process(target=dealWithClient, args=(newSocket, destAddr))
			
			client.start()
			
			# 因为已经向子进程中copy了一份，所以父进程中这个套接字没用了
			newSocket.close()
	finally:
		# 当前所有客服端服务完，表示不再接收新的客户端的到来
		serSocket.close()
		
	
if __name__ == "__main__":
	main()

			