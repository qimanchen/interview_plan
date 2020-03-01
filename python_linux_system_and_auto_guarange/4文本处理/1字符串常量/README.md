4.1 字符串常量
4.1.1 定义字符串
	- python 不区分字符和字符串，在python中，所有的字符都是字符串
	- python 使用单引号或双引号来定义字符串
	- 通过嵌套引号来完成字符串中存在引号的问题
	- 同样可以使用转义字符来实现引号嵌套
	
	- 可以使用原始字符串(r)来抑制字符串中的转义
	- 多行字符串，三个单引号或双引号
	
	# python中，两个相连的字符串会自动组成一个新的字符串
		# s = "chen " "qiman" -> "chen qiman"
4.1.2 字符串 - 不可变的有序集合
	- python的字符串是不可变的，无法直接修改
	- 访问方式：下标访问，切片访问
	- python字符串的两大特点：不可变和字符的有序集合
	- 修改字符串：字符运算，切片，格式化表达，字符串方法调用，赋值
	- 每次字符串操作，都会产生一个新的字符串，将占用一块独立内存
	- 实际编程中需要注意不要存在太多字符串的中间结果
	- python下标访问
		H e l l o  w o r l d
		0 1 2 ...       -1 -2
	- 下标操作每次访问一个元素，而切片范文范围
	- 代码可读性，尽量不要同时指定切片操作的起点，终点和步长
4.1.2 字符串函数
	- 通用操作
		len(str) 字符串的长度
		in 是否包含
	- 特定操作
		- 与大小相关的方法
			upper
			lower
			isupper
			islower
			swapcase
			capitalize
			istitle
		- 判断方法
			isalpha
			isalnum
			isspace
			isdecimal
		- 字符串方法
			startswith
			endswith 判断参数是否为字符串的后缀
		- 查找
			find 查找子串出现位置， -1 查找失败
				find(sub [,start [,end]) -> int
			index 查找失败 ValueError
			rfind 从后查找
			rindex 从后向前查找
		- 字符串操作方法
			join 连接字符串列表
				" ".join(['a','b','c'])
				join内接收的参数为任意可迭代对象
				print可以指定分割符,sep参数
			split 将一个字符串拆分成字符串列表
				默认以空白符为分隔符
			strip,rstrip,lstrip 对字符串进行裁剪
				传递的参数是字符的集合
			replace 替换
				"hello, world".replace('ll','oo')
				heooo, world
字符串格式化
	- %表达式
		
	- format函数
		{} 位置，关键字
		"{:_^10.2f}".format(3.1415926}
		____3.14____
			