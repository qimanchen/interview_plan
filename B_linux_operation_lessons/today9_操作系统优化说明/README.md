# 操作系统优化说明
# 课程回顾
	- 什么是挂载
		挂载到一个非空目录，会导致看不到原来的内容
			磁盘	/dev/sda1	/dev/sda2	/dev/sda3
			挂载点	/boot		swap		/	-> /mnt -> /dev/cdrom
											/mnt/oldboy.txt (根下面的一个目录）
		ps:在挂载时，尽量不要使用已经有数据的目录作为挂载点
		ps:卸载时，从目录中出来
	- 系统根目录下的信息
	- /etc目录中的内容 保存系统或服务的配置文件
	- /usr/local 保存安装的程序文件
	- /var/log	保存日志文件
		message 系统服务运行情况 错误信息
		secure 登录信息
		分析日志文件
	- /proc 进程信息 硬件信息
		ps： 目录中的数据文件是不能随意修改
	
# 课程介绍
	- vi的使用技巧 -- 编辑命令的使用技巧
	- 操作系统的优化 -- 环境准备
		企业中运维主要干什么
			1. 部署服务 命令
			2. 排错能力 经验
			3. 服务或系统优化能力
			4. 数据的分析能力
			5. 架构能力
		一种错误情况：你以为 -- 需要测试
		- 了解系统环境
			两个命令
				cat /etc/redhat-release 获得的系统发行版本和具体信息
				CentOS Linux release 7.6.1810 (Core)
				uname -a 显示系统的详细信息
				uname -n 主机名称
				uname -r 内核版本
				Linux qiman 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux 
				PS：记忆一下centos7系统的内核信息
		- 企业中管理系统用户身份是不同的
			- 老员工/经理 	root用户身份管理
			- 规范企业	普通用户
			- 普通用户如何创建
				useradd oldgirl 创建用户
				passwd oldgirl 设置密码
			- 普通用户如何切换
				su - 用户名 切换用户
			- 普通用户如何查看身份
				表示符
				- 查看用户是否存在
					su - old
					id old 查看用户是否存在
					PS1 命令行提示符
				- 查看用户是谁
					whoami 查看当前用户
		- 操作系统优化 -- 命令提示符的优化
			优化方法：修改PS1变量
			默认配置：[\u@\h \W]\$
			\u -- 显示当前登录用户名称
			\h -- 显示主机名称 -- 简写
			\W -- 显示当前所在目录信息（只显示末尾）
			\t -- 显示时间24小时格式
			\H -- 完整主机名
			\w -- 完整目录信息
			
			- 修改优化方法
				01. 修改命令提示符PS1
				02. 命令提示符如何修改颜色
					Linux系统中如何给信息加颜色
						PS1 = \[\e[32;1m\][\u@\h \W]\$ \[\e[0m\]
								设置颜色	内容		结束
						30 灰色
						31 红色
						32 绿色
						33 黄色
						34 蓝色
						35 粉色
						36 浅蓝
						37 白色
		- 操作系统优化 -- yum下载源优化
			yum优势：简单快捷
			1. 不需要到官方网站单独下载软件
			2. 可以解决软件的依赖关系
			- yum优化方法
				1. 优化基础的yum源文件
					mirror.aliyun.com
					CentOS7-Base.repo
					wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
				2. 优化扩展的yum源文件
					wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
				检查可用yum源的可用信息 yum repolist
				yum install -y cowsay
# 课程知识总结
	1. vi命令使用技巧
		vi命令三种模式以及切换方法
		如何快速移动光标进入编辑模式
		如何快速移动
		如何快捷便捷文档信息
	2. 如何查看系统信息
		cat /etc/redhat-release
		uname -a
	3. 如何设置系统用户信息
		创建用户
		切换用户
		查看用户信息
	4. 如何修改命令提示符
	5. yum源优化
		base
		epel
作业：
	如何每次登陆系统都提示小牛信息
	修改 cowsay "Welcom\!" > /etc/motd
拓展作业
	如何实现提示符是彩色的
		用户红色，主机绿色，目录蓝色
		\[\e[32;1m\] \[\e[0m\]	- 结束颜色只需要一个就可以
		[\[\e[31;1m\]\u\[\e[0m\]@\[\e[32;1m\]\h\[\e[0m\] \[\e[34;1m\]\W\[\e[0m\]]\$
		
		PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
		- 问题如何破解实验楼PS1的显示内容，具体是什么？？？