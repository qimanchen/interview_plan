#操作系统文件属性
# 自己课程回顾
	1. centos7修改网卡名称
	2. 第三阶段回顾
		- 目录和文件创建命令
		- vi/vim使用技巧
			- vim 常见错误说明
				a vim后面必须跟文件
				b vim只能编辑存在目录的文件
				c 编辑文件突然非正常退出
		- vim的编辑原理，实际编辑的swap文件
		- vim 问题解决
		- 查看文件信息
			- ls
				ls -ltr 根据文件时间进行排序（倒叙）
		- 查看文件内容
			- cat
			- less/more
			- head/tail
		- 直接编辑文件的方法
			- echo {}序列符号
			- cat>> test.txt <<EOF
	3. 过滤文件内容
		三剑客
			- grep
				-A
				-B
				-C
				-c
				
			- sed
				sed -n "/oldboy/p" test.txt
			- awk
	4. 修改文件部分内容
		1. sed -- 真正修改文件内容
			sed -i "s/old/new/g" test.txt
			- 修改前注意备份
		2. tr
# 视频中课程回顾
	1. vim常见的错误
	2. vim的执行原理（理解描述 学着画图）
	3. 查看文本信息命令 cat less/more head tail
	4. 直接编辑文件信息 echo(单行) cat(编写多行） {}序列号符号
	5. 进行筛选过滤信息 grep sed awk
	6. 进行信息内容替换 sed tr
		- tr "a-z" "A-Z"
	- 问题解析
		tail -f 追踪文件信息时：文件被删除或移走，需要进行重新追踪
		tail -F 追踪文件信息时：文件被删除或移走，不需要进行重新追踪，只要文件恢复回来会继续追踪
			- 日志文件，文件数据会不断增加，历史悠久的日志文件会清空
	- tr命令替换信息原理
		tr str1(要替换) str2(替换成) 
		str1用于查询，str2用于转换，tr执行时，str1中的字符被映射到str2中的字符，然后开始转换
		- 替换信息情况，tr命令替换信息是一对一
		- 可能出现的情况
			- str1/str2 abcd/123
				超出的部分使用，最后的一个字符替换 abcd - 1233
			- abc/1234
				超出的部分忽略 abc - 123
			- abc/123
				abc - 123
			- 极特殊情况
				后面的映射会覆盖前面的映射
				abcba/12345
				abcba - 54345
# 课程知识
	1. 第四阶段回顾 - 目录结构知识
		- 常见的目录结构
		- 目录结构特点
		- 目录挂载
		- 目录结构发展
		- 目录结构初识别
		dns的配置，网卡的配置优先级比较高
		/etc/rc.local 一定是可执行的命令，并且/etc/rc.d/rc.local 一定要有执行权限
		/usr/lib/sysytemd/runlevel
		家目录下的配置文件优先
		- 如何卸载软件
			yum --help -help --h -h
			1. yum卸载
				yum erase -y cowsay --- 及其不建议，会卸载依赖软件
			2. rpm -e 软件名称 --nodeps 不验证包的依赖关系 - 推荐
		可用的内存/buffer+free
	2. 第五阶段回顾 系统优化
		1. 查看系统信息的方法 uname cat /etc/redhat-release
		2. 系统用户信息设置
			创建用户：useradd
			1. 创建多个用户（借助nodapad++)
				一次性写多行
				alt + c 可以生成数据序列
			2. 借助sed，创建多个用户
			3. 利用shell脚本的循环语句
				username="user"
				for x in {01..20}
				do
					useradd oldgirl${x}
					echo "password" | passwd --stdin oldgirl${x}
				done
			- 设置密码信息 passwd username
				1. 交互式设置密码
					passwd username
				2. 免交互
					创建用户的同时，设置密码
					useradd username && echo "password" | passwd --stdin username
					useradd username; echo "password" | passwd --stdin username
		3. 安全
		4. 字符集
	3. 文件属性信息
		什么是软连接和硬链接
		什么是数据存储的inode和block
		文件类型都有哪些
	4. 文件操作系统，文件属性信息
		ls -li /etc/
		total 1092
		第一部分：文件属性										第二部分：文件名称
		33895759 drwxr-xr-x.  3 root root      101 Feb 13 01:12 abrt
		33866548 -rw-r--r--.  1 root root       16 Feb 13 01:15 adjtime
		01		02	03		  04 05  06		    07 08
		01 - 文件数据inode信息：index node == 索引节点
			作用：快速从磁盘中找到数据信息
		02 - 文件数据类型：文件 目录 链接文件 设备文件
			linux系统中一切皆文件
			作用：指明数据的文件类型
		03 - 权限位信息：r -read w-write x-execute
			作用：控制不同用户对文件有不同权限
		04 - 文件目录的硬链接数：类似于超市的多个门
			作用：可以多个路径查看信息
		05 - 文件所属用户信息：
			作用；文件的创建者或拥有者
		06 - 文件所属组信息
			作用：文件或数据的所属用户组
		07 - 文件的大小
		08 - 文件时间信息
	5. 文件属性详细信息 -- 文件类型
		a 文件类型概念
			windows：区分文件的类型 -- 扩展名
			linux：不用扩展名区分文件类型
		b linux系统区分文件类型方法
			- 颜色区分
			- 利用属性信息区分
				ls -l
				利用显示出的信息的第一行
			- 利用特殊的命令
				file test.txt 查看文件属性
		b linux系统中的常见文件类型
			d -- 目录
			- -- 普通文件
				1）纯文本 text /etc/hosts --- 可以直接编辑查看的普通文件
				2）二进制文本 binary /bin/ls --- 命令文件（不可编辑）
				3）数据文件 data /tmp/etc.tar.gz --- 数据文件 压缩文件
			l -- 软链接文件 快捷方式
				ln -s source destination
			c/b -- 块文件/字符文件（设备文件）
				块文件：存储的设备文件 光驱设备文件 磁盘
				字符文件： 根本停不下来的输出字符信息
				磁盘设备文件 /dev/sda 磁盘文件
				随机设备文件 /dev/urandom
				输出设备文件 /dev/zero 黑洞出个文件 磁盘分区
				输入设备文件 /dev/null 黑洞入口文件 定时任务
					echo 123456 2> /dev/null stderr
					echo 123456 &> /dev/null stderr stdout
			s -- socket文件（网络编程）
	6. 拓展命令说明
		- 显示文件信息类型 file
		- 显示命令绝对路径信息 which
		- 显示命令或文件文件信息 whereis ifcfg-eth0
			作用：显示命令以及命令相关帮助手册的路径
		- 快速定位文件路径信息 locate
			locate 文件名称 --- 可以显示文件所在的路径信息
			updatedb 更新文件数据库
			新建的文件，由于没有更新数据库，因此找不到
			PS:默认centos7没有安装locate
				yum provides locate 查找某个命令属于那个安装包
		- 快速查找数据信息命令
			find命令语法
				find 找寻路径范围 -type 类型f/d/l/c/b  -name 文件名称
			问题：一个文件名称没有记全
				find /etc -type f -name "*eth0"
				* 通配符 表示任意个字符
