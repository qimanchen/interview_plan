#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Frame -- pack
"""
from tkinter import *


class App:
	def __init__(self, master):
		self.master = master
		self.initWidgets()
		
	def initWidgets(self):
		fm1 = Frame(self.master)
		# 从顶部开始排列
		fm1.pack(side=LEFT, fill=BOTH, expand=YES)
		# x方向拉伸
		Button(fm1, text="first").pack(side=TOP, fill=X, expand=YES)
		Button(fm1, text="second").pack(side=TOP, fill=X, expand=YES)
		Button(fm1, text="third").pack(side=TOP, fill=X, expand=YES)
		
		fm2 = Frame(self.master)
		# 从右边开始排列，容器x方向的间距为10
		# 当未设置填充时，不会在任何方向上填充
		fm2.pack(side=LEFT, padx=10, expand=YES)
		Button(fm2, text="first").pack(side=RIGHT, fill=Y, expand=YES)
		Button(fm2, text="second").pack(side=RIGHT, fill=Y, expand=YES)
		Button(fm2, text="third").pack(side=RIGHT, fill=Y, expand=YES)
		
		fm3 = Frame(self.master)
		# 放置在右边，并从底部开始排列
		fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
		Button(fm3, text="first").pack(side=BOTTOM, fill=Y, expand=YES)
		Button(fm3, text="second").pack(side=BOTTOM, fill=Y, expand=YES)
		Button(fm3, text="third").pack(side=BOTTOM, fill=Y, expand=YES)
		
		
if __name__ == "__main__":
	root = Tk()
	root.title("Pack布局")
	display = App(root)
	root.mainloop()