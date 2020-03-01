# 操作系统优化
# 课程回顾
	- vi的使用技巧
	- 系统的信息查看方法
	- 系统用户创建 用户切换 以及查看确认
	- 系统命令提示符优化
		命令提示符格式进行优化
		命令提示符的颜色优化
	- 系统源文件优化
		1. 基础源优化
		2. 拓展源优化
		- 如何确认软件是否安装
			a 重新再安装一遍
			b 利用rpm命令可以管理软件是否已经安装
				rpm -qa cowsay 查询系统安装的所有的软件中是否有该软件
				rpm -ql cowsay 列出被安装软件的相关文档
				PS:有些命令名称和软件包的名称是不相同的
				
				which 命令
				rpm -qf 文件(绝对路径) 查看系统中的文件属于哪个安装包
				rpm -qf `which ssh`
			- rpm 安装软件
				默认安装路径 /var/lib/rpm
				rpm -i **.rpm
				rpm -ivh **.rpm 显示详细安装信息
				rpm -ivh --prefix 新的安装路径 **.rpm
			- rpm 升级
				rpm -Uvh 没安装的直接安装，安装的更新
				rpm -Fvh 只对安装的更新
			- rpm 查询
				查询/var/lib/rpm中的资料库
				rpm -qa 已安装的软件
				rpm -qf 存在系统的某个文档（绝对路径）
				rpm -qc 已安装的软件 /etc下的相关文件
				rpm -qi 已安装软件名称 查看该软件详细信息
				rpm -qR 已安装的软件 软件依赖
				rpm -qp(icdlR) 找到rpm包的信息（未安装）
			- rpm 验证
				rpm -Va 系统上所有被修改的文件
				rpm -V 已安装软件名称 该软件被更动档案
			- rpm 数字证书
				rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 安装数字证书
			- rpm 反安装
				1. 找出相关软件
					rpm -qa | grep pam
				2. 先移除依赖
					rpm -e pam-devel
				- 若/var/lib/rpm文档破损
					rpm --rebuilddb 重建数据库
			- yum卸载
				yum remove pam-devel
			补充：linux和windows软件安装程序区别
				xxx.exe -- windows 安装
				xxx.rpm -- centos
# 课程介绍
	- 操作系统优化
		- 系统安全相关优化（将一些安全服务进行关闭）
			ps：安全和系统性能（系统管理效率）是成反比的
			1. 防火墙服务程序
				centos6
					查看防火墙服务装态
						/etc/init.d/iptables status
					临时关闭
						/etc/init.d/iptables stop
					永久关闭
						chkconfig iptables off/on(开启)
					
				centos7
					查看防火墙服务装态
						systemctl status firewalld
					临时关闭
						systemctl stop firewalld
					永久关闭
						systemctl disable firewalld
					PS:查看服务状态信息简便方法
						systemctl is-active firewalld 服务是否在运行
						systemctl is-enable firewalld 服务是否开机运行
			2. 系统的selinux程序
				selinux服务对root用户权限进行控制
				很多企业中：selinux服务默认关闭
				centos6 == centos7
					getenforce 确认selinux的状态
					状态
						permissive 服务会日志提示，但不阻止操作
						enforcing 服务正常开启
						disable 服务彻底关闭
					ps：在linux配置中，能复制就复制
				临时关闭
					setenfore [ Enforcing|Permissive | 1|0]
				永久关闭
					修改selinux配置文件
					/etc/selinux/config
					ps： 如果想要配置文件生效，只有重启
					企业中不要使用立马关机重启
		- 字符编码优化
			什么是字符编码：可以实现对非英文字符的支持
			支持中文比较好的编码：
				UTF-8 比较通用
				GBK 比较国际通用
			- 出现乱码的原因
				1. 系统字符集设置出现问题
				2. 远程软件字符集设置有问题
				3. 文件编写字符集和系统字符集不统一
			- 系统中字符集编码设置方法
				centos6
					查看默认编码信息
						echo $LANG
							en_US.UTF-8
					临时修改
						和7一样
					永久修改
						1. 和7一样
						2. vim /etc/sysconfig/i18n -> LANG
							source
						
				centos7
					查看默认编码信息
						echo $LANG
					临时修改
						LANG=utf-8
					永久修改
						1. vi /etc/profile -- LANG变量修改 方法一更加优先
						2. vi /etc/locale.conf -- LANG='zh_CN.UTF-8'
					补充：一条命令完整修改 localectl set-locale LANG=zh_CN.GBK
		- 使xshell软件远程连接速度加快
			1. 修改ssh服务配置文件
				vi /etc/ssh/sshd_config
					79行 GSSAPIAuthentication no
					115行 UseDNS no
			2. 修改hosts文件
				vi /etc/hosts
					主机ip 主机名称
			3. 重启ssh远程服务
				systemctl restart sshd
	- 系统基础优化总结
		1. 命令提示优化
		2. 下载yum源优化
		3. 系统安全优化
			防火墙优化 selinux优化
		4. 系统字符编码优化
			显示中文
		5. 系统ssh连接xshell优化
	- 阶段总结回顾
		1. 不会的东西要记下来
		2. 什么叫做知识掌握了
			作用清楚
			操作熟练
			原理可以绘图说明
			PS:给不清楚的人能讲明白
		- 第一阶段 服务器硬件知识和系统概念
		- 第二阶段 系统安装部署和远程连接
		- 第三阶段 系统管理基础操作命令（新增命令）
		- 第四阶段 目录结构知识
		- 第五阶段 系统基础优化知识
	- 第一阶段 服务器硬件知识和系统概念
		服务器硬件组成
			电源
			cpu
			内存
			磁盘
			风扇
		服务器核心知识
			- 服务器介绍部分
				1U 4.45cm
			- 服务器硬件详细说明
				电源 供电 冗余能力 -- 双路 UPS 发电机
				cpu 2个作用，处理任务，控制硬件，路数，核数
				内存 存储设备，临时存储 缓冲 缓存  内存组成 -> |进程|缓冲buffer|缓存cache|剩余空间
					电影存储：
						1. 电影拆分 -> 缓冲（知道缓冲满了） -> 放到磁盘中
						2. 磁盘 -> 缓存 -> 内存 （这样效率更高）
						缓冲 -> 写
						缓存 -> 读
					程序
					进程
					守护进程
				磁盘 存储设备 永久存储
					磁盘接口类型 SAS > SCSI > SATA
					raid盘
					1. 存储容量更大
					2. 数据存储更安全
					3. 数据存储效率更高
					raid的配置方法
				远程管理卡
					远程开启，远程安装系统
					
		服务器系统知识
			- 操作系统的组成
				内核-解释器bash-应用程序
			- 系统的发展过程
				谭邦宁 -- 教学Unix
				斯托曼 -- 类似unix更好的系统 FSF,GNU，GPL
				Linus -- linux
			- 系统发行版本
				redhat
				centos
				ubuntu
				
# 作业
	- 一个软件安装好了如何利用rpm命令进行卸载
		rpm -qa | grep 指定的命令
		rpm -qR 软件名称 -- 找出软件依赖
		rpm -e 依赖
		rpm -e 需要卸载的软件
	- 总结第一阶段课程知识
	- 进行一条课程内容复述，录音（全民k歌）
# 拓展
	- 如何创建多个用户（创建50个用户）
		centos:
		#!/bin/bash
		for usernum in `seq 1 50`
		do
			username="user${usernum}"
			useradd ${username}
			usepw=${username}
			echo ${usepw} | passwd --stdin ${username}
			echo "username=${username},password=${usepw}" >> /home/outputpw.txt
		done
		