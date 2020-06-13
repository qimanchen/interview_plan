# 课程回顾
	1）awk命令概念
		擅长取列 擅长统计分析日志
		awk命令语法 awk [参数] '模式{动作}' 文件
		awk执行原理
	2）awk解决实际问题
		匹配
		awk '$2~!/02$/{print $0}' oldboy.txt
		~ 匹配
		!~ 不匹配
		awk匹配替换
			gsub(/要替换的信息/,"替换的内容",替换第几列)
		awk删除信息
			awk '!/oldboy/'
		awk统计分析
			累加运算 i=i+1
			column -t 对齐功能
# 课程介绍及内容
	1)	常见面试题 --- 系统启动流程 服务开启自启方法
	2） 用户管理概念
	3） 用户权限说明
	4）	企业中用户管理注意事项
	01. 常见面试题
		- 系统的启动流程
			centos6
				- 启动电源
				- 开机自检(BIOS)
					检测内存cpu硬盘是否有问题
				- MBR引导
					读取磁盘的mbr存储记录信息，引导系统启动
				- GRUB菜单
					选择不同的内核/进行单用户模式重置密码
				- 加载内核（kernel）
					可以更好的使用内核控制硬件
				- 运行INIT进程/系统的第一个进程运行起来
					init进程控制后续各种服务的启动：启动顺序（串行控制）
				- 读取/etc/inittab
					加载系统运行级别文件
				- 执行/etc/rc.d/rc.sysinit脚本
					系统初始化脚本
					设置主机名和网卡信息
				- 运行系统特殊的脚本
					/etc/rc.local
					服务运行的脚本
				- 启动mingetty进程
					显示开机登录信息界面
			centos7
				- 启动电源
				- 开机自检(BIOS)
					检测内存cpu硬盘是否有问题
				- MBR引导
					读取磁盘的mbr存储记录信息，引导系统启动
				- GRUB菜单
					选择不同的内核/进行单用户模式重置密码
				- 加载内核（kernel）
					可以更好的使用内核控制硬件
				- 系统的第一个进程运行起来 systemd （并行启动）
					服务启动的时候，同时一起启动
				- 读取系统启动文件 -- 启动级别
					/etc/systemd/system/default.target
				- 读取系统初始化文件
					/usr/lib/systemd/system/sysinit.target
				- 使服务可以开机自启动
					/etc/systemd/system 加载此目录中的信息，实现服务开机自动启动
				- 启动mingetty进程
					显示开机登录信息界面
	03. 用户管理章节
		用户概念
			管理员用户 	root	0	权利至高无上
			虚拟用户	nobody	1-999（centos7) 1-499（centos6）	管理进程 无家目录 不能登录系统
			普通用户	oldboy	1000+	权利有限
		权限：
			r	read
			w	write
			x	execute
			文件信息
				r	可以读文件内容
				w	可以编辑文件的内容
				x	执行这个文件（脚本文件）
				- 测试信息
					oldboy_root.txt			oldboy.txt
				属主	root					oldboy			oldgirl
				环境准备
					1. mkdir oldboy_root.txt
					2. chown /home/oldboy.txt
					3. chmod 000 oldboy_root.txt
				没有权限
					属主可以对文件进行操作，显示信息
					- root 可以读写，不能执行
					- oldboy 不可以写，但vim强制执行可以覆盖掉文件
					- oldgirl 不可以写，但vim强制执行可以覆盖掉文件
				只有读权限
					- root 可以读写，不能执行
					- oldboy 属主仅可以读
					- oldgirl 它需要对该文件的目录有访问权限
				只有写权限
					- root 可以读写
					- oldboy 仅可以写
					- oldgirl 需要对文件所在目录具有访问权限，才能进行写，但不能查看文件内容
				只有执行权限
					- root 可以读写，执行
					- oldboy 不可以读写，执行
					- oldgirl 什么都不可以
				- 权限配置的结论
					01. root用户对所有文件有绝对的权限，只要有了执行权限，root用户可以无敌存在
					02. 对于文件来说，写的权限和执行权限，都需要有读权限配合
					03. 如果想对文件进行操作，必须对文件赋予读的权限
			目录信息
				r	读目录中文件属性信息
				w	可以在目录中添加或删除文件数据信息
				x	是否可以进入到目录中
				没有权限
					- root 读，写，执行
					- oldboy 什么都不能干
					- oldgirl 什么都不能干
				只有读权限
					- root 读，写，执行
					- oldboy 可以获取目录内文件名称，当信息无法获取
						[qiman@qiman tmp]$ ll test_dir
						ls: cannot access test_dir/test_dir.txt: Permission denied
						total 0
						-????????? ? ? ? ?            ? test_dir.txt
						针对test_dir只有读的权限，那么只能读取目录中的名称
							如果没法进入到目录中，那么就看不到目录中文件的属性信息，因此显示为？？
					- oldgirl 可以获取目录内文件名称，当信息无法获取
				只有写权限
					- root 读，写，执行
					- oldboy 无法创建，无法看，无法切换目录
					- oldgirl 无法创建，无法看，无法切换目录
				只有执行权限
					- root 读，写，执行
					- oldboy 无法看，无法创建，可以切换目录
					- oldgirl 无法看，无法创建，可以切换目录
				r-x:
				- 权限配置的结论
					01. root用户对目录信息有绝对权限
					02. 对于目录来说，写权限，读权限，都需要有执行权限配合
					03. 如何想对目录进行操作，必须有执行权限
				- 当目录赋予读的权限：
					为何显示不了目录的详细信息
				- 一个普通文件默认权限：644 保证属主用户对文件可以编辑，其他用户可以查看文件内容
				- 一个目录文件默认权限：755 保证属主用户可以对目录进行编辑，保证其他用户可以读取目录中的信息，可以进入到目录中
				- /tmp目录下的文件为何属主用户无法删除？
					要想删除文件和目录，必须要有写权限，且只有属主和root可以删除
			- 文件读取的原理 /oldboy/oldboy01/oldboy.txt，一层一层读取
				/ 1. 你的目录下有没有oldboy目录文件
					inode 属性信息，指向block信息 -> block 文件的名称
				/odlboy 2. 你的目录中，有没有oldboy01目录
					inode 属性信息，指向block信息 -> block 文件的名称，看有没有权限操作这个目录，如果有可以操作这个目录
			- 文件目录数据设置权限的方法
				1）根据用户信息进行设定（属主 属组 其他用户）
					属主 - user		u
					属组 - group	g
					其他用户 - other	o
					chmod u+r/w/x | u-r/w/x | u=rw filename|dirname
					chmod u=rw,g=..,o=.., filename|dirname
				2) 使用数值进行设定，根据用户进行批量修改
					chmod a=x oldboy.txt
					chmod 777 oldboy.txt
			- 操作用户的某个文件的操作，该文件目录需要对应的权限
				
