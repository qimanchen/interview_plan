# 文件与文件路径管理
	- os.path 路径和文件管理
		import os
		
		- os.path
			- 拆分路径
				path = "/home/lmx/t/access.tar.gz"
				split 返回包含文件路径和文件名的二元组
				dirname 返回文件路径
				basename 返回文件的文件名
				splitext 返回一个除去文件扩展名的部分和扩展名的二元组，只能截取最后一部分
					os.path.splitext(path)
						-> ('/home/lmx/t/access.tar', '.gz')
			- 构建路径
				expanduser 展开用户的HOME目录，如~，~username
				abspath 获取路径或文件的绝对路径
				join 根据不同系统，使用不同的路径分隔符拼接路径
					os.path.join('~','t','a.py')
						-> '~/t/a.py'
				- 检查路径是否为绝对路径
					os.path.isabs('/home/lmx/t/a.py')
						-> True
				- python中可以使用__file__比奥斯当前代码所在的源文件
					path = /home/lmx/t
					os.path.abspath(__file__) -> /home/lmx/t/a.py
					os.path.pardir 符号 ..
			- 获取文件属性
				getatime 获取文件访问时间
				getmtime 获取文件修改时间
				getctime 获取文件创建时间
				getsize 获取文件大小, 如果path参数为目录，那么大小为0
			- 判断文件类型
				exists 参数path所指向的路径是否存在
				isfile 参数path所指向的路径存在，且为一个文件
				isdir 参数path所指向的路径存在，且为一个文件夹
				islinke 参数path所指向的路径存在，且为一个链接
				ismount 参数path所指向的路径存在，且为一个挂载点
				1. 获取当前用户home目录下所有的文件列表
					[item for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)]
				2. 获取当前用户home目录下所有的目录列表
					[item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)]
				3. 获取当前home目录下所有目录的目录名到绝对路径之间的字典
					{item: os.path.realpath(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)}
				4. 获取home目录下所有文件大小
					{item: os.path.getsize(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(item)}
	- 使用os管理文件和目录
		import os
		- 获取当前所在目录
			os.getcwd()
		- 列出当前目录下所有的文件和文件夹
			os.listdir('.')
		
	- tips
		os.path 模块的join函数可以拼接目录
		os.sep表示不同平台的路分隔符
		