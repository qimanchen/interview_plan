#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
gevent协程

不用像greenlet一样人工切换

遇到IO时，切换到其他greenlet
防止一直在等待io
"""

import gevent

def f(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()


# gevent切换运行
def f(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		# 用来模拟一个耗时操作， 注意不是用time的sleep
		gevent.sleep(1)
		
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()