# 课程总结
	- 删除文件，对应的目录必须拥有写的权限
	1) 系统开机的流程 （centos6 centos7）
	2）系统用户概念
		a 用户分类
		b 用户权限 （文件-权限 目录-权限）
			读写数据原理
		c umask 文件或目录的默认权限
			如何永久修改
	3） 系统的特殊目录 /etc/skel
# 练习
	- 两个权限问题：
		/oldboy/odlboy.txt
		01. oldboy.txt 权限 rwx--xr-- 属主如何操作文件 其他用户可以如何操作文件
			属主：可读可写可执行
			其他用户：只能读
		- 对目录进行操作必须拥有执行权限
		- 文件的读权限，获取文件或目录的inode信息
		被攻击了
			chmod 000 /, 对于根目录无法执行
	- 为什么创建的文件和目录权限不一致
		目录权限都是 755
		文件权限都是 644
			umask - 0022
			默认文件权限 666 - 022 644
				umask值是奇数 666 - 033 + 011 644 对应奇数位加1
				umaks是偶数 666 - 022 644
			默认目录权限 777 - 022 755
			！！ 把umask值看成拿掉的权限，比如0033,g=wx,o=wx这是要去掉的权限
	- 如何永久修改umask信息
		vim /etc/profile
			umask设置
			if [ $UID -gt 199 ] && [ "`/usr/bin/id -gn`" = "`/usr/bin/id -un`" ]; then
				umask 002  -- 用户umask权限
			else
				umask 022  -- 永久修改umask权限
			fi
	- 一个特殊文件，创建用户的home目录的模板
		/etc/skel
		[root@qiman ~]# ll -a /etc/skel/
		total 24
		drwxr-xr-x.  2 root root   62 Apr 11  2018 .
		drwxr-xr-x. 80 root root 8192 Mar  2 07:13 ..
		-rw-r--r--.  1 root root   18 Oct 31  2018 .bash_logout		当系统退出登录状态会执行的命令
		-rw-r--r--.  1 root root  193 Oct 31  2018 .bash_profile	别名和环境变量（只针对某个用户）家规
		-rw-r--r--.  1 root root  231 Oct 31  2018 .bashrc			别名和环境变量（只针对某个用户）
		
		useradd oldgirl --> /home/oldgirl/ ---> 目录中的数据内容会参考/etc/skel目录中的信息
		
		/etc/skel目录作用
			01. 目录中可以存储一些工作规范说明
			02. 调整命令提示符信息
				-bash-4.2$
				cp /etc/skel/.b* /home/newuser
				for i in $(seq 2);do userdel -r "man$i";done

# 拓展练习