# 课程知识回顾
		1. 阶段三
		2. 阶段四五
		3. 了解文件属性相关信息
		4 详细了解文件类型
			常见的类型有哪些
			拓展的文件相关命令
			find 找寻文件所在路径
			

# 练习
	- 总结find命令
		语法格式：
			find [PATH] [option] [action]
			- option
				1. 时间相关参数
					-mtime n：n天之前的一天内被更改过的文件
					-mtime +n: 列出n天之前（不含n天）
					-mtime -n：列出n天之内（含n天）
					-newer file: file为一个存在的档案，列出比file还要新的文件
							|4	|
								-4 ->
						<-	+4
					|7	|6	|5	|4	|3	|2	|1	|now
				2. 与使用者或群组相关参数
					-uid n: n为数字uid
					-gid n
					-user username
					-group groupname
					-nouser：	在/etc/passwd中找不到用户的文件
					-nogroup：在/etc/group中找不到组的文件
				3. 与文件权限以及名称有关的参数
					-name filename: 查找文件名称为filename的文件
					-size[+-]SIZE：查找比SIZE大（+）或小（-）的文件
						SIZE：c byte,k 1024bytes,
						-size +50k
					-type TYPE 查找文件类型
						f 一般文件
						b,c 装置文件
						d 目录
						l 链接文件
						s socket 
						p FIFO
					-perm mode 查找权限恰好为mode1的文件
						-rwsr-xr-x 4755
					-perm -mode 查找权限必须包括mode的文件
						-rwxr--r--,-perm -0744
					-perm /mode 查找包含任意mode权限文件也会被找到
				4. 额外可进行的动作
					-exec command command为其他指令，接额外的指令来处理查找到的结果
						find /usr/bin /usr/sbin -perm /7000 -exec ls -l {} \;
						{} find找到的内容
						-exec 开启 \;结束
					-print 将结果打印到屏幕上，预设
	- 总结文件属性信息
		
# 拓展练习
	- 如何产生随机字符信息
		利用/dev/urandom产生随机数
		提供永不为空的随机字节数据流
		- /dev/random - 随机性更好
			依赖于系统中断，当中断数不足时会等待，大量随机数，速度更慢
		- /dev/urandom 
			不依赖系统中，数据的随机性不高
		dd if=/dev/random of=random.dat bs=1024b count=1
		
		1. 随机纯数字
			tr参数说明
				-d 删除
				-c 反选，符合set1的部分不处理，不符合的部分才处理
			head /dev/urandom | tr -dc 0-9 | head -c 20
		2. 随机小写字母+数字
			head /dev/urandom | tr -dc a-z0-9 | head -c 20
		3. 随机大小写字母+数字
			head /dev/urandom | tr -dc A-Za-z0-9 | head -c 20