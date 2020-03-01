# 课程回顾
	1）sed流编辑命令
	2）语法结构 sed [option] [action] filename
	3）sed命令实际应用
		查 参数 -n 指令p
		增 参数 -i 指令 i，a
		删 参数 -i 指令 d
		替换 参数-i.bak(增加备份文件）  指令 s g c 后项引用前项 &
		
# 课程介绍
	1）awk 擅长对列进行操作/进行数据信息的统计（数组）
	2）awk 基本使用（高级使用-shell）
	01. awk概述
		gawk 模式扫描和处理文件语言
		- 作用
			1. 排除
			2. 查询
			3. 统计
			4. 替换
		awk语法格式：
			awk [options] [action] filename
				- action
					[条件-动作]
		awk处理过程
			0. 先处理BEGIN
			1. 先读取一行，判断模式是否符合
			2. 符合，进行动作
			3. 不符合，直接进行下一行
			4. 最后处理END
		- 测试数据
			Zhang	Dandan		41117397	:250:100:175
			Zhang	Xiaoyu		390320151	:155:90:201
			Meng	Feixue		80042789	:250:60:50
			Wu		Waiwai		70271111	:250:80:75
			Liu		Bingbing	41117483	:250:100:175
			Wang	Xiaoai		3515064655	:50:95:135
			Zi		Gege		1986787350	:250:168:200
			Li		Youjiu		918391635	:175:75:300
			Lao		Nanhai		918391635	:250:100:175
		- 命令的查询信息方法
			按照行号查询信息
				awk 'NR==2' test_awk.txt	单行
				awk 'NR==2,NR==4' test_awk.txt	多行连续
				awk 'NR==2;NR==4' test_awk.txt	多行不连续
			ps: 在linux系统中
				oldboy=10	赋值
				oldboy==10	等于验证
			按照字符查询信息
				awk '/Xiaoyu/' test_awk.txt	单行
					这个是整行里面匹配
				awk '/Xiaoyu/,/Waiwai/' test_awk.txt
				awk '/Xiaoyu/;/Waiwai/' test_awk.txt
		- 测试
			1. 显示姓氏和id
				awk '/Xiaoyu/{print $1 "\t" $3}' test_awk.txt 
				awk '/Xiaoyu/{print $1,$3}' test_awk.txt  使用逗号分隔显示出来表示空格分隔
			2. 姓氏是zhang的人，显示他的第二次捐款金额及他的名字
				awk '/Zhang/{print $4}' test_awk.txt
				awk '/Zhang/{print $NF}' test_awk.txt | awk -F':' '{print S3}'
					-F 指定分割符
					两个处理组合
						awk -F "[:\t]+" '/Zhang/{print $1,$5}' test_awk.txt 显示第一列和第二次
							- 以多个分割符分割[:\t]+
							- 从后面数$(NF-1)
				- awk中运算$(NF-1)
				$NF -- 倒数第一列
			3. 显示所有以41开头的姓名和Id
				awk '$3~"^41.*"{print $1,$2,$3}' test_awk.txt
					~表示匹配正则
			4. 显示所有Id号码最后一位数字是1或者5的人的全名
				awk '$3~"[15]$"{print $1,$2}' test_awk.txt|column -t
					- column -t 显示格式设置
				awk '$3~"/1$|5$/"{print $1,$2}' test_awk.txt|column -t
			5. 显示xiaoyu的捐款，每个数值前面加$符号
				awk '$2~/Xiaoyu/{print $NF}' test_awk.txt
					- awk中替换 gsub
						gsub(/需要替换的信息/,"修改成什么信息",将那一列进行修改)
				awk '$2~/Xiaoyu/{gsub(/:/,"$",$NF);print $NF}' test_awk.txt
					- 连续多个动作进行使用分号";"分割
		- 文件中空行进行排除/文件中注释信息进行排除
			grep -Ev "^#|^$" filename
			sed -n '/^#|^$/!p' filename
			sed '/^#|^$/d' filename
			awk '!/^#|^$/' test_awk.txt
			awk '$0!~/^#|^$/' test_awk.txt
		- awk取ip地址
			ip a s eth0|awk -F "[ /]+" '$2=="inet"{print $3}
		总结awk命令中$符号用法
			$1,$2,$3：取第几列
			$NF	倒数第一列
			$0	一整行
			$(NF-n)	倒数第几列
	02. awk高级功能
		a 对日志信息进行统计（计数）
		b 对日志信息进行数值进行求和 客户端-下载 服务端-上传 消耗网络流量
		c （数组）进行排序分析
		d 进行脚本编写（循环语句 判断语句）sh awk_nginx.log
		- awk模式概念说明：匹配的条件信息
			- 普通的模式
				01. 正则表达式为模式
					awk '/^oldboy/{print xx}'
				02. 比较匹配信息
					NR==2
					NR>=2
				03. 范围模式
					NR==2,NR==10 2~10的范围
			- 特殊的模式
				BEGIN{} 在awk命令执行之前所执行的动作
					awk 'BEGIN{print "firstname","lastname","qq","money record"}{print $0}' test_awk.txt
					作用：
						- 测试
						- 计算
							BEGIN{print 100-3}
							BEGIN{print 100/3}
						- 修改内置变量
							FS
							'BEGIN{FS=":"}'
							'BEGIN{FS="[ :]+"}'
							NR
							NF
						- awk调取变量，变量初始化
							awk -vFS=":" '{print $2}' test_awk.txt
							awk调取变量，不用增加$符号
							awk -vvar1="test" '{print var1}' test_awk.txt
				END{} 在awk结束后执行的动作
					awk 'END{print "all actions is over!"}{print $0}' test_awk.txt
			echo $(()) 做运算
			- 统计空行
				grep -c ..
				echo $((i=i+1))
			- 测试 - 统计累加
				01. 统计/etc/services中的空行
					awk '/^$/{i=i+1;print i}' /etc/services
					awk '/^$/{i=i+1}END{print i}' /etc/services awk统计空行
				02. 统计/etc/services中以#开头的
					awk '/^#/{i=i+1}END{print i}' /etc/services
					awk '/^#/{i=i++}END{print i}' /etc/services
				03. 统计系统中有多少个虚拟用户 普通用户
					a 用户信息保存文件 /etc/passwd
					b 从文件中匹配出虚拟用户和普通用户
						awk '$NF~/bash/' /etc/passwd
						awk '$NF~/\/bin\/bash/' /etc/passwd
					c 进行统计
						awk '$NF~/\/bin\/bash/{i++}END{print i}' /etc/passwd 统计普通用户
							- 当斜线符号冲突时，要使用转义符号进行转义
						awk '$NF!~/\/bin\/bash/{i++}END{print i}' /etc/passwd 统计虚拟用户
				- yum install -y lrzsz (windows - linux) linux软件包
					rz -y 传输文件
				- awk 统计secure登录信息文件
					awk '/Failed password/{i++}END{print i}' filename.log
			- 测试-统计累加
				sum=sum+$n	n有需要进行数值求和的列
				seq 1000|awk '{sum=sum+$1}END{print sum}'
					
# 课程练习
	- 求除测试文件中所有人第一捐款和第三次捐款总额
		test_awk.txt
	显示表头，第一总额，第三次总额
		# 找出要统计的对象
		awk -F'[:\t ]+' '{print $4,$6}' test_awk.txt
		# 输出表头
		awk -F'[:\t ]+' 'BEGIN{print "first\t\t","third"}{print $4 "\t\t" $6}' test_awk.txt
		# 统计求和
		awk -F'[:\t ]+' 'BEGIN{print "first\t\t","third"}{sum1=sum1+$4;sum2=sum2+$6}END{print sum1 "\t\t" sum2}' test_awk.txt
			ps：awk中的变量不要用双引号括起来，用双引号括起来的不是变量了
# 课程拓展
	awk同时满足多个条件
		awk '!/Accepted.*192.168.90.1|Disconnected.*192.168.90.1|error.*192.168.90.1/	&&/192.168.90.1/' /var/log/secure-20200221
			条件一																			条件二
		ps：其中一个"|"表示是正则表达式的或
		而awk中表示条件一或二 --- options1 || options2
	- sed，awk，grep同时匹配两个条件
		sed -n '/ABC/{/123/p}‘
		awk 'ABC/&&/123/’
		grep -E '(ABC.*123|123.*ABC)'
	- sed，awk，grep同时匹配两个条件其中任何之一
		sed -rn '/ABC|123/p'
		awk 'ABC/||/123/'
		grep -E '(ABC|123)'