#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class User(object):
	
	def __init__(self, name, passwd):
		self.name = name
		self.passwd = passwd
		
	def validLogin(self):
		print("验证%s的登录" % self.name)
		
class Role(object):
	
	def __init__(self, name):
		self.name = name
		
	def __call__(self):
		print('执行Role对象')

def foo():
	print('--foo函数--')
	
if __name__ == "__main__":
	# u = User('crazyit', 'leegang')
	# print(hasattr(u.name, '__call__'))
	# print(hasattr(u.passwd,'__call__'))
	# print(hasattr(u.validLogin, '__call__'))
	
	# r = Role('sb')
	# r()
	foo()
	foo.__call__()