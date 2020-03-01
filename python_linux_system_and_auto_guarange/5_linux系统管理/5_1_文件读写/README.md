# 文件读写
	- python中的文件处理
		- 计算机程序中，每打开一个文件就需要占用一个文件句柄
		- 一个进程拥有的文件句柄数是有限的
		- open函数
			f = open('data.txt') 打开一个文件，默认打开模式为'r'
				- 文件打开模式
					r 只读，如果文件不存在，则会报FileNotFoundError异常
					w 写，如果文件不为空，那么文件会被覆盖，文件不存在，那么会重新创建文件
					a 在文件末尾追加内容
					x 创建一个新的文件，若文件已存在，则抛出FileExistsError
			- 文件对象的方法
				f = open('data.txt', 'x') 创建一个新的文件
				f.write(字符串) 向文件中写入内容
				f.close() 关闭文件
		- 文件句柄泄露问题解决
			1. 使用finally来保证
				try:
					f = open('data.txt')
					print(f.read())
				finally:
					f.close()
				- 此方法不够整洁
			2. 使用上下文管理器
				with open('data.txt') as f:
					print(f.read())
				- ? 如果文件打开全程使用，那么如何操作？如果存在多级文件，那么岂不是代码更繁杂了
		- 常见的文件操作函数
			- 读相关函数
				- read 读取文件所有内容
				- readline 一次读取一行
				- readlines 将文件内容存放到一个列表中，列表中的每个内容对应着文件中的一行
			- 写相关函数
				- write 写字符串到文件中，并返回写入的字符数
				- writelines 写一个字符串列表到文件中
					f.writelines(['string1', 'string2'...])
				- 使用printh函数写入到文件中,指定file参数，file参数是个文件对象
					from __future__ import print_function
					with open('/tmp/data.txt', 'w') as f:
						print(1,2,'hello, world', sep=",", file=f)
		- 使用for循环来迭代访问文件内容
			with open('data.txt') as inf:
				for line in inf:
					print(line.upper())
	- 案例
		将文件中所有单词的首字母变成大写
		- 方案一，字符串拼接，双文件打开
			with open('data.txt') as inf, open('out.txt', 'w') as outf:
				for line in inf:
					outf.write(" ".join([word.capitalize() for word in line.split()]))
					outf.write("\n")
		- 方案二，print函数使用
			with open('data.txt') as inf, open('out.txt', 'w') as outf:
				for line in inf:
					print(*[word.capitalize() for word in line.split()], file=outf)