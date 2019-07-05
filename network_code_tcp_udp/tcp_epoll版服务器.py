#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
epoll版tcp服务器

优点：
	1. 没有并发限制
	2. 不是轮询的方式，只关注活跃的文件描述符
"""
import socket
import select


def main():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	s.bind(('', 7788))
	
	s.listen(5)
	
	# 创建一个epoll对象
	epoll = select.epoll()
	
	# 测试用来打印套接字对应的文件描述符
	# print(s.fileno())
	# print(select.EPOLLIN|select.EPOLLET)
	
	# 注册事件到epoll中
	# epoll.register(fd[, eventmask])
	# 注意，如果fd已经注册过，则会发生异常
	# 将创建的套接字添加到epoll的事件监听中
	
	"""
	参数说明：
		EPOLLIN -- 可读
		EPOLLOUT -- 可写
		EPOLLET -- ET模式
		
	epoll对文件描述符有两种模式： LT（默认）， ET模式
		LT: 应用程序可以不用立即处理，下次会再次响应
		ET: 应用程序必须立即处理，否则下次不会再次通知此事件
	"""
	epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)
	
	connections = {} # 存储对应socket服务端
	addresses = {} # 存储对应socket的地址
	
	# 循环等待客户端的到来或发送数据
	while True:
		
		# epoll 进行fd扫描的地方 -- 未指定超时时间则为阻塞等待
		epoll_list = epoll.poll()
		
		# 对事件进行判断
		for fd, events in epoll_list:
			
			# 如果是socket套接字创建的套接字被激活
			if fd == s.fileno():
				conn, addr = s.accept()
				
				print("有新客户端到来%s" % str(addr))
				
				# 将conn和addr信息分别保存起来
				connections[conn.fileno()] = conn
				addresses[conn.fileno()] = addr
				
				# 向epoll中注册连接socket的可读事件
				epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)
				
			elif events == select.EPOLLIN:
				# 从激活的fd上接收
				recvData = connections[fd].recv(1024)
				if len(recvData) > 0:
					print("recv: %s" % recvData)
				else:
					# 从epoll中移除该连接fd
					epoll.unregister(fd)
					
					# server侧主动关闭该连接fd
					connections[fd].close()
					print("%s---offline----" % str(addresses[fd]))
					

if __name__ == "__main__":
	main()
