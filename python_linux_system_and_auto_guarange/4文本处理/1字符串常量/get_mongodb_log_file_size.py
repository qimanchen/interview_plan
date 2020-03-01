#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取MongoDB日志文件占用磁盘大小
"""

import os


def main():
	"""
	"""
	mongod_logs = [item for item in os.listdir('/var/mongo/log') if item.startswith('mongod.log')]
	sum_size = sum(os.path.getsize(os.path.join('/var/mongo/log',item)) for item in mongod_logs)