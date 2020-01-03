#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tkinter第一个实例
# 使用步骤
1. 创建Tk对象 -- Tk()
2. 在Tk对象中添加对应的组件
3. 选择对应的布局方案
4. 主窗口渲染
"""
# from Tkinter import * # python2.x
from tkinter import *

# 创建tk对象
root = Tk()

# 设置窗口标题
root.title("Window Title")

# 在窗口对象中添加一个Label对象，并填写相应的内容
# Label 文本标签
w = Label(root, text="Hello Tkinter!")

# 使用pack来实现布局
w.pack()

# 启动主窗口
root.mainloop()