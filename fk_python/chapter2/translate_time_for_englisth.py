# 注意当元组中只有单个元素时，需要在其后面加逗号 ('th',) 
# 这个逗号必不可少，如果没有逗号，那么只是表示一个元素
order_endings = ('st', 'nd', 'rd')\
        + ('th',)*17 + ('st', 'nd', 'rd')\
        + ('th',)*7 + ('st',)

print(order_endings)
day = input("输入日期（1-31）：")
# 将字符串转换成整数
day_int = int(day)
print(day + order_endings[day_int-1])

