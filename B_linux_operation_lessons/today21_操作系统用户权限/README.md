# 课程回顾
	1）系统启动流程
		开机自检-MBR引导-grub菜单（内核 进入单用户）-加载内核-启动第一个进程init
		--> 自动加载系统运行级别 --> 加载系统初始化脚本 --> 启动系统开机自启服务-->启动tty终端/加载显示登陆界面进程
	2）系统用户管理
		a 用户分类
		b 数据文件权限说明(rwx)
			文件权限：- r
				- read	读文件内容的能力（有了读文件block的能力）
				- write	写文件内容的能力 （有了写文件block的能力） 重命名文件（不需要，主要对所在目录的需求）
				- execute 执行文件的能力（脚本文件）
			ps：文件是否可以编辑查看，和上一级或上n级目录有关
			目录权限 - x
				- read	读取目录文件属性信息
				- write	可以在目录中创建或删除数据
				- execute 可以切换进入到目录中
	3） 文件数据权限修改方法
		chmod u/g/o + - = rwx	--- 针对不同用户进行设置
		chmod a + - = rwx --- 	全部用户统一设置权限
		chmod 644 xxx -- - 全部用户统一设置，更加灵活
	4） 文件默认权限如何设置
		文件：644
		目录：755
		umask(内置命令):可以影响系统数据默认权限
		umask如何永久设置
			if [ $UID -gt 199 ] && [ "`/usr/bin/id -gn`" = "`/usr/bin/id -un`" ]; then
				umask 002 - 用户id大于199并且，属主和数组一样
			else
				umask 022
			fi
			- 判断符号
				-gt	>
				-lt	<
				-eq	=
				-ge	>=
				-le	<=
				-ne	<>
			- 逻辑符号
				&&
			id -gn 显示组名
			id -un 显示用户名
	5）一个特殊的目录 /etc/skel
		用户家目录都参照样板房设计
		- 家目录中特殊文件
			drwx------  2 qiman1 qiman1  83 Mar  2 00:06 .
			drwxr-xr-x. 6 root   root    61 Mar  1 23:30 ..
			-rw-------  1 qiman1 qiman1 926 Mar  3 09:16 .bash_history --- 历史命令记录文件
				曾经输入的历史命令保存位置
					1. 保存到内存中
						history
							help history
							history -c 清空历史记录
					2. 保存到磁盘中 ~/.bash_history
				
			-rw-r--r--  1 qiman1 qiman1  18 Oct 31  2018 .bash_logout
			-rw-r--r--  1 qiman1 qiman1 193 Oct 31  2018 .bash_profile
			-rw-r--r--  1 qiman1 qiman1 231 Oct 31  2018 .bashrc
			.viminfo -- vim样式设置
				自动加载文件样式信息
# 课程介绍
	1）用户相关的命令
	2）用户权限（如何让普通用户可以像root用户一样进行操作）
	01. 系统中和用户相关的文件
		/etc/passwd		记录系统用户信息文件
			[root@qiman ~]# head -5 /etc/passwd
			root	:x	:0	:0	:root	:/root	:/bin/bash
			01		02	03	04	05		06		07
			- 01：用户名
			- 02：用户密码信息
			- 03：用户uid
			- 04：用户gid
			- 05：用户的注释信息
			- 06：用户家目录信息
			- 07：用户登录系统方式
				/bin/bash
				cat /etc/shells 登录方式
					/bin/sh			-- 等价于/bin/bash
					/bin/bash		-- 通用的解释器
					/usr/bin/sh
					/usr/bin/bash
					/sbin/nologin	-- 无法登录系统
					sed -n "22s#/bin/bash#/sbin/nologin#gp" /etc/passwd
		/etc/shadow		系统用户密码文件
		/etc/group		组用户记录文件
		/etc/gshadow	组用户密码信息
	02. 系统用户相关命令
		a 创建用户命令
			useradd oldboy	普通用户被创建出来
			useradd oldboy01 -M -s /sbin/nologin 虚拟用户被创建出来
				-M 不创建家目录 但在/etc/passwd中会显示
				-s /bin/bash 指定用户登录方式
			useradd oldboy02 -u 2000
				-u uid 指定用户uid信息
			useradd oldboy03 -u 2001 -g oldboy02
				-g 组名/gid 指定用户默认组
			useradd oldboy04 -u 2003 -g oldboy02 -G oldboy01
				-G 组名/gid 指定用户加入组，附属组
			useradd mysql -s /sbin/nologin -M -c "manager database"
				-c 添加用户注释信息
		b 修改用户信息
			usermod
				-s /bin/bash	修改用户的登录方式
				-g root			修改用户主要的组
				-G				修改用户的附属组
				-u uid			修改用户的uid
				-c				修改用户注释信息
		c 删除用户
			userdel
				userdel alex01 删除用户和同名的组
				warning 提示建议
				userdel -r alex01 彻底删除用户
					-r 彻底删除用户以及家目录
		d 用户密码设置方法
			交互
				passwd oldboy
			非交互
				echo "password"|passwd --stdin
			- 企业中设置密码和管理密码的方式
				01. 密码要复杂12位以上字母数字及特殊符号
				02. 保存好密码信息
					keepass
						密码保险柜，本地存储密码
					lastpass
						密码保险柜，在线存储密码
				03. 大企业用户和密码统一管理（相当于活动目录ad）
					openldap域
					用户信息统一保存在一个用户管理服务器中，用户的家目录中的文件 用户密码 用户名称
					jumpserver
				04. 动态密码：动态口令，第三方提供自己开发也很简单
	03. 用户组相关命令
		groupadd	创建用户组
		groupmod	修改用户组信息
		groupdel	删除用户组信息
	04. 用户属主和数组设置命令
		chown 属主:属组 文件或目录
		chown -R Alex.Alex 	属主.属组	目录递归修改
		chown -R .Alex 只修改属组
	05. 用户信息查看命令
		a id 显示用户信息命令 （uid gid）
		b w 显示正在登录系统的用户信息
			 10:52:37 up 6 days, 11:49,  2 users,  load average: 0.00, 0.01, 0.05
			USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
			root     pts/0    192.168.90.1     08:30    5.00s  0.15s  0.00s w
			root     pts/1    192.168.90.1     09:18    1:33m  0.04s  0.04s -bash
			01		02			03				04		05		06		07
			- 01. 什么用户登录到系统中
				echo "..." >/dev/pts/1，通知用户
			- 02. 登录的方式
				pts/x	远程登录系统
				tty1	本地登录
			03. 从哪连接的服务器
			04. 登录时间
			05. idle空闲时间
			06. JCPU 用户操作系统 消耗cpu的资源时间
			07. 用户在干什么 -bash/sh
		c last 历史用户登录
		d lastlog 哪些用户最近一次登录过
	06. 用户权限说明
		普通用户如何像root用户一样操作管理系统
			a 直接切换到root用户
			b 直接修改要操作文件的权限
			c root用户赋予了普通用户权利
				sudo root用户授权一个能力给普通用户
				- 怎么授权
					visudo - 可以通过服务器来确认
					qiman	ALL=(ALL)	/usr/bin/useradd, /usr/bin/rm
					- 当编辑错误时，保存时会提示
				- 如何验证oldboy已经获取root用户权限
					sudo -l 可以显示sudo拥有的用户权限
				- 执行root用户可以执行的命令
					sudo command

# 课程总结

# 练习

# 拓展