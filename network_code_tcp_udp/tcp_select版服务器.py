#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
select版- tcp服务器

优点：跨平台

缺点：单个进程能监听的文件描述符的数量存在限制 1024
可以通过修改宏定义甚至重新编译内核的方式提升这一限制

与系统内存有关

2. 对socket的扫描是轮询的方式，效率低

"""

import select
import socket
import sys
import queue


def main():
	
	# 建立套接字
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口
	server.bind(('', 8888))
	server.listen(5)
	
	# 设置select输入，对应的监听列表
	inputs = [server, sys.stdin]
	# 这一部分在windows会出错
	running = True
	
	while True:
		
		# 调用select函数，阻塞等待
		# select监听三个，所有的输入data（外部发来的数据）、监控和接收所有要发出去的data, 监控错误信息
		readable, writeable, exceptional = select.select(inputs, [], [])
		
		# 数据抵达，循环
		for sock in readable:
			
			# 监听到有新的连接
			if sock == server:
				conn, addr = server.accept()
				# select 监听的socket
				inputs.append(conn)
			# 监听到键盘有输入
			elif sock == sys.stdin:
				cmd = sys.stdin.readline()
				running = False
				break
				
			# 有数据到达
			else:
				# 读取客户端连接发送的数据
				data = sock.recv(1024)
				if data:
					sock.send(data)
				else:
					# 移除select监听的socket
					inputs.remove(sock)
					sock.close()
		# 如果检测到有用户输入敲击键盘，那么就退出
		if not running:
			break
			
	server.close() # 关闭服务器
	


# 带有可写的版本
def main_with_writelist():
	serverIp = ('', 9999)
	
	# 保存客户端发送过来的消息，将消息放入队列中
	message_queue = {}
	input_list = []
	output_list = []
	
	server = socket.socket()
	server.bind(serverIp)
	server.listen(10)
	
	# 设置为非堵塞
	server.setblocking(False)
	
	# 初始化将服务器加入监听列表
	input_list.append(server)
	
	while True:
		
		# 开始select监听，对input_list中的服务端server进行监听
		stdinput, stdoutput, stderr = select.select(input_list, output_list, input_list)
		
		# 循环判断是否有客户端连接进来，当有客户端连接进来时，select将触发
		for obj in stdinput:
			# 判断当前触发的是不是服务端对象，当是时，有新客户端到来
			if obj == server:
				# 接收客户端的连接，获取客户端对象和客户端地址信息
				conn, addr = server.accept()
				print("client %s connected! " % str(addr))
				
				# 将客户端对象加入监听列表中，当客户端发送消息时触发
				input_list.append(conn)
				
				# 为连接客户端单独创建一个消息队列，用来保存客户端发送的消息
				message_queue[conn] = queue.Queue()
				
			else:
				# 客户端发送消息触发
				try:
					recv_data = obj.recv(1024)
					
					# 客户端未断开
					if recv_data:
						print("received %s from client %s " % (recv_data, str(addr)))
						# 将收到的消息放入各客户端的消息队列中
						message_queue[obj].put(recv_data)
						
						# 将回复操作放到output列表中，让select监听
						if obj not in output_list:
							output_list.append(obj)
					else:
						# 客户端主动关闭
						input_list.remove(obj)
						# 移除客服端对象的消息队列
						del message_queue[obj]
						print("\n[input] client %s disconnected" % str(addr))
				except ConnectionResetError:
					# 客户端断开类，将客户端的监听从input列表中移除
					input_list.remove(obj)
					# 移除客服端对象的消息队列
					del message_queue[obj]
					print("\n[input] client %s disconnected" % str(addr))
					
		# 如果现在没有客户端请求，也没有客户端发送消息时，开始对发送消息列表进行处理，是否需要发送消息
		for sendobj in output_list:
			try:
				# 如果消息队列中有消息，从消息队列中获取要发送的消息
				if not message_queue[sendobj].empty():
					# 从该客户端对象的消息队列中获取需要发送的消息
					send_data = message_queue[sendobj].get()
					sendobj.send(send_data)
				else:
					# 将监听移除等待下一次客户端发送消息
					output_list.remove(sendobj)
					
			except ConnectionResetError:
				# 客户端连接断开了
				del message_queue[sendobj]
				output_list.remove(sendobj)
				print("\n[output] Client %s disconnected" % str(addr))
if __name__ == "__main__":
	main_with_writelist()
