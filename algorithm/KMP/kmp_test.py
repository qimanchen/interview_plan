#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
京东求最短加长串
"""


def get_next(str2):
	"""
	得到str2的next数组
	"""
	if len(str2) == 1:
		return -1
	_next = [None]*len(str2)
	_next[0] = -1
	_next[1] = 0
	i = 2
	cn = 0
	while i < len(str2):
		if str2[i-1] == str2[cn]:
			cn += 1
			_next[i] = cn
			i += 1
		elif _next[i] == -1:
			cn = _next[cn]
		else:
			_next[i] = 0
			i += 1
	return _next
	
	
def kmp(str1, str2):
	"""
	kmp实现主方法
	"""
	_next = get_next(str2)
	str1_move = 0
	str2_move = 0
	
	while str1_move < len(str1) and str2_move < len(str2):
		if str1[str1_move] == str2[str2_move]:
			str1_move += 1
			str2_move += 1
		elif _next[str2_move] == -1:
			str1_move += 1
		else:
			str2_move = _next[str2_move]
	return str1_move-str2_move if str2_move == len(str2)else -1
	

if __name__ == "__main__":
	str2 = "ababcababak"
	str1 = "cgababcababakdef"
	str3 = "ababcababtk"
	print(kmp(str1,str2))