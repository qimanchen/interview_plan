#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KMP算法的实现
"""


def get_next_array(str2):
	"""
	得到待匹配子串的最长前缀和后缀
	ababc ababc t x
	            i-1 i
	0 -1
	1 0
	i next_str[i-1]+1 array[next_str[i-1]+1]
	如果不等，接着下去看前面的位置结果，迭代
	ababc ababtk
	ababc ababak
	"""
	if len(str2) == 1:
		return -1
	next = [None]*len(str2)
	next[0] = -1
	next[1] = 0
	i = 2
	cn = 0
	while i<len(next):
		if str2[i-1] == str2[cn]:
			next[i] = cn+1
			cn += 1
			i+=1
		elif cn >0:
			cn = next[cn]
		else:
			next[i] = 0
			i+=1
	return next
	

def kmp(str1, str2):
	"""
	算法执行
	return 包含的起始位置
	"""
	i1, i2 = 0, 0
	next = get_next_array(str2)
	while i1 < len(str1) and i2 < len(str2):
		if str1[i1] == str2[i2]:
			i1+=1
			i2+=1
		elif next[i2] == -1:
			i1+=1
		else:
			i2 = next[i2]
	return  i1 - i2 if i2 == len(str2) else -1
	
if __name__ == "__main__":
	str2 = "ababcababak"
	str1 = "cgababcababakdef"
	str3 = "ababcababtk"
	print(kmp(str1,str2))