# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数说明
# 要输出的对象(value); 多个输出参数的分隔符(seq)  -- 默认是空格;
user_name = "陈起慢"
user_age = "24"
print("****默认输出****")
print("读者名: ", user_name, "年龄: ", user_age)
#>>> 读者名:  陈起慢 年龄:  24
print("****修改分隔符****")
print("读者名: ", user_name, "年龄: ", user_age, sep="|")
#>>>读者名: |陈起慢|年龄: |24

# 默认输出结尾操作符(end) -- 默认换行符('\n')
print("****默认****")
for i in [40, 50, 60]:
    print(i, '\t')
"""
40
50
60
"""
print("****修改****")
for i in [40, 50, 60]:
    print(i, '\t', end="")
#>>>40    50    60

with open('print_out_file.txt', 'w') as f:
    # 建立输出的文件
    print('沧海月明珠有泪,', file=f)
    print('蓝田日暖玉生烟,', file=f)

# flush控制输出缓存 -- 默认为False

