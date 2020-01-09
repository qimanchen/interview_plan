# shell脚本实现Linux系统监控

# 主要命令介绍
"""
查看内存(free)
查看磁盘(df)
查看cpu占用率(top)
查看内核版本(uname)
"""

"""
$(shell指令) -- 提前执行指令
"""
# 参数说明
"""
$1 -- 表示第一个参数
$2 -- 表示第二个参数
$# -- 表示参数的个数
$@ -- 表示参数列表
$* -- 表示参数字符串 -- 指定字符分割开来的
"""

# 实验步骤
"""
getopts -- 获取用户在命令下的参数

# 使用方法
getopts option_string variable
option_string -- 字符串，会逐个匹配
variable -- 每次匹配成功的选项

getopts 三个参数 ivh
i -- 执行脚本安装
v -- 查看版本
h -- 帮助说明

脚本见 tecmint_monitor.sh

#basename命令会删掉所有的前缀包括最后一个slash（‘/’）字符，然后将字符串显示出来

#scriptname就是tecmint_monitor.sh的地址
"""

