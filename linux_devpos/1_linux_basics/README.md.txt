# Linux 简介
	1. Unix操作系统
	2. 基于POSIX和UNIX的多用户、多任务、支持多线程和多CPU
	3. Linux -- 内核加系统调用
	4. 发行版本
		Debian,Gento,Ubuntu,Centos,Kail Linux
	5. 终端模拟器
		gnome-terminal,Konsole,xterm, rxvt,kvt,nxterm,eterm
	6. shell -- 终端指令行
		$ -- 普通用户命令提示符
		# -- root用户命令提示符
	7. ls 命令
		ls -- 显示目录，文件的信息（权限，大小）
		ls [选项] [参数]
		选项说明
			-a -- 显示所有文件
			-l -- 显示完整的文件，目录信息
			-d -- 仅显示目录名
			-k,h,m -- 以相应的单位，显示文件大小
	8. pwd命令
		-- 显示用户当前的工作目录
	9. cd 目录
		-- 目录间切换
		-- . 当前目录
		-- .. 上一层目录
		-- - 上一次的目录
		-- ~ 家目录
		-- 使用的目录，相对或绝对
	10. wget 命令
		wget [参数] [下载网址]
		-- 从网络上下载文件或资源，不指定目录，文件默认下载到当前目录，http,https,ftp,http proxy
	11. cp命令
		-- 复制文件和目录
		cp [选项] [源] [目的目录]
		选项说明
			-a 复制文件时，保留源文档所有属性，创建备份
			-r 复制目录中所有项目
	12. rm 命令
		-- 删除文件或目录
		rm [选项] [文件]
		选项说明:
			-f 强制删除
			-i 删除前提示
			-r 递归删除，删除目录内所有项目
	13. mkdir 命令
		-- 创建指定名称的目录
		-- 创建目录需要对当前目录有写权限
		mkdir [选项] [目录]
		选项说明：
			-p 建立多级目录 -- 当创建多级目录时，自动创建不存在的目录
	14. cat 命令
		-- 用于显示文件内容 $ cat filename
		-- 用于将几个文件合并 $ cat filename1 filename2 >filename
		
		-- 从标准输入读取并显示 $ cat > file << "EOF"
		cat [选项] [文件]
		选项说明:
			-A 显示所有
			-b 对非空输出行号
			-n 从1开始输出所有行数编号
	15. linux开源社区
		- Linux Online
		- Linux.com -- linux使用经验
		- Linuxforums -- linux软件资源
		- Linux公社
		- LinuxCN -- 专注中文linux技术
		- ChinaUnix
		- Linux伊甸园论坛
		
		
