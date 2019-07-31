s = '   this is a puppy   '
# 删除左边的空白
print(s.lstrip())

# 删除右边的空白
print(s.rstrip())

# 删除两边的空白
print(s.strip())

# 再次输出检查s并没有改变
print(s)

# 同样也可以删除字符串前后指定字符的功能
s2 = 'i think it is a scarecrow'
print(s2.lstrip('itow'))
print(s2.rstrip('itow'))
print(s2.strip('itow'))
