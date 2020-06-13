# 第五章Linux的文件权限和目录配置
# 命令
	chgrp
	chown
	chmod
	uname
	lsb_release
# 内容
	1. 使用者群组
		- 文件拥有者 -- 文件隐私
		- 群组 -- 团队开发
			- 一个账号可以有多个群组支持
		- 其他用户
		- /etc/passwd, /etc/shadow(secret code), /etc/group
		
	2. Linux文件权限概念
		- Linux文件属性
			su - 默认切换到root用户
			-rw-r--r--.  	1 		root 	root   	176 	Dec 29  2013 		.bash_profile
			文件类型与权限	连接数	拥有者	所属组	大小	文件最后修改时间	文件名
			- 文件类型
				d	目录
				-	文件
				l	link file
				b	可提供存储的设备（可随机存取设备）
				c	外设设备（一次性读取装置）
			- 连接数
				多少文件名连接到同一个i-node
			- 修改语系
				/etc/locale.conf
		- linux文件权限的重要性
			- 系统保护
			- 团队开发软件或资料共享
				SGID
		- 如何改变文件属性与权限
			- 改变所属组 chgrp
				PS：被改变的组名必须在/etc/group中
				chgrp [-R] dirname/filename
					-R 递归改变
			- 改变文件拥有者
				PS：使用者必须在/etc/passwd存在
				chown [-R] username dirname/filename
				chown [-R] username:groupname dirname/filename
					chown .sshd filename 只修改文件所属组
				- 什么时候使用
					当文件复制时，针对文件拥有者的修改
			- 改变权限 chmod
				- 数字设定
					4	r
					2	w
					1	x
					chmod [-R] xyz filename/dirname
				- 符号设定
					u	user
					g	group
					o	other
					a	all
					+ - =
					chmod u=rwx,go=rx filename
		- 目录与文件权限的意义
			- 权限对文件的重要性
				r	可以读取文件中的内容
				w	可以编辑，增加，修改文件中的内容，但不包括删除该文件
				x	可以被系统执行
			- 权限对于目录
				- 目录的主要内容为文件的列表
				r	可以读取目录结构清单，可以查询该目录下文件名信息
					- 只有读权限，并不能显示 ls 目录内文件的属性信息
				w	可以变动目录结构清单
					- 新建文件或目录
					- 删除
					- 改名
					- 移动
				x	表示使用者能进入该目录并成为工作目录
					只有x权限，仍然可以操作目录中的文件
				- 网站，目录至少给rx
			- 使用者执行命令与权限
		- Linux文件种类与后缀
			- 文件种类
				- regular file
					ASCII 纯文字档
					binary 二进制档
					data	数据档  -- cat读取乱码
				- 目录 directory
					d
				- 链接 link
					l
				- 设备与装置文件 device
					block设备 -- 存储 b 
					character设备 -- 外设 c 
				- 套接字 sockets
					/run /tmp
				- FIFO pipe
			- linux后缀
				只是为了表示方便
				*.sh	shell
				*.tar.gz	压缩档
				*.html	网页
			- linux文件名长度限制
				- 单一文件或目录文件名最长为255字节
					ASCII 255个字符，每个字符一个字节
					中文 128个字符，每个字符两个字节
			- Linux文件名限制
				避免特殊符号
	3. Linux目录配置
		- linux目录配置依据-FHS Filesystem Hierarchy Standard
						shareable			unshareable
			static		/usr(软件)			/etc(设置)
						/opt(第三方软件)	/boot(开机与内核)
			variable	/var/mail(邮件)		/var/run(程序运行)
						/var/spool/news		/var/lock
			/	根目录
				- 根目录与开机/还原/系统修复
				- 根目录所在分割槽越小越好
			/usr	软件安装与执行
			/var	系统运行
			/bin	系统执行档 可以被root与一般用户使用
			/boot	vmlinuz,开机使用，linux核心，开机选单和开机设置档
			/dev	装置
			/etc
				/etc/passwd 用户信息
				/etc/fstab 磁盘
				/etc/issue 	登录前提示
				/etc/opt 第三方软件配置文件
			/lib	开机时使用到的函数库
				/lib/modules/ 	核心模组
			/media 可移除装置
				/media/cdrom
			/mnt	临时挂载目录
			/opt	第三方软件
				以前/etc/local
			/run --> /var/run
			/sbin	开机过程中需要的，开机，修复，还原系统
			/srv	service 服务启动后数据存放
			/tmp	临时存储
			/usr
			/var	变动文件
			/home	家目录
			/root	root家目录
			/lost+found	ext文件系统特有
			/proc	虚拟文件系统 内存
			/sys	内核硬件
		- /usr unix software resource
			/usr/bin 	所有用户可以执行的命令 /bin为此文件的link
			/usr/lib	/lib --> /usr/lib
			/usr/local	管理员自己安装的软件
			/usr/sbin	/sbin --> /usr/sbin
			/usr/share	只读数据文件
				/usr/share/man
				/usr/share/doc
				/usr/share/zoneinfo
			/usr/src/ 源码
		- /var 系统运行时产生的资料
			/var/cache	缓存
			/var/lib	程序执行过程中需要的配置
				/var/lib/mysql
				/var/lib/rpm
			/var/lock	某些程序只能同时被一个程序使用
				/var/lock --> /run/lock
			/var/log	日志文件
				/var/log/messages
				/var/log/wtmp(记录登录者信息)
			/var/mail
			/var/run
				/var/run --> /run
			/var/spool/
				排队数据，使用后会被删除
				/var/spool/cron
		- 目录树
			root为根
		- 绝对路径，相对路径
		- uname -r 查看核心版本
		- uname -m 查看系统的位数
		- lsb_release -a
			
			
# 实例
# 练习
	請問底下的目錄與主要放置什麼資料：
	/etc/, /boot, /usr/bin, /bin, /usr/sbin, /sbin, /dev, /var/log, /run
		/etc/：幾乎系統的所有設定檔案均在此，尤其 passwd,shadow
		/boot：開機設定檔，也是預設擺放核心 vmlinuz 的地方
		/usr/bin, /bin：一般執行檔擺放的地方
		/usr/sbin, /sbin：系統管理員常用指令集
		/dev：擺放所有系統裝置檔案的目錄
		/var/log：擺放系統登錄檔案的地方
		/run：CentOS 7 以後才有，將經常變動的項目(每次開機都不同，如程序的PID)移動到記憶體暫存，所以 /run 並不佔實際磁碟容量