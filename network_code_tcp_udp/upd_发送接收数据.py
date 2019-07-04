#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
udp网络-发送数据

1. 创建客服端套接字
2. 发送/接收数据
3. 关闭套接字
"""

import socket

# 发送数据
# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 指定接收方地址
sendAddr = ('192.168.1.103', 8080)

bindAddr = ('', 7788)
udpSocket.bind(binAddr) # 绑定服务器端的端口号
# 从键盘获取输入数据
sendData = input("请输入要发送的数据: ")

# 发送数据到指定的电脑上
# sendto()格式 sendto(数据包, (目标ip, 对应port))
udpSocket.sendto(sendData, sendAddr)

# 等待接收方发送回来的数据
# 接收方的端口是内部调度程序决定的
recvData = udpSocket.recvfrom(1024) # 接收数据的最大字节数

# 显示对方发送的数据
print(recvData)
# recvData数据格式(发送的数据, (ip, port))

# 关闭套接字
udpSocket.close()