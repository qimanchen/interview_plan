# 课程回顾
	1）用户相关的文件
		/etc/passwd
		/etc/shadow
			密码：
			!! 未设置密码
		/etc/group
		/etc/gshadow
	2）用户相关的命令
		useradd -u -g -G -M -s -c
		usermod -u -g -G -s -c
		userdel
		groupadd
		groupmod
		groupdel
		chown -R
		id
		w
	3）如何让普通用户获得root用户能力
		1）直接切换用户为root	su -
			su - /su有什么区别
				PS：当用户登录时，环境变量会体现用户信息
				su 切换用户，只切换了家目录，而环境变量没有改变
				su - 切换家目录时，环境变量也切换
				env | grep 'username' 确认环境变量是否改变
				su 需要的是要切换的用户的密码
			su - -c command 一次性指令
		2）直接修改文件权限
			rwx 属主信息
		3）让root用户将自己的部分赋予给普通用户
# 课程介绍
	1）用户权限说明
	2）系统定时任务
	01. sudo功能配置说明
		sudo [-u new_username] command 以某个用户执行一次命令
			-b 将后面的命令放到后台执行，不影响当前shell
		a 如何配置sudo权限信息
			visudo -- 语法检查功能
			/etc/sudoers
			visudo -c -- 配置好了语法检查
			- 扩展配置方法 -- 针对单个用户
				1） 授权单个命令或多个命令
					root    ALL=(ALL)       /usr/sbin/useradd, /usr/bin/rm
					使用者帐号	登录者来源主机名称=(可切换的身份)	可下达的命令（必须用绝对路径）
					
				2）授权单个命令目录或多个命令目录（需要排除某些命令）
					root    ALL=(ALL)       /usr/sbin/*	给一个目录下所有命令权限
					root    ALL=(ALL)       /usr/sbin/*,!/usr/sbin/visudo 排除某个命令
					myuser1		ALL=(root)	/usr/bin/passwd 赋予myuser1可以设置密码
					myuser1		ALL=(root)	!/usr/bin/passwd,/usr/bin/passwd [A-Za-z]*,!/usr/bin/passwd root 限制不能修改root密码
					
				3）	不需要输入用户密码，可以直接sudo的方式执行命令
					root    ALL=(ALL)       NOPASSWD: /usr/sbin/*
				4）别名设置visudo
					[root@study ~]# visudo  <==注意是 root 身份
					User_Alias ADMPW = pro1, pro2, pro3, myuser1, myuser2
					Cmnd_Alias ADMPWCOM = !/usr/bin/passwd, /usr/bin/passwd [A-Za-z]*, !/usr/bin/passwd root
					ADMPW   ALL=(root)  ADMPWCOM
					HOST_Alias 来源主机别名，这些名称都要大写
				5） sudo的时间间隔 -- 默认5分钟
					
					[root@study ~]# visudo
					User_Alias  ADMINS = pro1, pro2, pro3, myuser1
					ADMINS ALL=(root)  /bin/su -
					切换为root
			- 针对用户组
				%wheel 表示群组
				usermod -a -G wheel pro1 将pro1加入到wheel
					-a 表示为增加支持群组，而不是设置
				
		b 如何查看确认配置
			- 切换到授权的用户下
			- sudo -l 需要授权的用户密码
		c 如何使用sudo功能
			sudo command（授权的命令）
	03. 设置特殊权限位
		rwx -w- --x 系统文件数据的9个权限位 系统中实际应该有12个权限位
		setuid：s
			4
			chmod u+s
			chmod 4755
			总结：setuid权限位设置，将文件的属主能力分配给所有人
		setgid：s
			2
			chmod g+s
			chmod 2755
			总结：setuid权限位设置，将文件的属组能力分配给所有用户组
		sticky bit：粘滞位 t
			1
			chmod o+t /share_dir/
			chmod 1755
			共享，查看文件内容
			其他人只能看，不能修改
			作用：可以将不同用户信息放置到共享目录中，实现不同用户数据可以相互查看，但不可以互相随意删除
			系统中共享目录 1777 /tmp
		总结：普通用户拥有root用户能力
			01. 直接切换用户 su -
				- 简单快捷
				- 风险太高，root权限位泛滥
			02. 修改数据文件权限 9位权限位 属主信息
				- 只针对某个数据文件进行修改，只针对某个用户进行授权
				- 需要了解权限位功能
			03. 修改sudo提权方式
				- 可以利用文件编辑指定用户有哪些权限
				- 配置规划复杂
			04. 修改数据文件权限 3位权限
				- 设置权限简单方便
				- 设置好的权限，所有用户都拥有
	04. 如何防范系统中的重要文件不被修改(root用户都不能修改）
		隐藏权限
			- 给文件加锁，使root用户也不能直接修改相应文件
			chattr +i 只读文件
			chattr -i 解锁
				- 更安全，将命令移动到其他命令
					重命名 mv chattr oldboy_attr
				
			chattr +a 仅能增加
			lsattr 查看隐藏权限
	05. 定时任务概念（第一个服务）
		作用：
			1. 类似生活中的闹钟
				alarmy 叫醒方式
					- 做算数题
			2. 可以自动完成操作命令
				备份(访问量少) 白天(访问量也少-游戏)
				cp /data /backup
				自动清理磁盘
				自动进行时间同步更新， ntpdate xxx
		实现方式
			- cronie	实现定时任务功能
			- atd		实现定时任务 只能一次设置定时功能
			- anacron	实现定时任务功能， 7*24小时服务
		检查软件是否安装 cronie
			rpm -qa cronie
			[root@qiman ~]# rpm -ql cronie
			/etc/cron.d
			/etc/cron.d/0hourly
			/etc/cron.deny
				
			/etc/pam.d/crond
			/etc/sysconfig/crond
			/usr/bin/crontab
			/usr/lib/systemd/system/crond.service
			/usr/sbin/crond
		- rpm -ivh 软件包.rpm安装软件包
			-i install 安装
			-v			显示过程
			-h			以人类可读的方式
		- rpm -e cronie --nodeps  禁止使用yum remove
		- 如何让linux和windows主机之间传输数据
			yum install -y lrzsz
			在linux上操作
			rz -y (windows -> linux) 从windows上下在重要数据信息
			sz -y (linux -> windows) 从linux上上传重要数据到windows
		- 一个文件大的时候，导致查看时一直刷屏
		- 定时任务实现方法
			- 日志文件需要定期进行切割处理
		- 系统中特殊目录
			- 系统定时任务周期：每小时 控制定时任务目录：/etc/cron.hourly
			- 每一天 /etc/cron.daily
			- 每一周 /etc/cron.weekly
			- 每一个月 /etc/cron.monthly 
		- 用户定时任务
			- 每天02:30 进行数据备份
				用户定时任务查看 crontab -l
					列表查看定时任务信息
				用户定时任务编辑 crontab -e
					编辑配置定时任务信息	
				crontab -e 编写定时任务  vi /var/spool/cron/ 定时任务配置文件保存目录
											/var/spool/cron/root root用户设置的定时任务配置文件
	06. 定时任务实际编写方法
		- 定时任务环境准备
			systemctl status crond 查看定时任务是否启动
			是否开机自启
		- 实际编写定时任务
			- 配置方法：crontab -e
				vi /var/spool/cron/root root用户
				vi /var/spool/cron/oldboy 普通用户
			- 查看定时任务 crontab -l
				cat /var/spool/cron/root
			- 编写的语法规范
				# Example of job definition:
				# .---------------- minute (0 - 59)
				# |  .------------- hour (0 - 23)
				# |  |  .---------- day of month (1 - 31)
				# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
				# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
				# |  |  |  |  |
				# *  *  *  *  * user-name  command to be executed
				分钟 小时 日期 月份 几周 user-name command /etc/crontab 中
				- 写法：
					01. 用数值表示时间信息
						00 02 * * * 备份文件
					02. 利用特殊符号表示时间信息
						* * * * * 备份文件
						* 表示每
						- 定时任务最短的执行的周期是分钟
						*/5 */5 * * * 备份文件
						每5分钟
						01-05 02 * * * 备份文件
						01到05每分钟 -- 指定时间的范围
						
						00 14,20 * * * 备份文件
						   指定不连续的时间信息
				- 什么时间做什么，然后在想下一次什么时候执行，做什么事
				- 测试
					- 每天14:30分，起来学习
						30 14 * * *
					- 每隔3天 夜里两点 执行数据备份
						00 2 */3 * *
					- 00/10 01,03 * * *
						*/10 --> 01:00 01:10
						每天 1点和3点的 每隔10分钟0点整 --> 01:00 03:00
						隔10分钟后的下一个整点
					- */10 01-03 * * *
						每天 1:10,2:10,3:10
					- * 01,03 * * *
						每天 1点的每分钟，3点的每分钟
					- * 01-03 * * *
						每天 1点到3点的每分钟
					- 00 02 28 */2 7
						错误，日期和周不能同时使用
				- 结论：
					01. 在写时间信息时，如果想要表示每隔多久执行什么任务
						/上面尽量用*表示，不要写具体数值
					02. 时间信息由左到右依次书写，尽量不要跳步
					03. 当编写定时任务时，日期信息不要和星期信息同时出现
				- 补充说明
					00/10 01,03 * * *
					/之前写数字表示，从那分钟开始执行
					20/10
						01:20 01:30 ...
					01:00 01:10 01:20 01:59
					03:00   03:59
		- 实际编写定时任务
			- 每天凌晨两点 备份 /data 目录到/backup
				- 写上时间信息
					00 02 * * *
				- 具体命令
					cp -a /data /backup
				- 编写定时任务
					crontab -e
					00 02 * * * /bin/cp -a /data /backup
			- 定时任务排查方法
				01. 检查是否有定时任务配置文件
					cat /var/spool/cron/root
				02. 检查定时任务日志文件
					ll /var/log/cron
					- 日志信息说明
						Mar  5 01:09:21 qiman crontab[12319]: (root) BEGIN EDIT (root)
						时间			主机名 	编辑/执行		以什么用户编辑或执行定时任务/干了什么事
	07. 定时任务编写注意事项:(规范)
		1) 编写定时任务要有注释说明
			# the data file backup - author:qiman
			00 02 * * * /bin/cp -a /data /backup
		2) 编写定时任务路径信息尽量使用绝对路径
			tar zcvf /backup/data.tar.gz /backup/data
			# gzip data
		3）编写定时任务命令需要采用绝对路径
			定时任务执行时，识别的PATH信息只有:/usr/bin:/bin
			- 命令执行成功条件
				1. 到PATH中找命令
				2. 命令找到了，执行成功
		4）编写定时任务时，可以将输出到屏幕上的信息保存到/dev/null中，避免占用磁盘空间
			&>/dev/null
			1> fiel 2>&1
			定时任务中执行命令，如果产生屏幕输出信息，都会产生邮件
			You have new mail in /var/spool/mail/root
			ll /var/spool/mail/root 不断变大，会占用block空间
				df -- 查看block
			- 解决方法：
				systemctl stop postfix 将邮件服务关闭
				关闭服务后，/var/spool/postfix/maildrop/ 不断产生小文件，会占用inode
					df -i 查看inode
				- 解决方法，删除小文件
					rm -f /var/spool/postfix/maildrop/*
		5) 编写定时任务，尽量不要产生屏幕输出信息
			cp -a /data /backup
			tar zvcf /backup/data.tar.gz /data 有信息输出
			tar zcf /backup/data.tar.gz /data
				可以切换到上一级目录上
		6）当需要多个命令完成一个定时任务需求时，可以利用脚本编写定时任务
			crontab -e
			* * * * * /bin/sh /server/scripts/backup.sh &>dev/null
			/etc/cron.deny -- 黑名单，用户名
	08. 规范
		- 定时任务执行命令规范
			01. 测试定时执行命令
				- 定时任务执行命令使用绝对路径
			02. 编写定时任务
				- 定时任务编写时注意语法规范
					- 编写注释
				- crontab -e
			03. 检查定时任务效果
				- 查看定时任务日志
				- 查看定时任务效果
					- 临时修改定时任务每分钟
					- 最终修改定时任务时间
			04. 排查定时任务问题
				- 查看定时任务日志
				- 查看定时任务效果
		- 定时任务脚本规范
			01. 测试定时执行命令
				- 定时任务执行命令使用绝对路径 /bin/sh 
			02. 编写定时任务
				- 定时任务编写时注意语法规范
					- 编写注释
					- 编写定时任务 /bin/sh shell.sh
				- crontab -e
			03. 检查定时任务效果
				- 查看定时任务日志
				- 查看定时任务效果
					- 临时修改定时任务每分钟
					- 最终修改定时任务时间
			04. 排查定时任务问题
				- 查看定时任务日志
				- 查看定时任务效果
# 课程总结
	
# 练习
	
# 拓展