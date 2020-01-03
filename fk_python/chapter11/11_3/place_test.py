#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Place布局
指定位置，绝对布局
"""
from tkinter import *
import random


class App :
	def __init__(self, master):
		self.master = master
		self.initWidgets()
		
	def initWidgets(self):
		books = ("疯狂Python 讲义", "疯狂Swift讲义", "疯狂Kotlin 讲义", "疯狂Java 讲义", "疯狂Ruby 讲义")
		for i in range(len(books)):
			ct= [random . randrange(256) for x in range(3)]
			grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
			bg_color = "#%02x%02x%02x" % tuple(ct)
			
			lb = Label(root, text=books[i], fg="White" if grayness<125 else "Black", bg=bg_color)
			
			lb.place(x=20, y=36+i*36, width=180, height=30)
			
			
if __name__ == "__main__":
	root = Tk()
	root.title("Place布局")
	
	root.geometry("250x250+30+30")
	App(root)
	root.mainloop()