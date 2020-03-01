# 系统操作命令及目录结构
# 课程回顾
	- 系统挂载
	- 系统的目录结构
	- 重要目录数据
		- 网卡配置文件
		- 解析域名的配置文件
# 课程介绍
	- 系统目录重要文件
		- 详细掌握/etc中的配置文件
			- 配置主机名称
				centos6: 
					临时修改
						# hostname 显示主机名称
						# hostname newname 修改主机名称
					永久修改
						vi /etc/sysconfig/network
				centos7:
					临时修改 
						# hostname 显示主机名称
						# hostname newname 修改主机名称 
					永久修改 （重启系统才能加载配置文件）
						vi /etc/hostname
					通过命令可以同时永久修改和临时修改
						# hostnamectl set-hostname newname
			- 解析映射文件
				hosts文件：在本地建立Ip地址和主机名称的对应关系
				windows本地解析文件位置：c:\Windows\System32\drivers\etc\hosts
				linux本地解析文件位置：/etc/hosts
			- 永久挂载系统
				/etc/fstab	开机自动挂载磁盘的配置文件
					分为多列
					UUID=2653fb0a-af55-432d-a5c0-771b16dcc70a	/	xfs	defaults  0 0
					UUID	挂载点	文件系统类型
			- 实现光驱开机自动挂载
				/dev/cdrom	/mnt	iso9660	defaults	0	0
			- 查看开机是否自启动
				# systemctl status sshd
			- 开机服务自启文件
				/etc/rc.local -> /etc/rc.d/rc.local
				vi /etc/rc.local
					systemctl start sshd
				- 总结rc.local文件作用
					1. 文件中的内容信息，会在系统启动之后进行加载
					2. 文件中的编写内容，一定是命令信息
				注意需要给与执行权限
				# chmod +x /etc/rc.d/rc.local
			- 查看系统的版本
				cat /etc/redhat-release
						
	- 系统命令
		- 查看系统运行级别
			# runlevel
		- 切换系统运行级别
			# init 运行级别
			- 永久切换
				centos6
					vi /etc/inittab
				centos7
					启动级别
					systemctl get-default 获取运行级别
					systemctl set-default rescue.target
					ls -l /usr/lib/systemd/system/runlevel*target
		- 系统运行级别
			windows
			centos6
				启动级别
					00	系统关机/维护模式 init 1 进入关机转态
					01	系统单用户级别
						可以直接修改，不用挂载
					02
			centos7
				启动级别
					/usr/lib/systemd/system/runlevel*target
					00	关机级别 维护模式 init 1 进入维护转态 poweroff.target
					01	系统单用户模式 用于修复系统或重置密码信息 rescue.target
						修改root密码：
							a. 进入开机界面 按e
							b. 在核心设置项中添加 init=/bin/sh
							c. ctrl + x 重启
							d. mount -o remount,rw / 挂载根目录
							e. password	修改密码
							f. touch /.autorelabel 新建认证信息
							g. exec /sbin/init	重启系统
					02	系统多用户 无网络
					03	系统多用户模式 正常系统运行级别 有网络 默认
					04	预留	multi-user.target
					05	图形 graphical.target
					06	重启级别 reboot.target
	- 变量加载文件
		什么是变量
			- 设置变量
				X=123 注意等号两边不要有空格
			- 获取变量
				echo ${X}
			- 脚本
				- *.sh 文件
				- 执行脚本
					sh 脚本名称
				- 作用
					多个命令整合在一个文件中
					通过执行加载脚本执行多个命令
		- 全局变量
			vi /etc/profile
			作用，让变量永久生效
				在此文件中添加变量
			source /etc/profiel	让系统重新加载文件
		- 系统中变量类型
			- 普通变量 人为设置
			- 环境变量 系统默认有的 $PATH
				1. 系统默认存在
				2. 大写
				cat /etc/hosts -> load $PATH -> get envir var info /usr/bin -> find cat command
			- 修改变量
				# PATH=${PATH]:/new_dict 临时修改
				永久设置：
					vi /etc/profile
					export PATH=${PATH}:/new_dict
		- 查看命令位置
			which cat
		- 系统命令别名
			alias ll='ls -l'
			用相同的别名时，会自动覆盖
			永久设置别名 /etc/profile
		- 使别名功能失效
			1. 取消别名
				unalias ll
			2. 使用撬棍\rm 忽略别名
			3. 使用绝对路径方式执行命令
	- vi使用技巧
作业：
	- 如何实现光驱开机自动挂载
		- 实现光驱开机自动挂载，使用/etc/fstab
			/dev/cdrom	/mnt	iso9660	defaults	0	0
		- 配置autofs
			1. 安装autofs
				rpm -qa | grep autofs 查看是否安装了
			2. 配置auto.master
				/etc/auto.master文件制定文件系统的挂载点
				挂载点		挂载时使用的配置文件		自动挂载前的空闲时间
				/mnt		/etc/auto.misc				--timeout 600（second）
			3. 配置auto.misc
				每一行表示一种文件系统
				相对挂载点		文件系统挂载时的参数		文件系统位置
				cdrom			-fstype=iso9660,ro,nosuid,nodev	:/dev/sr0
			4. 启动autofs
				service	autofs	restart
			5. 使用autofs
				当读取光驱时，600秒后会自动挂载
	- 开机自动创建/oldgirl/oldgirl.txt 文件，并且文件中有“oldgirl.com"信息内容
		vi /etc/rc.local
			# mkdir -p /odlgirl/oldgirl.txt
			echo "oldgirl.com" > /oldgirl/oldgirl.txt
		PS:运维人员工作宗旨 简单 高效 稳定