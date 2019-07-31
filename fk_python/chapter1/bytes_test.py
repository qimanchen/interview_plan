# bytes类型里的每个单元都是一个字节
# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes值
b2 = b''
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])

# 调用bytes方法将字符串转换成bytes对象
b4 = bytes('我爱python编程', encoding='utf-8')
print(b4)
# 利用字符串的encode方法编码成bytes，默认使用utf-8字符集
b5 = "学习python很有趣".encode('utf-8')
print(b5)

# bytes类型中每个数据单元都是字节，每四位用一个十六进制数表示
# 每字节用两个十六进制数表示
# 可以使用decode方法将其解码成字符串
st = b5.decode('utf-8')
print(st)
# >>> 学习python很有趣"
