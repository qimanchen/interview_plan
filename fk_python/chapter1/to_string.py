# python 不允许直接拼接数值和字符串
# 可以通过str()和repr()函数将数值转换成字符串
s1 = "这本书的价格是："
p = 99.8
# 使用str()将数值转换成字符串
print(s1 + str(p))
# 使用repr()将数值转换成字符串
print(s1 + repr(p))

# str -- python内置的类型
# repr -- 只是一个函数
# repr -- 还可以实现python表达式的形式表示值
st = "I will play my fife"
print(st)
print(repr(st))
