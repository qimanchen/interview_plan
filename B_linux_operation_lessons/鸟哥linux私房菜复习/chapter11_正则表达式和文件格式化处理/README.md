# 第十一章 正则表达式和格式化处理
	- 正则表达式 Regular Expression
		通过一些特殊字符的排列，用来实现对一列或多列文字字符串进行 查找/替换/删除
		
# 内容
	1. 什么是正则表达式
		- 以行为单位进行字符串的处理
		- 查询/删除/替换
		- 这是一种表示方法，只要工具支持这种表示方法，那么就可以使用
		- vi，grep， awk， sed
	2. 基础正则
		- 系统中语言对正则的影响
			不同的语言格式的英文字母的排序不一样
				LANG=C	0 1...A B C D...Z a b c ...
				LANG=zh_TW	0 1...a A... z Z
			- 几种特殊符号
				[:alnum:]	0-9,A-Z,a-z
				[:alpha:]	A-Z,a-z
				[:blank:]	space,tab
				[:digit:]	0-9
				[:graph:]	除空白字符的其他字符
				[:lower:]	a-z
				[:upper:]	A-Z
				[:xdigit:]	十六进制，0-9，A-F，a-f
		- grep的一些进阶用法
			grep [-n] [-A] [-B] [--color=auto] '查找字符串' filename
				-A 后面指定行数也列出来
				-B 前面指定行数也列出来
				-n 列出行数
				以行为单位进行处理
		- 基础正则练习
			- 练习文件为 regular_express.txt
			- 查找指定字符串
				grep -n 'the' regular_express.txt
				grep -vn 'the' regular_express.txt 反选（没有the的）
				grep -in 'the' regular_express.txt 忽略大小写
			- 利用中括号[]来查找集合字符
				grep -n 't[ae]st' regular_express.txt
				grep -n '[^[:lower:]]oo' regular_express.txt 使用特殊符号
					[^]反向选择
			- 行首和行尾字符^$
				grep -n '^the' regular_express.txt the开头的一行
				grep -n '\.$' regular_express.txt
					. 需要转义
				grep -n '^$' regular_express.txt 找出空白行
				- 显示特殊换行符
					cat -An filename
				grep -Ev '^$|^#' /etc/rsyslog.con 排除空行和注释
			- 任意一个字符.和重复字符*
				.	一定有一个任意字符
				*	重复前一个字符，0到无限次
				grep -n 'g..d' regular_express.txt
			- 限定连续字符次数
				{}	"\{2,3\} 只用使用反斜线才生效
		- 基础正则字符
			^
			$
			.
			\
			*
			[]
			[n1-n2]
			[^list]
			\{n,m\}
			
		- sed工具
			sed [-nefr] [action]
				-n 只显示找到内容的行
				-e 直接在指令模式上进行sed动作编辑，用来接多个动作
				-f 后面跟执行脚本（sed动作集）
				-r 使用扩展正则
				-i 直接修改文件内容
					sed -i 's/\.$/\!/g' regular_express.txt
				action: [n1,[,n2]]function
					- sed后面的动作必须使用两个单引号括起来
					a string	新增，在当前行的下一行
						nl /etc/passwd | sed '2a drink tea'
						nl /etc/passwd | sed '2a Drink tea or ...\
											drink beer?' 增加多行
					c string	替换整行，将制定内容替换
						nl /etc/passwd | sed '2,5c No 2-5number'
						- 列出 11-20行
							head -n 20 | tail -n 10
					d			删除
						sed '2,5d' /etc/passwd
						nl /etc/passwd | sed '2,5d' 列出行号
					i			插入，当前行的上一行
						nl /etc/passwd | sed '2i drink tea'
					p			打印 sed -n
						nl /etc/passwd | sed -n '5,7p'
					s			替换 1,20s/old/new/g
						sed 's/要被替换的字符串/新字符串/g'
						- 找出ip
						ifconfig eth0|grep 'inet '|sed 's/.*inet//g'|sed 's/ netmask.*//g'
						- 排除空行和注释
							grep -Ev '^#|^$' /etc/man_db.conf
					cat /etc/passwd | sed -e '4d' -e '6c no six line' > passwd.new
						sed连续两个动作，删除第四行并且第六行使用'no six line' 替换
	3. 扩展正则
		egrep -v '^$|^#' regular_express.txt
		+ 重复一个或一个以上的前一个re字符
		? 0个或一个前一个re字符
		| or
		() 分组
			分组利用
			echo 123455 --> 装换为<12>34<56>进行显示
				echo 123456 | sed -r "s#(..)(..)(..)#<\1>\2<\3>#g"
			
	4. 文件格式化与相关处理
		- 格式化打印输出 printf
			- printf.txt
			printf '输出格式' 实际内容
			ps: printf后面跟着实际的内容而不是文件
				options
					\a bell
					\b 倒退键
					\f 清除屏幕
					\n 换行
					\r Enter
					\t 水平tab
					\v 垂直tab
					\xNN 转换数字为字符
				格式
					%ns n-数字，s-字符串 多少字符
						printf '%s\t%s\t%s\t%s\t%s\n' $(cat printf.txt )
					%ni i 整数
					%N.nf f-浮点数，N-总的位数，n小数点后的位数
						printf '%5s\t%5i\t%5i\t%5i\t%4.2f \n' $(cat printf.txt | grep -v 'Name')
						printf '\x45\n'
							[root@qiman chapter11]# printf '\x45\n'
							E
		- awk
			awk 一行分成多栏处理
			awk '条件1{action1}条件2{action2}...' filename
				- 预设没栏位的分割符为空白符或tab
				last -n 5|awk '{print $1 "\t" $3}' 过滤出用户和登录ip
				- 每一栏的名称 $1 $2 ..
				- $0 一整行资料
				- awk处理流程
					1. 读入一行，并将第一行的内容填入到$0..中
					2. 根据条件的限制，判断是否需要进行后面的动作
					3. 执行完所有的动作
					4. 若后序仍然还有行，重复1到3行
				NF 每一行有多少栏
				NR 目前第几行
				FS 当前分割符
			- awk使用单引号括起来，由于printf要求使用双引号括起来
				last -n 5|awk '{print $1 "\t" NR "\t" NF}'
			- awk的逻辑运算符
				>	大于
				<	小于
				>=
				<=
				==
				!=
				变量设置时，直接var=value
				- 输出用户
					awk -F':' '$3<10{print $3}' /etc/passwd
			- awk的几点说明
				所有awk动作，在{}执行，当有多个指令时使用;分割，或使用[Enter]进行分割
				逻辑等，必须用 ==
				格式化输出时printf时必须使用\n 换行处理
				cat pay.txt | awk 'NR==1{printf "%10s %10s %10s %10s %10s\n",$1,$2,$3,$4,"Total" } NR>=2{total = $2 + $3 + $4;printf "%10s %10d %10d %10d %10.2f\n", $1, $2, $3, $4, total}'
				awk可以利用if判断
		- 文件比对工具
			- diff
				- 以行为单位， 同一单位不同版本
				diff [-bBi] from-file to-file
					from-file 原始文件
					to-file 要比较文件
						可以使用 - 代替 Standard input
					-b 忽略一行中，多个空白符看成一个空白符
					-B 忽略空白行差异
					-i 忽略大小写
			- cmp
				以字符单位进行比对
			- patch
				需要单独安装
				将旧的文件升级成新的文件
				1. 比较文件，并将差异文件制作成补丁
					diff -Naur passwd.old passwd.new > passwd.patch
				2. patch -pN < patch_file 更新
					patch -R -pN < patch_file 还原
						-p 取消基层目录
							根据建立patch文件所在目录进行目录的删减
						-R 还原
			- pr 文件打印准备
				pr filename 文件时间，文件名，页码
				
	5. 内容总结
# 实例
	- ls -l 找出/etc下所有的链接文档
		ls -l /etc/ | grep '^l' | wc -l
# 习题
	- 提取指定网卡的ip
		1. ifconfig eth0 | grep 'inet' | sed 's/^.*inet//g' | sed 's/*netmask.*$//g' 提取出ip
		2. 别名设置
			alias myip_eth0="ifconfig eth0 | grep 'inet' | sed 's/^.*inet//g' | sed 's/*netmask.*$//g' 提取出ip"
		3. 定义变量
			MYIP_ETH0=$(myip_eth0)
		4. 将其写入到配置文件中