Linux 基本操作
	1. Shell概述与分类
		-- 提供用户与内核进行交互操作的接口
		-- shell也是一个命令解释器
	2. shell类别
		- Bourne Again Shell -- bash
		- Bourne Shell -- sh
		- C-Shell -- csh
		- Korn Shell -- ksh
		- Z Shell -- zsh
		-- Ubuntu终端默认bash
		$ cat /etc/shells -- 当前主机支持的shell类型
	3. shell脚本初试
		#!/bin/bash -- 告诉系统这个脚本的指定解释程序
		不指定时，使用$SHELL变量的值
		$ ./test.sh -- 文件必须有执行权限
		$ bash test.sh -- 直接用bash执行
		$ source test.sh -- 直接使用父shell执行当前程序
	4. Tab键
		-- Tab键进行命令，目录文件名补全
	5. 常用组合快捷键
		- Ctrl+c -- 终止当前命令，中断
		- Ctrl+d -- 结束键盘输入或退出终端(exit)
		- Ctrl+s -- 暂停当前程序
		- Ctrl+a -- 光标移动到行首
		- Ctrl+e -- 光标移动到行尾
		- Ctrl+l -- 清屏
		- Ctrl+shift+N -- 新建终端窗口
		- Ctrl+k -- 命令行从前往后删除
		- Ctrl+u -- 命令行从后往前删除
	6. 历史输入命令
		-- 使用上下按键
		$ history [n] -- 显示指定条数的历史指令
	7. Linux命令格式
		$ command [options] [arguments]
		command:
			-- 命令
		options：选项
			-- 长选项，“--”来引导 --help
			-- 短选项，"-" 来引导 -a
		argument: 参数，命令的作用
			[]: 可以省略的内容
			<>: 必须提供
			a|b:二选一或多选一
			...:前面的内容和重复出现多次
	8. 环境变量
		-- 系统级和用户级
		-- 系统级，每个用户都要读取的变量
			/etc/profile -- 用户登入shell的初始化工作
			/etc/bash.bashrc -- 由上一文件调用，具体的工作执行
			/etc/environment -- 系统级别的环境变量，不从shell启动的程序设置环境变量
		-- 用户级别，用户个人的环境变量
			~/.profile -- 用户登录时调用，仅调用一次
			~/.bashrc -- 每次多开启shell都会调用
		-- 临时变量
			-- 只针对当前环境变量
		-- 子程序会继承父进程大多数环境变量
	9. Linux变量种类
		-- 生存周期
			永久的：通过配置文件来实现
			临时的：export命令声明，关闭shell时失效
		-- 环境变量自身的信息
			shell进程中定义的
			shell自身内建变量
			从自定义变量中导出的环境变量
	10. 设置变量的方法
		-- /etc/profile 针对所有用户
		-- ~/.profile 支队单一用户
		-- export导出，临时变量
		-- home目录下的.bashrc/Bash， 对应的配置脚本
	11. 环境变量的查看
		-- export查看
			$ export
		-- echo命令
			$ echo ${变量名称}
		-- env查看所有的环境变量
			$ env
		-- set命令查看本地定义的环境变量
			$ set
		-- vimdiff查看环境变量，查看不同
			$ vimdiff env.txt export.txt set.txt
		-- 删除环境变量
			$ unset temp
		-- 修改环境变量
			${变量名#匹配子串} -- 从头开始匹配
				-- ## 最长匹配
			${变量名%匹配子串} -- 从尾向前匹配
				-- %% 
			${变量名/旧字串/新字串} -- 字串替换
				-- // 替换全部
	12. 环境变量生效
		-- source可以读取并执行指定文件中的命令
		-- 可以通过source让配置文件立即生效
	13. 常用的环境变量
		- PATH 执行命令或程序的路径
		- HOME 当前用户主目录
		- HISTSIZE 历史记录数
		- LOGNAME 当前用户的登录名
		- HOSTNAME 当前主机的名称
		- SHELL 当前用户shell类型
		- LANGUGE 语言环境变量
		- MAIL 邮件存放目录
		- PS1 基本提示符
	14. 终端 -- 人机交互的接口
		-- linux终端类型
			- /dev/tty 当前进程的控制终端
			- /dev/ttySn 串行口终端
				串行端口对应设备名称/dev/tts/0
			- /dev/pty 伪终端
				master/slave
			- /dev/ttyn tty1 ~ tty6虚拟终端，tty0当前虚拟终端的别名
			- /dev/console 控制台终端
		-- linux常见的终端模拟器
			- gnome-terminal
			- Konsole
			- xterm
			- rxvt
			- kvt
			- nxterm
			- eterm
		-- tty命令可以查看它具体对应哪个实际终端设备
	15. console 控制系统的地方
	16. 控制台终端文件 -- /dev/console
		tty1-tty6虚拟终端
		Ctrl+Alt+F1~F6
Linux用户与权限
	1. 用户与用户组
		-- 用户管理
		-- 用户组，具有相同特征的用户的逻辑集合
	2. 用户与用户组相关配置文件
		-- /etc/passwd 用户信息文件
		用户名:密码:UID:GID:用户说明:家目录:登录shell类型
		-- /etc/shadow 密码文件
		username:password:最后一次修改时间:密码最短有效天数:密码最长有效天数:密码过期前警告时间:密码过期后保留时间:用户失效时间:保留位
		-- /etc/group 保留用户组信息
		groupname:group password:GID:组内用户列表，多个用逗号隔开
	3. 创建用户
		-- useradd [选项] [用户名]
		选项说明:
			-c comment，指定用户说明
			-d 指定某个目录为家目录
			-g 指定用户所属组
			-G 指定用户所属附加组
			-s 指定登录的shell类型
			-u 指定UID
		$ id username -- 查询用户信息(UID,GID)
		$ sudo passwd username 设置密码
			$ passwd -h 查看其具体的使用
			$ passwd -d username 删除密码
		$ sudo tail -1 /etc/passwd 查看最后一行
		$ su username 切换用户
	4. 修改用户
		-- usermod [选项] [用户名]
		选项说明：
			-a 该参数给用户添加一个新的附加组
			其他参数与useradd类似
	5. 删除用户
		-- userdel [选项] [用户名]
		选项说明:
			-r 用户家目录同时一起删除
	6. 查看用户
		-- /etc/passwd UID大于5000以上用户
		$ w -- 查看当前用户
		$ who
		$ whoami 查看当前登录用户
		$ lastlog 查看登录记录
		$ id 查看用户ID和组信息
	7. 增加新用户组
		-- groupadd [选项] [用户组]
		选项说明:
			-g 指定新用户组的GID
			-o 允许添加形同GID的用户组
	8. 修改用户组
		-- groupmod [选项] [用户组]
		选项说明：
			-g 指定新GID
			-n 指定新名称
	9. 删除用户组
		-- groupdel 用户组名
	10. 查看用户所属的所有组
		$ groups 查看当前有效组
		$ groups username 查看当前用户支持的组
	11. 用户禁用与恢复登录
		-- 禁用
			# usermod -L username
			# passwd -l username
		-- 恢复
			# usermod -U username
			# passwd -u username
		禁用实际在/etc/shadow密码位添加一个特殊符号，使得密码失效
Linux 目录与文件
	1. Linux文件系统
		-- linux的文件系统采用树形结构，"/"为根节点
		-- 根目录必须挂载一个分区
		文件系统的构成
			-- namespace给事物对象命名，并按照一种层次结构来组织
			-- API查询和操作对象的一种系统调用
			-- 安全模型，保护、共享和隐藏对象
			-- 实现，用于逻辑模型和硬件系统连接
	2. Linux目录结构
		-- 路径
			-- 根目录 "/"
			-- 相对路径
				.
				..
				-
				~
			-- 绝对路径
				$ pwd
		-- 文件树
			-- 树型结构，无论几个磁盘分区，都只有一个目录树
			-- 文件系统布局遵从FHS
				-- "/"下面的各个目录应该放什么数据
				-- 针对/usr和/var两个子目录的定义
			安装tree
				$ sudo apt-get update
				$ sudo apt-get install tree
				$ tree / # 查看根目录的树形结构
	3. 文件属性
		$ ls -al
			从左往右：文件类型和权限、硬链接数、所有者、所属组、文件大小、最后修改时间、文件名
		-- Linux里一切皆文件
		-- 文件类型
			- 普通文件
			d 目录
			c 字符设备文件，让相关驱动程序作为输入输出的缓冲
			b 块设备文件，处理数据I/O驱动
			s 本地域套接口，实现进程间通信的连接，使用socker创建，rm或unlink删除
			p 有名管道FIFO，让运行在同一主机的两个进程相互通信，使用mknod删除，用rm删除
			l 符号连接，软连接，通过名称指向文件，用ln -s创建，用rm删除
		-- 文件权限
			三个一组,读、写、执行 rwx
			拥有者(U),所属组(G),其他用户(O)
			权限编码
				r 4,查看文件内容/查看目录下的文件或目录
				w 2,修改文件内容/在目录下删除
				x 1,执行脚本或程序/可以切换目录
			-- 改变文件或目录权限
				$ chmod [选项][权限][文件或目录]
				选项说明
					--reference=RFILE，根据参考文档设置权限
					-R 递归将权限用于所有的子目录和文件
			-- 修改权限的三种方式
				$ sudo chmode u=rwx,g=rwx,o=rwx file
				$ sudo chmode a=rw file
				
				$ sudo chmod u+x,g+x,o-rw file
				
				$ chmod 777 file
			-- 改变文件所属
				$ chown user:group file
			-- 改变文件所属组
				$ chgrp group file
			-- 修改默认权限
				$ umask, 以补码的形式
				/etc/profile,~/.bash_profile,~/.profile设置umask值
				
				对于文件，创建时不能有执行权限
	4. Linux文件操作
		-- 文件查看
			查看文件信息
			$ ls -l
			$ ls -a
			查看文件内容
			$ cat -n /etc/passwd
			$ tac /etc/passwd
			分页查看
			$ more /etc/passwd
			$ less /etc/passwd
			$ grep sh /etc/passwd
			$ head [选项][参数]
				选项说明
					-n<数字>,几行
					-c<字符>
					-v,文件名头部信息
					-q,不显示头部信息
			$ tail 从结尾开始显示
		-- 操作文件
			$ touch filename，创建空白文件
			$ mkdir dirnmae，创建空目录，也可以指定创建目录的权限
			$ cp [-r] source target,复制文件和目录
			$ rm [-rif] filename，删除文件或目录
			$ mv source target/newname,移动或重命名文件或目录
			$ du [-s] /home，计算文件或目录的容量信息，s查看目录总大小
			$ stat file,查看文件状态
		-- 链接文件
			$ ln -s source target，软连接,需要新inode
				-- 软连接可以跨分区，但源文件不能删除
			$ ln source target,硬链接,不需要新inode
				-- 目录不能创建硬链接
				-- 只有同一文件系统中的文件才能创建链接，只用root可以
Linux文件查找与打包
	1. find
		$ find [path...] [expression]
		expression
			options 影响整体的操作
			tests 返回一个true or false，取决于文件的属性
			actions 根据对应的操作
			operators 连接其他参数
		$ find /etc/ -size +100k - 找/etc/目录下文件大小大于100k的文件
			+n 大于n
			-n 小于n
			 n 等于n
		
		- 通配符
			* 匹配0个或多个字符
			？匹配任意一个字符
			[string] 匹配string字符串中的任意一个字符
			\ 转义
		- 查找指定名称的文件
			-name 指定名称
			-iname 指定名称并忽略大小写
			
			-path 指定路径（绝对或相对）
			-wholename 功能与-path类似
			
			-regex 使用正则表达式
			-iregex 
			-regextype 指定正则表达式的类型
		- 查找链接文件
			-P 默认选项，查找符号链接本身
			-L 查找链接所指向的文件
			-H 处理命令行参数，不遵守符号链接
			
			-lname 查找链接文件
			
			$ find -samefile file1 当前目录中与file1相同inode的硬链接
			
			-inum n filename 查找指定inode的文件
			-links n filename 查找有指定硬链接数的文件
		- 查找指定时间参数的文件
			-atime n testdict 访问时间
				n*24小时之前，n为0表示24小时内
			-amin n 分钟
			-ctime n testdict 状态改变
			-cmin n 
			-mtime n testdict 文件内容改变
			-mmin n 
		- 文件大小
			-size n[ckwMG]
		- 文件类型
			-type d/f/l（目录/文件/符号链接）
		- Owner
			-user uname
			-group gname
			-uid n
			-gid n
		- 文件普通权限类型
			-readable
			-writable
			-executable
		- 执行相应的命令
			-exec
				执行的命令或脚本
			-ok 功能类似，不过增加了一个确认环节
			# 必须的格式
			$ find . -type f -exec ls -l {} \;
	2. locate
		在一个保存有所有文件名和目录名的数据库中去查找
		$ updatedb 更新此数据库
		$ locate shiyanlou 文件或路径中包含
		$ locate --basename shiyanlou 文件中包含
	3. whereis
		查找二进制文件或源或man手册的文件
		options
			-f 定义查找范围
			-b 仅查找二进制文件
			-m 仅查找man手册
			-s 仅查找源
		$ whereis -m python 查找python帮助手册
	4. which
		查找shell命令的完整路径
		在环境变量PATH中列出目录中查找可执行文件或脚本
		options：
			-a 列出所有选项
	文件打包和压缩
	5. gzip
		对文件进行压缩 .gz文件结尾
		$ gzip file # 会取代原先的文件
		$ gunzip -v file 解压缩
	6. tar
		创建文件档案
		$ tar [option...] [FILE]
		options:
			-c/--create 创建一个存档
			-r 将文件附加到档案文件末尾
			-z/--gzip 指定gzip格式
			-v/--verbose 显示文件处理的详细过程
			-f 指定档案文件名称
			-x 还原文件
Linux文本编辑
	1. vim
		normal/insert/command line
		:set number
		:set ruler 显示当前光标的位置
		删除换行符 - 大写字母J
		撤销 - u ctrl+R 
		:set ignorecase 忽略大小写
		:{作用范围}s/{目标}/{替换}/{替换标志}g整行
		# 默认当前行
			:s/foo/bar
		# % 表示全文
			:%s/foo/bar
		# ,分隔起始
			:5,12s/foo/bar
		# .当前行+表示从起始行开始多少行
			:.,+2s/foo/bar
		# 在visual模式下，所选区域
			:'<,'>s/foo/bar
		# 替换标志
			g 整行替换
			i 大小写不敏感
			I
			c 每次替换是进行确认
				y 确认替换
				n 不替换
				a 替换所有
				q 退出查找模式
				l 表示替换当前位置并退出
		:wq filename 另存为
		
		- 多文件
			:n 切换到下一个文件
			:e 3.txt 打开新文件
			:e# 回到前一个文件
			:ls 列出当前编辑中的文件
			:b 2.txt 直接进入2.txt文件
			:bd 2.txt 删除以前编辑过的列表中的文件
			:e! 4.txt 新打开文件
			:f 显示正在编辑的文件名
			:f new.file 修改正在编辑的文件的文件名
		- 多窗口
			:new 打开一个新vim视窗
			:sp 1.txt 打开水平视窗来编辑
			:vsp 2.txt 垂直视窗
			ctrl+w s 当前窗口分割成两个水平视窗
			ctrl+w v 垂直视窗
			ctrl+w q 结束分割出来的视窗
			ctrl+w o 打开一个视窗并隐藏之前所有视窗
			ctrl+w j/k/h/l 移动到下/上/左/右面视窗
			ctrl+w J/K/H/L 移动视窗位置
			ctrl+w -/+ 缩小/增加视窗的高度
		- 配置vim
			:scriptname
			.vimrc
			set autoindent 自动缩进
			set nocompatible 与vi编辑器不兼容
		- 命令行模式
			:set nu 设置行号
			:set nonu
			
			:set list 显示制表符
			:set tabstop=4 tar字符长为4
			:set readonly 设置文件只读
			:set encodeing=utf-8设置编码格式
			:set fileencoding=utf-8设置文件编码
			:set softtabsotp=4设置tab为4个空格
			:set backup 生成备份文件
			:set nobackup
		- 其他模式
			v/V 可视模式
			r/R 替换模式
		- 内置教程
			$vimtutor
	2. gedit
Linux管道符
	1. I/O流
		- stdin
			标准输入
			文件描述符为0
			文件描述符：
				kernel使用文件描述符来访问文件
				文件描述符是非负整数.
				一个索引值，内核为每一个进程所维护的该进程打开文件的记录表
		- stdout
			标准输出
			文件描述符为1
		- stderr
			标准错误输出
			文件描述符为2
	2. 管道符
		linux命令之间以及linux程序和命令之间的通信
		$ command1 | command2 | command3
	3. 重定向
		- 重定向输入
			[n] < file 从文件描述符为n的文件重定向到file
			不指定n时，为标准输入
		- 重定向输出
			[n] > file
			从文件描述符为n的文件重定向到file
			不指定时为标准输出
			附加：>>
		- 重定向stdout和stderr
			$ command |& command2
			command命令的标准输出和标准错误作为command2的输入
		&> file
		or
		>& file
		附加：
		&>>file
		>>file 2>&1
	4. tee
		读取标准输入，将其写入标准输出和文件中
		$ tee [option].. [file]...
		option:
			-a/--append 附加到文件末尾
			-i 忽略中断信号
		$ tee test1 test2
		$ ls | tee out.txt
	5. 文本处理
		- 排序
			sort将文本内容以行为单位进行排序
			option:
				-u 去除重复行
				-t 指定分割字符,默认空格
				-o 输出到指定文件
				-k 指定使用某一列进行排序
				-r 修改为降序，默认为升序
			$ sort -k 3 -o test2 test1
		- 合并
			paste
				将多个文件以列对列的方式加以合并
				直接两个文件多列合并
			join
				将多个文件中有相同特征的行以类似paste的方式进行合并
		- tr
			将标准输入复制到标准输出，这个过程中可以执行转译或删除
			$ tr [option] set1 [set2]
				set1 需要转换或删除的原字符集
				set2 转换的目标字符集
			$ echo "shiyanlou" | tr a-z A-Z
		- xargs
			从标准输入构建和执行命令
			传递参数
			默认使用空格或换行符为定界符
			没有指定命令时，将参数传递个/bin/echo
			option：
				-a 从指定文件中读取，而非标准输入
				-d 自定义定界符(识别目标中的分隔符
				-n 每行最多参数个数
			$ echo "shiyanlou001xshiyanlou002xshiyanlou003" | xargs -n 2 -d x
Linux磁盘管理
	1. 系统信息
		- uname
			打印正在运行的操作系统的一些信息
			option:
				-a/--all 显示全部信息
				-m 显示硬件类型
				-n 显示网络节点的主机名
				-o 显示操作系统的名称
				-s 打印内核名称，默认选项
				-r 打印内核版本
		- lspci
			查看pci设备信息
			$ sudo apt-get install pciutils
			$ lspci
	2. 系统模块
		- lsmod
			显示已载入系统的模块信息
			$ lsmod
	3. 分区
		- df
			报告文件系统磁盘空间的使用情况
			$ df 显示当前被挂载文件系统的使用情况
			option：
				-h 以易读的方式显示容量大小
			/dev 存放设备文件的目录
			tmpfs 临时文件系统
			/dev/vda1 s SATA硬盘设备 h IDE设备 d disk磁盘
		- 硬盘 主分区，拓展分区，逻辑分区 -- MBR分区方式，最多只是4个主分区
		
		- $ sudo fdisk /dev/vdb 进入设备操作页面
		- 创建文件系统
			mkfs 特定分区上建立Linux文件系统
			mkfs tab tab 以.的扩展命令方式来达到对应的效果
			$ sudo mkfs.ext4 /dev/vdb1
		- 挂载
			$ mount [-t 文件系统类型] 待挂载项 挂载位置
			$ sudo mount /dev/vdb1 test1
			这只是临时挂载，实际需要修改/etc/fstab文件
			/dev/vdb1    /home/shiyanlou/test1    ext4    defaults    0    2
			从上往下一一对应
			filesystem: 对应设备
			mount point：挂载点
			type
			options：配置
			dump： 备份
			pass num：一般根目录对应设为0
	4. lvm
		逻辑卷管理
		$ sudo apt-get install lvm2
		$ fdisk /dev/vdb I查看系统类型id
		$ sudo pvdisplay /dev/vdb1
		- 物理卷
			$ sudo umount test1
			$ fdisk /dev/vdb
			I 查看文件系统类型id
			t 修改对应的文件系统类型 8e lvm
			$ sudo pvcreate /dev/vdb1 在已创建好的分区上创建物理卷
			$ sudo pvdisplay /dev/vdb1 查看一个物理卷信息
			$ sudo pvchange /dev/vdb1 对物理卷进行修改
		- 卷组
			在物理卷的基础上进行创建
			$ sudo vgcreate vg1 /dev/vdb1 /dev/vdb2
			$ vgdisplay vg1
			$ sudo vgchange -s 8MB vg1
			当需要扩展vg1卷组时
			$ sudo vgextend vg1 /dev/vdb3 /dev/vdb4
		- 逻辑卷
			从卷组中创建逻辑卷 lvcreate
			option：
				-n 指定逻辑卷的名称
				-l 通过指定PE的数量来指定逻辑卷的大小
				-L 直接指定逻辑卷大小
				-p 设置权限 r 只读 rw 读写
			$ sudo lvcreate -l 100 -n lv1 vg1
			$ sudo lvcreate -L 800M -n lv2 vg1
			$ sudo lvdisplay vg1 查看卷组vg1中的逻辑卷
			接着使用mkfs建立文件系统,挂载
			$ sudo mkfs.ext4 /dev/vg1/lv1
			$ sudo mkdir /home/shiyanlou/lv1
			$ sudo mount /dev/vg1/lv1 /home/shiyanlou/lv1
	5. 交换分区
		物理内存使用完后，将磁盘空间虚拟成内存来使用
		$ sudo lvremove /dev/vg1/lv1 删除逻辑卷
		$ sudo vgremove vg1 删除卷组
		linux交换区的id为82
		
		$ sudo mkswap /dev/sda5 设置交换分区
		$ sudo swapon 启动交换分区
		$ sudo swapoff 关闭
		
		开机自动swap，需要修改/etc/fstab文件
		$ top 查看swap分区
Linux系统备份与恢复
	1. 备份
		完整备份和增量备份
		- dump
			$ sudo apt-get install dump
			dump支持0~9级备份
			等级0，将整个文件系统进行备份
			等级1，相对于完整备份的修改文件进行备份
		option：
			-level 指定备份等级
			-f 指定备份设备
			-n 向群组内使用者发通知
			-T 指定备份时间
		$ sudo dump -0 -f /home/test.dump /
		$ file test.dump 查看备份文件信息
	2. 恢复
		restore
		option：
			-C 比较备份内容与当前实际内容的区别
			$ sudo restore -C -f test.dump -D /
			-f 指定备份文件
			-D 指定需要比较的文件系统
			
			$ sudo restore -r -f test.dump -T /home
			-T 指定需要恢复的路径
			
			$ sudo touch shiyanlou.txt
			$ sudo dump -1 -f test1.dump /
			$ sudo rm shiyanlou.txt
			$ sudo restore -i -f test1.dump
			部分恢复
			
			-i 交互模式，仅还原部分内容
			-r 还原整个系统
			-t 查看备份内容
	3. tar
		进行增量备份
		option:
			-g/--listed-incremental
		$ sudo tar -cvf shiyanlou1.tar -g metadata /home/shiyanlou
		$ sudo tar -xvf shiyanlou2.tar 备份目录下解压
	4. dd
		用于复制和转换文件，也可用于复制文件系统
		dd 默认从标准输入读取，输出到标准输出
		$ sudo dd if=/etc/hosts of=hosts
		
		# 创建临时swap区间
			$ sudo dd if=/dev/zero of=test_swap bs=1M count=1024
			$ sudo mkswap test_swap
			$ sudo swapon test_swap
		option：
			- bs 设置输入输出块大小
			- count 对应块数目
Linux任务计划
	1. at
		单次指定时间运行
		- 将任务放入到/var/spool/at目录中
		/etc/at.allow, /etc/at.deny管理限制，若这两个文件都不存在，只有root可以使用at
		
		$ sudo apt-get install at
		$ sudo service atd start
		# service 读取/etc/init.d中的脚本
			$ service 服务 operation
			operation:
				- start
				- stop
				- restart
				- reload
				- status
		$ at [options] args
		option：
			-f 指定包含具体指令的任务文件
			-q 指定新任务的队列名称
			-l 显示待执行任务的列表
			-d 删除指定的待执行任务
			-m 任务执行完成后向用户发email
		args：
			- 绝对计时
				midnight,noon,teatime(下午四点)
				hh:mm today, hh:mm tomorrow
				12小时制 2.30 am, 2:30 pm
				mm/dd/yy, dd,mm,yy,yy-dd-mm
			- 相对计时
				at now + 时间数量 时间单位
				minutes,hours, days, weeks
		
		应用
		$ at now +2 minutes
		at> echo "hello shiyanlou" > my.txt
		
		$ atq/at -l 查看任务
		$ at -c 2 查看指定任务
		$ atrm 任务号， 删除指定任务
	2. batch
		当系统负载低于1.5时或到达指定时间才执行任务
		$ batch
	3. crontab
		设置周期性被执行的指令
		/etc/cron.allow,/etc/cron.deny
		工作记录在/var/spool/cron/，不同用户记录在不同文件下
		
		# 格式
		minute hour day month "day of week" command
		* 任何时刻
		, 分隔时刻
		- 时间范围
		/n 每隔n单位间隔
		
		$ sudo service rsyslog start
		
		sudo cron -f & 启动
		
		$ crontab [-u username] [option]
		option:
			-u 只有root使用此
			-e 编辑crontab工作内容
			-l 列出crontab工作内容
			-r 移除所有crontab工作内容
		$ crontab -e 添加一个新的任务
		$ sudo tail -f /var/log/syslog 查看日志反馈
		
		- 系统级别的定时任务
			编辑/etc/crontab 文件
			cron服务监测的最小单位是分钟
			/etc/cron.daily 6:25
			/etc/cron.hourly 17
			/etc/cron.monthly 每月1号6:25
			/etc/cron.weekly 周日6:47
Linux软件管理
	1. dpkg
		debian安装包管理工具
		option:
			-i 安装指定安装包
			-R 指定目录，将安装该目录中所有包
			-r remove，移除某个已安装的软件包
			-I 显示deb包文件的信息
			-s 显示已经安装软件的信息
			-S 搜索已安装的软件包
			-L 显示已安装软件包的目录信息
		$ dpkg -l 显示已安装软件包列表
		$ dpkg -l git 查看已安装软件信息
		$ dpkg -L git 查看已安装软件安装目录信息
		$ dpkg -s git 查看安装包详细信息
		
		$ sudo apt-get -d install sysvbanner 只下载，不安装
		$ sudo apt-get -f install 修复安装（依赖）
		
		$ dpkg -r 软件名，会保存原有配置文件
		$ dpkg -P 完全卸载，会删除配置文件
	2. apt
		debian系列软件包管理工具
		- apt-get 管理软件包
		- apt-cache 查询软件包信息
		- apt-proxy 搭建apt代理服务器
		- apt-show-versions 显示系统软件包版本信息
		- apt-config 读取apt配置文件
		- apt-cdrom 将CD-ROM加入软件源配置文件
		client/server工具
		
		镜像站中 /var/lib/apt/lists
		软件缓存在/var/cache/apt/archives
		安装完，信息存在/var/lib/dpkg/available
		
		/etc/apt/sources.list 镜像源地址配置文件
		$ sudo apt-get update 更新镜像源
		
		- 查看软件包信息
			apt-cache pkgnames | less 查看所有可用软件包
			apt-cache stats 获取一些统计信息
			$ apt-cache search git 
			$ apt-cache search ^git$ 使用正则查询
			$ apt-cache show git 查询包详细信息
			$ apt-cache policy git 查询软件包安装状态
			$ apt-cache depends git 查询依赖包
			
		- apt-get操作软件包
			install 安装软件包
			update 更新本地软件列表缓存
			upgrade 升级本地可更新软件包
			distupgrade 解决依赖升级
			remove 移除已安装软件包
			autoremove 不用的软件包
			purge 完全移除
			clean 清空本地缓存deb包
			autoclean 移除已安装旧版本安装包
			
			option：
				-y 自动确认
				-s 模拟安装
				-q/-q=# 静默安装
				-f 修复依赖
				-d 只下载不安装
				-- reinstall 重新安装
				--install-suggests 安装apt建议的包
			$ sudo apt-get --reinstall install sysvbanner
			
		- 软件升级
			$ sudo apt-get update
			$ sudo apt-get upgrade
			$ sudo apt-get dist-upgrade
			
			只升级单个安装包
			$ sudo apt-get install --only-upgrade deb
		- 软件卸载
			$ sudo apt-get purge sysvbanner
			$ sudo apt-get --purge remove sysvbanner
			$ sudo apt-get autoremove
	3. aptitude
		整合版
		$ sudo apt-get install aptitude
	4. rpm
		$ rpm -i package-name.rpm
		$ rpm -e package-name
		$ rpm -qa 查询所有安装包
	5. yum
		- install 安装
		- clean 删除缓存数据
		- deplist 查看依赖关系
		- erase 卸载软件包
		- upgrade 升级软件包
		- groupinstall 服务安装
Linux启动流程
	1. 启动顺序
		- BIOS自检
			系统读取BIOS中的硬件信息，查找启动设备并设置优先级，系统自检（POST),启动执行硬件初始化并设置PnP设备，最后启动硬盘主引导记录MBR中的引导程序GRUB或lilo
		- GRUB/lilo引导启动程序
			引导加载程序启动Linux系统。引导程序将控制权交给内核，此时操作系统并未装入内存。ubuntu默认GRUB为引导加载程序
		- 装载Linux内核
			引导程序开始加载Linux内核。ubuntu的linux内核在/boot目录中
		- 系统初始化
			ubuntu基于事件的启动管理器--upstart,主要包括3个程序(init\telinit\runlevel)和相应的配置文件(/etc/init, /etc/rcN.d,/etc/init.d)
			系统内核先启动init进程，读取并运行/etc/init目录下的配置文件
		- 初始化阶段完成后，系统准备接受用户登录
			- bios 接管主板所有自检工作，掌握系统的启动
			- boot loader grup,开机管理程序制定核心文件来开机，并实际载入核心到内存中解压缩与执行
			- init进程
				系统的第一个进程，其他所有进程的父进程
				读取初始化脚本，完成系统相关管理任务
	2. 运行级别
		init是linux内核启动的用户级别进程
		默认运行级别文件是/etc/init/rc-sysinit.conf
		
		/etc/rc$.d中定义了各种运行级别的运行服务
		/etc/rc.local 任何开机时就进行的工作
		K开头的是系统将终止对应的服务
		S开头系统将启动对应的服务
			它们后面跟的数字是程序的优先级，数值越小，优先级越高
		级别：
			- 0 关闭系统
			- 1 让系统进入单用户(S，恢复)模式
			- 2/3/4/5 多用户模式，图形界面
			- 6 重启系统
			- S 单用户与（恢复）模式，文本登录界面，只运行很少几项系统服务
			
			默认情况下，ubuntu进入运行级别2
			/etc/init/rc-sysinit.conf
				default runlevel = 2
	3. 添加移除自启动程序
		- 图形界面
			设置 -> 会话和启动 -> 应用程序自启动
		- rc.local脚本设置
			/etc/rc.local中脚本设置
		- 自定义脚本文件
			$ vim new.sh 新建脚本
			$ sudo chmod +x new.sh 设置脚本权限
			$ sudo mv new.sh /etc/init.d/new_service.sh 移动脚本到启动目录
			将自定义脚本添加至启动项中
			$ sudo update-rc.d new_service.sh defaults 95
		- 使用sysv-rc-conf工具
			$ sudo apt-get install sysv-rc-conf
			$ sudo su
			$ sysv-rc-conf
				X 启动该服务，q 退出
		- 启动mysql
			使用update-rc.d
				$ sudo update-rc.d mysql defaults
				查看mysql的相关运行信息
				$ ll /etc/rc?.d/*mysql
				移除自启动
				$ sudo update-rc.d -f mysql remove
				指定运行级别上的状态,优先级50-2,3,4 优先级51-0
				$ sudo update-rc.d mysql start 50 2 3 4 . stop 51 0 1 5 .
				运行级别需要写全
			使用sysv-rc-conf工具
				$ sudo sysv-rc-conf
Linux进程与工作
	1. 进程的关系
		父进程进行资源回收与收尾工作
		- 僵尸进程
			子进程任务执行完，系统资源也归还了，但父进程未回收 PID还在 Z
		- 孤儿进程
			父进程结束，但子进程仍然在运行
			被init进程收养
		- 内核初始化 0
		$ pstree 查看进程树
		ps - afxo user,ppid,pid,pgid,command 查看进程
		
		- 进程分类
			功能与服务对象
				- 用户进程
				- 系统进程 内核，资源分配
			应用程序的服务类型
				- 交互进程 用户交互
				- 批处理进程 多个进程按顺序执行
				- 守护进程 周期性，系统后台
	2. 工作管理
		- 进程组 PGID 等于第一个成员的pid
		 每个进程组都会在一个Session中
		 Session针对一个tty建立,每个进程称为一个工作
		 前台/后台 ls &
		 
		 ctrl+z 前台工作停止并丢到后台中
		 $ tail -f /var/log/dpkg.log
		 $ jobs 查看停止在后台的工作
			+ 最近，-倒数第二
		 $ fg [%jobnumber] 后台工作放到前台并运行
		 $ bg [%jobnumber] 后台的工作启动
		 $ kill -signal %jobnumber 删除一个工作
		 $ kill -l 查看信号值
			-1 restart
			-2 ctrl+c
			-9 强制终止
			-15 以正常的方式终止该任务
	3. 进程的状态
		$ top 
			实时查看当前系统中进程的信息
			load average 1,5,15分钟内cpu平均负载
		查看cpu个数与核心数
		$ cat /proc/cpuinfo | grep "physical id" |sort | uniq|wc -l
		$ cat /proc/cpuinfo | grep "physical id"|grep "0" | wc -l
		load临界值为0.7
		NICE 静态优先级
		PR 动态优先级
		交互指令
			q 退出程序
			l 切换单核平均负载
			P 根据cpu使用百分比大小进行排序
			M 根据驻留内存大小进行排序
			i 忽略闲置和僵死进程
			k 终止一个进程
		$ ps
			$ ps aux 列出所有进程信息
			$ ps axjf 显示部分进程树
			$ ps -l 显示自己登陆的bash的进程
			$ ps -afxo user,ppid,pid,pgid,command 指定显示的信息
		$ pstree
			查看进程树
		$ pstree -up
			-A 各进程树之间用ASCII字元连接
			-p 列出进程pid
			-u 同时列出每个process所属账户
	4. 进程控制
		kill -9 pidnumber
Linux帮助命令
	1. 内建命令，外部命令
		- 内建命令 shell程序的一部分，shell常驻内存中
		- 外部命令 linux中的使用程序部分，通常放在
			/bin,/usr/bin,/sbin,/usr/sbin中
		$ type command 检查命令是否是内建还是外部
			- builtin
			- /usr/sbin/xxx
			- alias
	2. alias命令的使用
		shell内建命令
		简化命令输入
		$ alias ngconf='cd /etc/nginx/conf.d'
		$ unalias ls 取消别名
		
		alias永久生效，修改~/.bashrc
		临时忽略别名 \ls 'ls'
	3. help命令的使用
		bash的内建命令
		显示shell内建命令的简要帮助信息
		$ help ls
		$ ls --help
	4. man命令的使用
		显示系统手册页中的内容
		章节数
			-1 标准命令
			-2 系统调用
			-3 库函数
			-4 设备说明
			-5 文件格式
			-6 游戏娱乐
			-7 杂项
			-8 管理员命令
			-9 其他，用来存放内核例行程序文档
	5. info命令的使用
		$ sudo apt-get install info
		GNU超文本帮助系统，得到的信息更多
	6. 命令之间的关系
		help < man < info
Linux日志系统
	1. 日志文件
		$ sudo service rsyslog start
		$ ll /var/log 存储日志目录
		常用日志文件
			-alternatives.log 系统更新替代信息
			-apport.log 应用程序崩溃信息记录
			-apt/history.log 使用apt-get安装卸载软件的信息记录
			-apt/term.log 使用apt-get时具体操作
			-auth.log 登录认证的log信息
			-boot.log 系统启动时的日志信息
			-btmp 记录所有失败启动信息
			-dmesg 内核缓冲信息
			-dpkg.log 安装或dpkg命令清除软件包日志
			-kern.log 内核产生的日志，有助于定制内核
			-lastlog 记录所有用户的最近信息，需要使用lastlog命令查看内容
			-faillog 用户登录失败信息，错误登录命令也会记录在本文件中
			-wtmp 包含登录信息。谁正在登录系统，谁使用命令显示这个文件或信息
			-syslog 系统信息记录
			-apport.log 应用崩溃信息记录
	2. 日志格式
		- 事件发生时间
		- 发生的主机名
		- 启动的服务的名称
		- 实际信息内容
		使用last和lastlog提出ASCII文件内容信息
		$ lastlog 
		option：
			-b, --before DAYs 早于DAYS的登录信息
			-h, --help
			-R, --root CHROOT_DIR chroot到的目录
			-t, --time DAYs 晚于DAYs的登录信息
			-u --user LOGIN LOGIN用户的最近登录信息
	3. rsyslog系统日志
		日志产生方式
			- 软件开发商自己定义的日志格式
			- Linux提供的日志服务格式
		syslog 系统日志记录程序
		配置文件
			- /etc/rsyslog.conf 决定需要加载的模块，文件所属者
			- /etc/rsyslog.d/50-default.conf 配置Filter Conditions
		结构框架
			- Input 收集信息
			- Output 输出到日志文件 actions
			- Parser 解析
		核心模块Queue
		配置中rsyslog支持三种配置语法格式
			- sysklogd
			- legacy rsyslog
				以$符号开头的语法
			- RainerScript
				可以分割多行
				注释，#或/*...*/
		rsyslog.conf文件是从上到下的顺序执行的
		
		rsyslog系统日志的配置
			- 配置格式
				日志设备(类型).(连接符号)日志级别 日志处理方式
				日志级别0-7
				.xx 大于或等于
				.=xx 等于
				.!xx xx之外的等级
			日志设备
				- auth pam产生的日志
				- authpriv ssh,ftp登录信息验证，权限
				- cron 时间任务
				- kern 内核消息
				- lpr 打印
				- mail 邮件系统信息
				- mark(syslog) rsyslog服务内部消息
				- news 新闻组消息
				- user 用户程序产生
				- uucp unix主机间通信
				- local 1~7 定义的日志设备
			日志级别
				- emerge 0 严重事件-系统崩溃
				- alert 1 严重错误 - 程序关闭影响其他程序
				- crit 2 错误信息，程序关闭
				- err 3 程序中存在错误通知
				- warning 4 程序存在潜在错误告警
				- notice 5 程序运行需要注意事件
				- info 6 程序状态报告
				- debug 7 调试信息
	4. 日志文件的转储
		$ logrotate
			日志文件管理工具，把旧日志删除，根据天数或大小来切割或管理日志
			
			可以压缩日志文件，减少存储空间
			基于CRON运行
			/etc/cron.daily/logrotate
			配置/etc/logrotate.conf /etc/logrotate.d
			
			# see "man logrotate" for details  //可以查看帮助文档
			# rotate log files weekly
			weekly                             //设置每周转储一次(daily、weekly、monthly当然可以使用这些参数每天、星期，月 )
			# keep 4 weeks worth of backlogs
			rotate 4                           //最多转储4次
			# create new (empty) log files after rotating old ones
			create                             //当转储后文件不存在时创建它
			# uncomment this if you want your log files compressed
			compress                          //通过gzip压缩方式转储（nocompress可以不压缩）
			# RPM packages drop log rotation information into this directory
			include /etc/logrotate.d           //其他日志文件的转储方式配置文件，包含在该目录下
			# no packages own wtmp -- we'll rotate them here
			/var/log/wtmp {                    //设置/var/log/wtmp日志文件的转储参数
				monthly                        //每月转储
				create 0664 root utmp          //转储后文件不存在时创建它，文件所有者为root，所属组为utmp，对应的权限为0664
				rotate 1                       //最多转储一次
			}
		$ logrotate /etc/logrotate.d/ 通过输出日志信息查看错误日志信息
		$ sudo head -c 10M < /dev/urandom > /var/log/log-file
		快速生成文件填入10M随机比特流
		