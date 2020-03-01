# 课程回顾
	1）系统符号
		- 基础系列符号：# $ ! |
		- 引号 '' "" `` 没引号
		- 重定向符号
		- 路径符号 -=$OLDPWD
		- 逻辑符号 && ||
	2) 通配符，用于匹配文件名称信息
		* 模糊匹配信息
		{} 生成序列信息 有序序列，无序序列 组合序列
	3）正则符号
		基础正则 grep sed awk
			grep "^old" test.txt
			sed -n '/^old/p' test.txt
			awk '/^old/' test.txt
		扩展正则
	
# 课程介绍
	01. 系统的正则符号
		- 基础正则符号
			1） 点符号 .
				匹配任意一个字符，且只有一个字符
			2）星符号 *
				匹配任意0个或多个符号
				匹配次数0次或多次
				grep -o 显示匹配字符的过程
			3）点星 .* 任意字符
				grep '^m.*o?' test.txt
				问题：贪婪匹配
					grep "^m.*blog" test.txt 前面多点字符
					grep "^m.*og " test.txt 后面多一点字符
					grep -P "^m.*?o" test.txt 关闭贪婪
			4）\ 转义符号
				将文件中以.结尾的符号
				1. 将有特殊意义的符号，转义成普通信息进行识别
				2. 将没有意义的信息转义为有特殊意义的信息 
					\n 换行符
					\t 制表符
					\r\n windows下的换行
					echo -e "oldboy01\noldboy02" echo执行转义
			5） 括号符号 []
				匹配多个字符信息
				grep "oldb[oe]y" oldboy_test.txt
				
				问题：将以i开头和以m开头的行
					grep "^[Im]" test.txt
				grep "^[a-zA-Z0-9]" /etc/selinux/config 
			6) 排除符号，[^a-z] 表示排除没有a-z都取出来
				[^abc] 
				^[^abc]
		- 扩展正则符号
			grep sed 不能直接识别
			grep -E，egrep
			sed， sed -r
			1） +号符号
				匹配前一个字符1次或多次
				grep -o 列出每次匹配的字符
				grep -Ev "[0-9]+" test.txt
			2） | 竖线符号
				与，用于匹配多个信息
				grep "oldboy|oldgirl" test.txt
			3）小括号()
				a 指定信息进行整体匹配
					grep -E “oldb(o|e)y" test.txt
				b 进行后项引用前项进行匹配 sed命令替换过程
					echo oldboy{01..10} | xargs -n1 | sed -r 's#(.*)#useradd \1#g'|bash批量创建用户
					echo oldboy{01..10} | xargs -n1 | sed -r 's#(.*)#passwd \1#g'|bash批量设置密码
					
					seq -w 10 | sed -r 's#(.*)#useradd oldboy\1;echo 123456|passwd --stdin oldboy\1#g'|bash
					3 设置随机密码
					seq -w 10 | sed -r 's#(.*)#useradd oldboy\1;echo $(openssl rand -base64 6)|tee -a test.txt|passwd --stdin oldboy\1#g'|bash
					- 批量删除用户
						seq -w 10 | sed -r 's#(.*)#userdel -r oldboy\1#g'|bash

						01. 如何创建用户 给用户设置密码
						02. 基础命令echo
						03. sed命令替换
						04. 正则符号
						05. 基础符号
						06. bash内置命令
					将输出信息
						echo 123456 --> 装换为<123456> 进行显示
							echo 123456 | sed -r "s#(.*)#<\1>#g"
						echo 123455 --> 装换为<12><34><56>进行显示
							echo 123456 | sed -r "s#([0-9]{2})([0-9]{2})([0-9]{2})#<\1><\2><\3>#g"
							echo 123456 | sed -r "s#(..)(..)(..)#<\1><\2><\3>#g"
						echo 123455 --> 装换为<12>34<56>进行显示
							echo 123456 | sed -r "s#([0-9]{2})([0-9]{2})([0-9]{2})#<\1>\2<\3>#g"
			4）{}
				可以指定字符连续匹配的次数
					x{n,m} 最少出现n次，最多m次
					x{n} n次
					x[,m} 0-m次
					x{n,} 最少n次
			5）?
				定义匹配前一个字符出现0次或者一次
			补充：想让grep sed 使用扩展正则符号
				grep "o\+" test.txt
				给每个符号使用转义符，可以实现高级功能
# 课程内容
	
# 练习
	- sed/awk 命令如何进行排除过滤
		sed '/^$/d' oldboy/oldboy.txt 使用删除
	- 批量设置密码，并给每个用户设置随机密码信息
		shell
			1）如何生成随机信息
			2）变量设置
			3）循环信息
		3 设置随机密码
			seq -w 10 | sed -r 's#(.*)#useradd oldboy\1;echo $(openssl rand -base64 6)|tee -a test.txt|passwd --stdin oldboy\1#g'|bash
			- 批量删除用户
				seq -w 10 | sed -r 's#(.*)#userdel -r oldboy\1#g'|bash
	- 利用ip address show过滤出ip地址
		ip address show eth0|grep "inet "|sed "s/.*inet //g"|sed "s/brd.*//g"
		ip address show eth0 | egrep "([0-9]+\.?){4}" -o |head -3 | tail -1
		
		sed
			ip address show eth0| sed  -nr "/([0-9]+\.){3}/p"|sed -r "s#.*inet (.*)/24.*#\1#g"
			ip address show eth0| awk "/ ([0-9]+\.){3}[0-9]{1,3}\/24/"|awk 'BEGIN{FS=" +"}{print $2}'
		hostname -i 显示主机的ip
	- stat 提取出权限
# 拓展