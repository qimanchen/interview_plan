#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
单进程服务器 - 非阻塞模式
"""
import socket
import time
import random


def main():
	
	gSocketList = [] # 用来存储所有新链接的socket
	# 1. 创建套接字
	serSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 2. 设置端口可复用，避免两倍MSL
	serSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	# 3. 绑定指定服务器端口
	localAddr = ('', 7788)
	serSocket.bind(localAddr)
	
	# 4. 设置监听数
	serSocket.listen(1000)
	
	# 5. 将套接字设置为非堵塞
	# 设置为非堵塞后，恰巧没有客户端connect,
	# accept会产生一个异常，所以需要try来处理
	serSocket.setblocking(False)
	
	while True:
		
		# 测试
		try:
			newClientInfo = serSocket.accept()
		except Exception as result:
			pass
		else:
			print(f"一个新客户端到来: {newClientInfo}")
			newClientInfo[0].setblocking(False)
			# 将新来的客户端加入到维护列表中
			gSocketList.append(newClientInfo)
		
		# 用来存储需要删除的客户端信息
		needDelClientInfoList = []
		
		for clientSocket, clientAddr in gSocketList:
			# 检查每个被监听的客户端是否发送了信息
			try:
				recvData = clientSocket.recv(1024)
				if len(recvData) > 0:
					print('recv[%s]:%s' %(str(clientAddr), recvData))
				else:
					print('[%s]客户端已经关闭' % str(clientAddr))
					clientSocket.close()
					# 将关闭的客户端列表记录 -- 从gSocketList中移除
					needDelClientInfoList.append((clientSocket, clientAddr))
			except Exception as result:
				pass
		for needDelClientInfo in needDelClientInfoList:
			gSocketList.remove(needDelClientInfo)
			
			
# 客户端
def client():
	serverIp = input("请输入服务器IP: ")
	connNum = input("请输入需要链接的次数: ")
	
	gSocketList = []
	
	for i in range(int(connNum)):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((serverIp, 7788))
		gSocketList.append(s)
		print(i)
	while True:
		for s in gSocketList:
			# 模拟每个客户端发送信息
			s.send(str(random.randint(0, 100)))
			
if __name__ == "__main__":
	main()
