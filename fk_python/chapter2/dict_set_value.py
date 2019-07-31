# 字典的几种赋值方式
# 1. 通过列表+dict实现
vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
dict3 = dict(vegetables)

# 2. 也可以通过dict指定关键字参数来创建字典
# 对应的key不用使用引号括起来
dict6 = dict(spinach=1.39, cabbage=2.59)
#>>> dict6 = {'spinach': 1.39, 'cabbage': 2.59}
