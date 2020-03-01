#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理apache日志
日志格式
	193.252.243.232 - - [29/Mar/2009:06:05:34 +0200] "GET /index.php HTTP/1.1" 2008714 "-" "Mozilla/5.0 (compatible; PJBot/3.0; +http://crawl.pagesjaunes.fr/robot)" "-"
	客户端IP,远程登入名称，认证的远程用户
	请求时间，UTC时差，请求的http方法
	http协议，http状态码
	服务端发送过来的字节数
	访问来源
	客户浏览器信息
"""
from __future__ import print_function
from collections import Counter


def get_PV_UV():
	"""统计PV，UV"""
	ips = []
	with open('access.log') as f:
		for line in f:
			ips.append(line.split()[0])
	print("PV is {0}".format(len(ips)))
	print("UV is {0}".format(len(set(ips))))


def get_popular_resource():
	"""
	统计每个资源访问次数，并得出前十
	"""
	c = Counter()
	with open('access.log') as f:
		for line in f:
			c[line.split()[6]] += 1
	print("Popular resources: {0}".format(c.most_common(10)))


def get_error_access():
	"""
	统计错误访问次数
	2xx,3xx视为访问正确
	4xx,5xx视为访问出错
	"""
	d = {}
	with open('access.log') as f:
		for line in f:
			key = line.split()[8]
			d.setdefault(key,0)
			d[key] += 1
	sum_requests = 0
	error_requests = 0
	
	for key, val in d.iteritems():
		if int(key) >= 400:
			error_requests += val
		sum_requests += val
	print('error rate :{0:.2f}%'.format(error_requests*100.0/sum_requests))