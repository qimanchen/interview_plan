#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grid布局管理工具

将空间分解成一个网格进行维护，行+列
"""
from tkinter import *


class App:
	def __init__(self, master):
		self.master = master
		self.initWidgets()
		
	def initWidgets(self):
		e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
		e.pack(side=TOP, pady=10)
		p = Frame(self.master)
		p.pack(side=TOP)
		
		names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/",".","=")
		
		for i in range(len(names)):
			b = Button(p, text=names[i], font=('Verdana', 20), width=6)
			b.grid(row=i//4, column=i%4)
			
			
if __name__ == "__main__":
	root = Tk()
	root.title("Grid布局")
	App(root)
	root.mainloop()