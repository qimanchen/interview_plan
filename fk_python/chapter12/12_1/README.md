#pathlib -- PurePath
# PurePath几个实用的属性
	from pathlib import PurePath
	PurePath的本质还是字符串
	 pp = PurePath("...")
	 1. pp.anchor --> 获得windows的盘符或unix的根目录
	 2. pp.parent -- > 获得该文件的父目录（绝对）
	 3. pp.name -- > 获得当前文件（从绝对路径中）
	 4. pp.suffix --> 获得文件最后的文件标示符
	 5. pp.as_uri() -- > 将路径转换成uri -- 转换相对路径会引发异常
	 6. pp.match(规则) -- > 判断路径是否匹配
	 7. pp.with_name(待替换文件) --> 替换文件
	 8. pp.with_suffix(".txt") --> 替换后缀
	 
# Path
	Path会正真的访问底层的文件路径
	from pathlib import Path
	p = path('.')
	1. p.iterdir() --> 访问当前目录下的所有文件，但是不会深入到子目录中
	2. p.glob('**/*.py') --> 获取相应目录下及其子目录下的.py文件
	p.read_bytes/text(encoding=None)
	p.write_bytes/text(data)
	
	
# os.path
	对应的文件名称可以为绝对路径或相对路径
	os.path.abspath("abc.txt") --> 获取文件的绝对路径
	os.path.dirname("abc/xyz/README.txt") --> 获取文件的目录
	os.path.exists("abc/xyz/README.txt") --> 确认文件是否存在
	getatime(filename) --> 文件最后一次访问时间
	getmtime(filename) --> 文件最后一次修改时间
	getctime(filename) --> 文件创建时间
	isfile()
	isdir()
	samefile()
	

# fnmatch
	import fnmatch
	fnmatch.fnmatch(filename, pattern) # --> 找出匹配的文件
	fnmatch.filter(names, pattern) --> 找出对应文件队列中的符合条件的文件
	
# 打开文件
	file = open(filename [, access_mode] [, buffering])
	file.close() --> 关闭文件
	file.closed --> 文件是否关闭
	file.mode --> 文件的访问模式
	file.name --> 文件的名称
	文件打开模式：
		r -- 只读，不能打开不存在的文件
		w -- 写，打开文件会直接擦除原有内容
		a -- 追加
		+ -- 读写 r+,w+
		b -- 二进制 rb rb+ ab
	open的第三个参数 -- 0|1 -- 不缓存|缓存
	
	
# 读取文件
	f = open("test.txt", 'r', True)
	read([num]--字节|字符数) -- 不使用b模式，每次读取一个字符，反之每次读取一个字节
	windows平台默认GBK字符集
	
	# 当要打开的文件的字符集与当前操作系统的字符集不符
		1. 使用二进制打开，然后使用bytes的decode()方法恢复成字符串
			f = open("test.txt", 'rb', True)
			f.read().decode('utf-8')
		2. 利用codecs模块的open()函数打开文件，并在打开文件时允许指定的字符集
			# UnicodeDecodeError
			import codecs
			f = codecs.open('read_test.py', 'r', 'utf-8', buffering=True)
			
			
	# 按行读取文件
		readline([n]) --> 读取一行内容，或n个字符
		readlines() --> 读取文件中所有的行，并以列表的形式返回
		
		
# 使用fileinput读取多个输入流
	# 打开文件时不能指定字符集
	fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
	fileinput.filename() --> 返回正在读取的文件的文件名
	fileinput.fileno() --> 返回当前文件的文件描述符
	fileinput.lineno() --> 当前读取文件的行号
	fileinput.filelineno() --> 在文件中的行号
	
	fileinput.nextfile() --> 关闭当前文件
	fileinput.close() --> 关闭fileinput对象
		
		
# 文件迭代器
	import codecs
	f = codecs.open("test.txt", 'r', 'utf-8', buffering=True)
	for line in f:
		print(line, end='')
	f.close()
	# 文件本身可以迭代
	sys.stdin 也是一个迭代对象，类似open一个文件
	
	
# 管道输入
	cmd1 | cmd2 | cmd3 ...
	type ad.txt | python pipein_test.py
	
	
# 使用with语句
	自动关闭文件
	with context_expression [as targes(s)]:
		with 代码块
	
	context_manager.__enter__() --> 代码执行前自动执行
	context_manager.__exit__() --> 异常或不异常
	as 语句后面可以有多个变量，但必须用括号括起来
	
	
# 使用linecache随机读取指定行
	linecache.getline(filename, lineno) --> 读取指定文件的指定行
	

# 写文件
	文件对象操作文件指针
		seek(offset [, whence]) --> 将文件移动到指定位置，whence为0从文件开头算起，whence为1当前位置算起，为2结尾算起
		tell() --> 判断文件指针的位置
		

# 输出内容
	write(str or bytes)
	writelines(可迭代对象) --> 输入多个字符串或字节符
	os.linesep --> 当前操作系统上的换行符
	若为字节符 -- 必须使用encode()编码
	
	
# os模块的文件与目录函数
	os.getcwd() --> 获取当前目录
	os.chdir(path) --> 改变当前目录
	os.fchdir(fd) --> 通过文件描述符改变当前目录
	os.listdir(path) --> 返回path对应目录下的所有文件和子目录
	os.mkdir(path [,mode]) --> 创建path对应的目录
	os.mkdirs(path [,mode]) --> 创建目录，可递归创建
	os.rmdir(path),os.removedirs(path) --> 删除目录
	os.rename(src,dst) --> 重命名文件或目录
	os.renames(old, new) --> 递归命名，--对应('abc/xyz/wawa', 'foo/bar/haha')
	
	# 权限相关的函数
		os.access(path, mode) --> 是否具有指定权限，mode -- os.F_OK,os.R_OK,os.W_OK,os.X_OK
		os.chmod(path,mode) --> 修改权限
		os.chown(path, uid, gid) --> 修改文件所有者
		os.fchmod(fd, mode) 
		os.fchown(fd, uid, gid)
		
	# 与文件访问相关的函数
		os.open(file, flags[,mode])
		os.read(fd, n)
		os.write(fd, str)
		os.close(fd)
		os.lseek(fd, pos, how)
		os.remove(path) --> 删除path对应的文件
		os.link(src, dst) --> 建立硬连接
		os.symline(src, dst) --> 软连接
		

# tempfile模块生成临时文件或目录
	