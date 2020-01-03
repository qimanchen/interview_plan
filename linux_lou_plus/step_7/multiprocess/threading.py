#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading

def hello(name):
	print('child thread: {}'.format(threading.get_ident()))
	print('Hello ' + name)
	
def main():
	t = threading.Thread(targer=hello, args=('shiyanlou', ))
	t.start()
	t.join()
	print('main thread: {}'.format(threading.get_ident()))
	
if __name__ == "__main__":
	main()
