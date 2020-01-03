#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pack布局管理器
可通过help(tkinter.Label.pack) -- 查看pack()方法支持的选项
"""
from tkinter import *


root = Tk()

root.title("Pack 布局")

for i in range(3):
	lab = Label(root, text="第%d个Label" % (i+1), bg="#eeeeee")
	lab.pack()
	
root.mainloop()