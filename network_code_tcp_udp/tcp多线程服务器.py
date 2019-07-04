#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多线程服务器
"""

from socket import *
from threading import Thread
from time import sleep


# 处理客户端请求
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
	
	
def main():
	
	serSocket = socket(AF_INEt, SOCK_STREAM)
	
	serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	
	localAddr = ('', 7788)
	serSocket.bind(localAddr)
	serSocket.listen(5)
	
	try:
		while True:
			print ("等待客户端的到来")
			newSocket, destAddr = serSocket.accept()
			
			print("处理来自[%s]客户端的数据" % str(destAddr))
			client = Thread(target=dealWithClient, args=(newSocket, destAddr))
			client.start()
			
			# 因为线程中共享这个套接字，如果关闭此套接字，会导致这个套接字不可用
			# 但此时这个套接字还在接收数据，不能关闭
			# newSocket.close()
	finally:
		serSocket.close()
		

if __name__ == "__main__":
	main()
