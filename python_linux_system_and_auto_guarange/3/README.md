# 打造命令行工具

#3.1 与命令行相关的Python语言特性
	
	# 使用sys.argv获取命令行参数
		argv 列表中的第一个元素为执行程序的名称
		
	# 使用sys.stdin和fileinput读取标准输入
		sys.stdin # 标准输入，一行一行读取
		sys.stdin.readlines # 一次读取全部文件并每行为一个数据
		
		fileinput 遍历sys.argv[1:]，实现多个文件的读取 read_from_fileinput.py
		
	# 使用SystemExit异常打印错误信息
		使用sys.stdout,sys.stderr输出内容 test_stdout_stderr.py
		使用sys.exit()返回程序运行结果错误码
		
	# 使用getpass库读取密码
		getuser和getpass函数，分别获取用户名和用户密码
		getpass函数相较于input函数，它不会显示的显示密码
		
# 3.2 使用ConfigParse解析配置文件
	配置文件 -- 配置好后，不用每次都指定相应的参数
	ini格式的文件 -- 编程语言无关，可读性强，易于处理
	
	# 一个配置文件包含一个到多个章节(section)
		# MySql
		...
		[client]
		port = 3306
		user = mysql
		password = mysql
		host = 127.0.0.1
		
		[mysqld]
		basedir = /usr
		datadir = /var/lib/mysql
		tmpdir = /tmp
		skip-external-locking
		
	# 使用ConfigParse解析配置文件过程
		# 在python3没有此模块 --- 切换成了其他模块？？
		a. 创建一个ConfigParse对象
			allow_no_value -- 默认值为False 选项是否可以没有值
			$ cf = ConfigParser.ConfigParser(allow_no_value=True)
			$ cf.read('my.cnf') # 返回文件名
			
		b. 操作
			cf.sections() # 返回配置文件中所有的section
			cf.has_section('client') # 是否有section client
			cf.options('client') # client中所有参数
			cf.has_option('client', 'user') # client中是否有user option
			cf.get('client', 'host') # client中的'host', 若没有则会报错
			cf.getint('client', 'port') # 获取 int的option值
			getboolean() bool
			getfloat()
		c. 修改配置文件
			remove_section # 删除一个section
			cf.add_section('mysql')
			>>> cf.set('mysql','host', '127.0.0.1')
			>>> cf.set('mysql', 'port', 3306)
			add_section # 添加一个section
			remote_option # 删除一个选项
			set # 添加一个选项
			write # 将ConfigParser对象中的数据保存到文件中
			>>> cf.write(open('my_copy.cnf', 'w'))
		
3.3 使用argparse解析命令行参数
	
	# ArgumentParser解析器
		argparse.ArgumentParser()
		description -- 初始化参数
	
	# 使用argparse解析参数，会自动生成帮助信息
		python *.py --help
		
3.4 使用logging记录日志
	# 诊断日志和审计日志
	logging模块
		debug,info,warn,error,critical
		10调试
		20 显示程序正常运行时的一些数据
		30 可以容忍，但需要改进
		40 严重错误，马上处理
		50 软件已经无法运行
		# 只有日志级别大于等于warning的才会被显示
	
	# 日志分级便于日志分析，提高性能
	# 针对日志可以配置日志格式
	
	# logging中模块的配置
		Logger -- 日志记录器，应用程序中能直接使用的接口
		Handler -- 日志处理器，以表明将日志保存到什么地方以及保存多久
		Formatter -- 格式化，用以配置日志的输出格式
		
		# 简单的脚本使用basicConfig进行配置
		# 复杂使用一个配置文件，并使用fileConfig函数读取配置文件
		配置文件加logging.cnf
	
3.5 与命令行相关的开源项目
	
	# 使用click解析命令行参数
		http://click.pocoo.org/5/
		$ pip install click
		# 改进argparse的易用性
		a. 使用@click.command()装饰一个函数，使之成为命令行接口
		b. 使用@click.option()装饰函数，为其添加命令行选项
		click_test.py
		# 当一条命令输入错误时可以通过fc命令进行修改
		
	# 使用prompt_toolkit实现交互式命令行工具
		