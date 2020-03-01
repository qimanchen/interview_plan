#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
求解最长回文子串问题
使用Manacher方法
"""


def manacher(string):
	"""
	主函数
	"""
	if len(string) < 2:
		return string
	string = "#" + "#".join(list(string)) + "#"
	array = [None]*len(string)
	c = -1
	r = -1
	max_value = 0
	max_index = 0
	for i in range(len(string)):
		array[i] = min(array[2*c-i], r-i) if r > i else 1
		while i+array[i]<len(string) and i-array[i] > -1:
			if string[i+array[i]] == string[i-array[i]]:
				array[i] += 1
			else:
				break
		if i+array[i] > r:
			r = i + array[i]
			c = i
		if r == len(string):
			print(c,r)
			print(len(string))
			break
		if max_value < array[i]:
			max_value = array[i]
			max_index = i
	return max_value - 1,string[max_index-max_value+1:max_index+max_value-1].replace("#", "")

def manacher_for_min(string):
	"""
	对于一个字符串后面添加最少的元素，构成回文串
	"""
	if len(string) < 2:
		return string
	string = "#" + "#".join(list(string)) + "#"
	array = [None]*len(string)
	c = -1
	r = -1
	for i in range(len(string)):
		array[i] = min(array[2*c-i], r-i) if r > i else 1
		while i+array[i]<len(string) and i-array[i] > -1:
			if string[i+array[i]] == string[i-array[i]]:
				array[i] += 1
			else:
				break
		if i+array[i] > r:
			r = i + array[i]
			c = i
		if r == len(string):
			print(c,r)
			print(len(string))
			mid = string +string[:c][::-1]
			print(mid.replace("#",""))
			break

def manacher_for_min2(string):
	"""
	对于一个字符串前面添加最少的元素，构成回文串
	"""
	string = string[::-1]
	if len(string) < 2:
		return string
	string = "#" + "#".join(list(string)) + "#"
	array = [None]*len(string)
	c = -1
	r = -1
	for i in range(len(string)):
		array[i] = min(array[2*c-i], r-i) if r > i else 1
		while i+array[i]<len(string) and i-array[i] > -1:
			if string[i+array[i]] == string[i-array[i]]:
				array[i] += 1
			else:
				break
		if i+array[i] > r:
			r = i + array[i]
			c = i
		if r == len(string):
			mid = string +string[:c-array[i]+1][::-1]
			print(string)
			return mid.replace("#","")[::-1]

		
if __name__ == "__main__":
	# string = "abc1234321ab"
	# string = "chenqimanam"
	string = "abcd"
	print(manacher_for_min2(string))
			
	