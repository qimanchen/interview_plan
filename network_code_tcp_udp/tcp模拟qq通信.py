#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


"""
模拟QQ聊天
"""
import socket


# 客服端

def client():
	
	tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 链接服务器
	serAddr = ('192.168.0.102', 7788)
	tcpClientSocket.connect(serAddr)
	
	while True:
		
		# 提示用户输入数据
		sendData = input("send: ")
		
		if len(sendData) > 0:
			tcpClientSocket.send(sendData)
		else:
			break
		
		# 接收服务端反馈的信息
		recvData = tcpClientSocket.recv(1024)
		print(r'recv: {recvData}')
		
	# 关闭套接字
	tcpClientSocket.close()
	
	
# 服务器端
def server():
	tcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口
	address = ('', 7788)
	tcpClientSocket.bind(address)
	
	# 设定监听
	tcpClientSocket.listen(5)
	
	while True:
		
		newSocket, clientAddr = tcpSerSocket.accept()
		
		while True:
			
			recvData = newSocket.recv(1024)
			
			# 检测数据长度
			if len(recvData) > 0:
				print(f'recv: {recvData}')
			else:
				break
			
			# 发送一些数据给客户端
			sendData = input("send: ")
			newSocket.send(sendData)
		# 关闭这个socket
		newSocket.close()
	tcpSerSocket.close()
