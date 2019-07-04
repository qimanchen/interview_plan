#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tftp 客服端

每次发送文件（数据大小）512字节

两个字节记录 -- 数据序号
两个字节记录 -- 数据包功能 -- 操作码

操作码			功能
1						读请求，即下载
2 						写请求上传
3 						表示数据包，DATa
4 						确认码 ACK
5 						错误
"""


import socket
import struct
import sys


def main():
	# 确认输入参数
	if len(sys.argv) != 2:
		print('-'*30)
		# 程序运行样例
		print('tips: ")
		print("python xxx.py 192.168.1.1")
		print('-'*30)
		exit()
	else:
		ip =sys.argv[1]
		
	# 创建udp套接字
	udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 够找下载请求数据
	cmd_buf = struct.pack("!H8sb5sb", 1, 'test.jpg', 0, 'octet', 0)
	# 对应信息 H -- 两个字节，8s -- 8个字符串类型，b -- 一个字节
	
	# 发送下载文件请求到指定服务器
	sendAddr = (ip, 69)
	udpSocket.sendto(cmd_buf, sendAddr)
	
	# 记录发送数
	p_num = 0
	recvFile = ''
	
	while True:
		# 接收文件
		recvData, recvAddr = udpSocket.recvfrom(1024)
		
		recvDataLen = len(recvData)
		
		cmdTuple = struct.unpack("!HH", recvData[:4])
		# 从接收到的数据中取得相应的ACK信息
		
		cmd = cmdTuple[0] # 操作码
		currentPackNum - cmdTuple[1] # 对应的包编号
		
		if cmd == 3: # 检测操作码，是否为数据包
			# 如果是第一次接收数据就创建文件
			if currentPackNum == 1:
				recvFile = open('test.jpg', 'a')
			
			# 包编号是否与上次相等
			if p_num +1 == currentPackNum:
				recvFile.write(recvData[4:])
				p_num += 1
				print(f'{p_num}接收到的数据')
				
				ackBuf = struct.pack("!HH", 4, p_num)
				# 发送反馈信息到服务端
				udpSocket.sendto(ackBuf, recvAddr) # 接着收数据
				
			if recvDataLen < 516:
				# 数据长度小于512，数据发送完成
				recvFile.close()
				print("已经下载成功")
				break
		elif cmd == 5: # 是否为错误应答
			print(f"error num {currentPackNum}")
			break
			

if __name__ == "__main__":
	main()
