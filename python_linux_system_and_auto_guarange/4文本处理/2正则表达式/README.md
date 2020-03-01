# 正则表达式
同时使用"." 和 ":" re.split('[:.]\s*', data)
- 语法
	正则表达式由普通文本和具有特殊意义的符号组成
		- 要匹配给定文本中所有单词
			?[a-zA-Z]+
		- 匹配一个IP
			[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
- re库使用
	re.findall()
	flags=re.I
	- 直接使用re模块中的函数
	- 创建一个特定模式编译的正则表达式对象
		re.compile()
	编译过后的运算速度更快
- 常用的re方法
	- 匹配
		findall 找到所有匹配的字符串，返回列表
		match 从开头匹配，匹配失败返回None
			匹配成功返回SRE_match类型的对象
			相关模式，原始字符串，模式匹配成功的子串位置和结束位置
			r = re.match(pattern,data)
			r.start()
			r.end()
			r.re
			r.string
			r.group()
		search 从字符串任意位置进行匹配
			仅查找第一次匹配
	- 修改
		sub
			re.sub(pattern, 替换成的子串，待替换字符串)
			re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
		split
	- 大小写不敏感
		re.findall(pattern, text, flags=re.IGNORECASE)
	- 非贪婪模式
		在匹配模式后（非贪婪匹配部分）添加?
		
		