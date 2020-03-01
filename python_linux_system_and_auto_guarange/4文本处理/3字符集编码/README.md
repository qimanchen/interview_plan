# 字符集编码
- 编码历史
	ASCII编码
		0 - 48
		A - 65
		a - 97
		128字符只占用字节的7位
		最前面一位统一规定为0
		使用一个字节来存储一个字符
	latin-1
		127以上的字符代码分配给了重音和其他特殊字符
	Unicode
		unicode编码通常记为U+xxxx
		python中Unicode记做\uxxxx - 十六进制
- UTF-8编码
	Unicode转换格式
	UTF-8和UTF-16可变长度编码
	可能需要1到6个字节
	- Unicode是表现形式
	- UTF-8是存储形式
	- UTF-8编码规则
		1. 对单字节符号，字节第一位设为0，后面7位为这个符号的unicode码
			对于英文字母，UTF-8编码和ASCII码是相同的
		2. 对于x字节的符号，第一个字节的前x位都设为1，第x+1位设为0，
			后面的字节的前两位一律设为10，其他位为unicode码
	第一个编码范围\uD800 ~ \uDBFF，编码的高代理项
	\uDC00 ~ \uDFFF 低代理项
	code = 0x1000 + (H - 0xD800) * 0x400 + (L - 0xDC00)
	使用进位思想，进位后使用两个编码表示一个unicode编码
	
	- 未指定定义字符串的编码时，默认是ASCII编码
- Python2和Python3中的Unicode
	Python3
		- 存在两种字符序列的类型，bytes和str
		- bytes实例包含原始的8位值
		- str实例包含Unicode字符
	python2
		- str和Unicode
		- str实例包含原始的8位值
		- Unicode实例包含Unicode字符
		
		在python2中默认使用Unicode字符串的方法
			from __future__ import unicode_literals
	- encode 编码
	- decode 解码
	
	如果写入的字符串比较多，那么每次都需要进行编码
	python2中使用codecs模块
		import codecs
		with codecs.open('/tmp/data.txt', 'w', encoding='utf-8') as f
	python3中内置的open函数就支持指定编码转换
		with open('/tmp/data.txt', 'w', encoding='utf-8') as f
	
	程序编码和解码操作放在程序的最外围来处理，程序的核心部分使用unicode
	