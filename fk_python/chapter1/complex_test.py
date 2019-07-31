# 对复数进行运算 -- 导入cmath模块
ac1 = 3 + 0.2j
print(ac1)
print(type(ac1)) # 输出复数类型
ac2 = 4 - 0.1j
print(ac2)
# 复数运算
print(ac1 + ac2)
#>>> (7 + 0.1j)
# 导入 cmath模块
import cmath
# sqrt()函数，计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)
#>>>1j
