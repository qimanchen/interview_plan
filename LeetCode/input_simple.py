#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


"""
测试输入
2
1 2 3 4
5 6 7 8

"""

# 指定测试样例数
def specialSampleNum():
	
	n = int(sys.stdin.readline().strip())
	
	for i in range(n):
		line = sys.stdin.readline().strip()
		
		numList = list(map(int, line.split()))
		print(numList, type(numList))
		
 
# 不指定测试样例数
def noSpecialSampleNum():
	
	while True:
		line = sys.stdin.readline().strip()
		
		if line == "":
			break
		numList = list(map(int, line.split()))
		print(numList, type(numList))


if __name__ == "__main__":
	noSpecialSampleNum()
