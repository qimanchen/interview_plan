#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
udp 模拟qq通信
"""

import socket
from threading import Thread


# 接收消息
def recv_data():
	
	while True:
		recv_info = udpSocket.recvfrom(1024)
		print("\r>> %s: %s" % (str(recv_info[1]), recv_info[0])
		# 输出格式 (ip, port): 接收到消息
		

# 数据发送
def send_data():
	
	while True:
		send_info = input("\r<< ")
		udpSocket.sendto(send_info.encode("utf-8"), (dest_ip, dest_port))
		# 注意发送的消息要进行编码
		

# 定义相应的全局
udpSocket = None
dest_ip = ""
dest_port = 0


# 主函数
def main():
	global udpSocket
	global dest_ip
	global dest_port
	
	# 获取相应ip和port
	dest_ip = input("receive ip: ")
	dest_port = int(input("receive port: "))
	
	udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	updSocket.bind(("", 7788))
	
	tr = Thread(target=recv_data)
	tr = Thread(target=send_data)
	
	tr.start()
	tr.start()
	
	tr.join()
	tr.join()
	
	
if __name__ == "__main__":
	main()
