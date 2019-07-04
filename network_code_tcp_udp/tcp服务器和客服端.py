#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tcp通信
服务器和客服端
"""
import socket


# 服务器
def tcpServer():
	tcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口信息
	address = ('', 7788)
	tcpSerSocket.bind(address)
	
	# 使用socket创建的套接字属性是主动的，使用listen将其变为被动的
	tcpSerSocket.listen(5)
	
	# 如果有新的客服端到来时，那么产生一个新的套接字为其服务
	newSocket, clientAddr = tcpSerSocket.accept()
	
	# 接收对方发送过来的数据，最大接收1024字节
	recvData = newSocket.recv(1024)
	print(f'接收到的数据为: {recvData}')
	
	# 发送一些信息到客服端
	newSocket.send("Thank You!")
	
	# 关闭这个服务
	newSocket.close()
	
	# 关闭监听套接字
	tcpSerSocket.close()

# 客服端

def tcpClient():
	tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 链接服务器
	serAddr = ('192.168.1.102', 7788)
	tcpClientSocket.connect(serAddr)
	
	# 提示用户输入数据
	sendData = input("请输入数据: ")
	
	tcpClientSocket.send(sendData)
	
	# 接收对方发送过来的数据, 最大接收1024个字节
	recvData = tcpClientSocket.recv(1024)
	print(f'接收到的数据为: {recvData}')
	
	# 关闭套接字
	tcpClientSocket.close()