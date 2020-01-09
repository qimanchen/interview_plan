#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Frame子类自动创建Tk对象
"""
from tkinter import *
ImagePath = "image_directory"


class Application(Frame):
	"""
	"""
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.initWidgets()
		
	def initWidgets(self):
		w = Label(self)
		
		bm = PhotoImage(file=ImagePath+"cat_issc.png")
		
		w.x = bm
		
		w['image'] = bm
		w.pack()
		
		okButton = Button(self, text="确定")
		okButton['background'] = 'yellow'
		# okButton.configure(background=’yellow')
		# okButton = Button(self, text="确定", background='yellow')
		okButton.pack()
		
		
if __name__ == "__main__":
	app = Application()
	print(type(app.master))
	
	app.master.title('窗口标题')
	
	app.mainloop()
	