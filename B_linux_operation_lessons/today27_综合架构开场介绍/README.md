# 课程介绍
	整体课程介绍：
		01. 备份服务
		02. 存储服务
		03. 实时同步服务
			定时任务的时间间隔为分钟
		04. 批量管理服务
		05. 网站服务（web服务）
		06. LNMP网站架构
		07. 负载均衡反向代理服务
		08. 高可用服务
		09. 监控服务
		10. 跳板机服务
		11. 防火墙服务
	今天
		01. 架构介绍
		02. 架构规划
			网络的规划
			主机名称规划
		03. 系统优化
			字符集优化
			安全优化（防火墙 selinux）
			ssh服务优化
			命令提示符优化
			yum源优化
		04. 进行虚拟主机克隆操作
		备份服务
# 课程知识回顾
	01. 什么是路由交换
		交换机：实现在同一个局域网内多台主机之间的通讯
		路由器：实现不同局域网之间的通讯
	02. 路由器的配置方法
		静态路由配置
		动态路由配置
	03. OSI7层模型
		数据封装与解封装
	04. TCP/UDP协议
		TCP三次握手
		TCP四次握手
		TCP11种状态集
	05. 网络的主要原理
		DNS解析原理 域名 -- IP地址
		补充：反向DNS解析 IP -- 域名
		ARP
		 IP -- MAC
	06. IP地址划分
	07. linux系统中路由配置
		静态默认网关路由
		静态网段路由
		静态主机路由
# 课程内容
	1. 中小型公司网站架构
		1）用户 -- 访问网站人员
		2）防火墙 firewalled
			进行访问策略控制
		-- 外网交换机
		3）负载均衡服务器 nginx
			对用户的访问请求调度处理
		4）web服务器 nginx
			处理用户的请求
		-- 内部交换机
		5）后端服务器
			数据库服务器 mysql
			-- 存储字符数据
			存储服务器 nfs
			-- 存储图片 音频 视频 附件等数据信息
			备份服务器 rsync+crond 定时备份，rsync+sersync 实时备份
			-- 存储网站所有服务器的重要数据
			缓存服务器 redis memcache mongodb
			-- redis
			-- 将数据信息存储到内存中
			-- 减缓服务器的压力
		6）批量管理服务器 ansible
			批量管理多台服务器主机
	部署网站架构：
		1）需要解决网站的单点问题
			高可用服务 -- keepalive
			数据库单点问题：高可用服务 -- mha
			存储服务器：高可用服务 -- keepalived
						分布式存储
			备份服务器：异地备份
			面试题：公司的数据是如何备份
			1）利用开源软件实现数据备份 rsync
			2）利用企业网盘进行数据备份
				七牛云存储
			3）利用自建备份存储架构 两地三中心
			缓存服务：高可用 -- 缓存服务集群/哨兵模式
		2）内部员工如何远程访问架构
			员工通道 -- VPN服务器（认证） 
			PPTP vpn
		3）内部员工操作管理架构服务器要进行审计
			-- 审计服务器（跳板机）jumpserver
		4）架构中服务器出现问题需要提前报警告知
			监控服务器（报警）zabbix
	02. 综合架构规划
		主机名称和IP地址规划
			00.	模板机			centos-01	10.0.2.200					192.168.90.200
			01. 防火墙服务器 	firewalld 	10.0.2.81（外网地址）		192.168.90.81（内网地址）	软件：firewalld
			02. 负载均衡服务器 	lb01 		10.0.2.15 					192.168.90.15 				软件：nginx keepalived
			03. 负载均衡服务器 	lb02 		10.0.2.16 					192.168.90.16 				软件：nginx keepalived
			04. web服务器 		web01 		10.0.2.17 					192.168.90.17 				软件：nginx
			05. web服务器 		web02 		10.0.2.18 					192.168.90.18 				软件：nginx
			06. web服务器 		web03 		10.0.2.19 					192.168.90.19 				软件：nginx
			07. 数据库服务器 	db01 		10.0.2.51 					192.168.90.51				软件：mysql MariaDB
			08. 存储服务器 		nfs01 		10.0.2.31 					192.168.90.31 			软件：nfs
			09. 备份服务器 		backup 		10.0.2.41 					192.168.90.41 			软件：rsync
			10. 批量管理服务器 	m01 		10.0.2.61 					192.168.90.61 			软件：ansible
			11. 跳板机服务 		jumpsever 	10.0.0.71 					172.16.1.71 			软件：jumpserver
			12. 监控服务器 		zabbix 		10.0.0.72(61) 				172.16.1.72 			软件：zabbix
			
			缓存服务器 忽略
	03.	优化配置模板主机
		1）进行网络配置
			a 添加网卡
				virtualbox需要添加三块网卡
				一块Nat网卡，一块host-only网卡，一块内部网络
			b 配置网卡
				方式一 nmtui
					172.16.1.200/24
					不需要网关和DNS
				方式二 直接修改/etc/sysconfig/network-scripts/ifcfg-eth*
		2）系统优化过程
			1. host文件配置
				cp /etc/hosts{,.bak}
				cat /etc/hosts/
				172.16.1.15		lb01
				172.16.1.16		lb02
				172.16.1.17		web01
				172.16.1.18		web02
				172.16.1.19		web03
				172.16.1.51		db01 db01.etiantian.org
				172.16.1.31		nfs01
				172.16.1.41		backup
				172.16.1.61		m01 jumpserver zabbix
			2. 修改yum源
				base
				epel
					阿里源
					yum install wget
			3. 关闭selinux
				sed -i.bak 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
				grep SELINUX=disabled/ /etc/selinux/config
				setenforce 0
				getenforce
			4. 关闭防火墙
				systemctl stop firewalld
				systemctl disable firewalld
				systemctl status firewalld
			5. 提权sudo
			6. 英文字符集优化
				localectl set-locale LANG=""
			7. 时间同步
				echo '#time sync by lidao at 2017-03-08' >> /var/spool/cron/root
				ntpdata -- yum install -y ntpdata
				
				echo '*/5 * * * * /usr/sbin/ntpdate ntp1.aliyun.com > /dev/null 2>&1' >> /var/spool/cron/root
				crontab -l
			8. 加大文件描述符
				echo '* - nofile 65535' >> /etc/security/limits.conf
				source /etc/security/limits.conf
				！！若不设置1024
				ulimit -a 查看可以打开的文件数
				tail -l /etc/security/limits.conf
				一个服务程序运行起来，会打开相应的文件
				lsof - list system open file
				lsof -i:22 查看某个服务打开的文件数
				yum install lsof
			9. 安装其他软件
				yum install lrzsz nmap tree dos2unix nc telnet wget lsof ntpdate bash-completion bash-completion-extra -y
			10. ssh连接优化
				/etc/ssh/sshd
				systemctl sshd
	04. 进行模板主机克隆操作
		快照
		克隆
			创建链接克隆（学习环境）
				优势：
					节省物理主机资源
					克隆主机效率快
				劣势：
					模板主机删除，链接主机也会失效
			创建完整克隆（企业环境）
				优势：
					模板主机删除，克隆主机依然可以使用
				劣势：
					消耗物理主机的资源
					克隆主机效率低
		克隆后虚拟主机配置
			a 修改主机名称
				hostnamectl set-hostname backup
			b 修改主机地址
				PS：一台一台顺序启动依次配置
				grep 200 /etc/sysconfig/network-scripts/ifcfg-eth[01]
				sed -i 's#200#41#g' /etc/sysconfig/network-scripts/ifcfg-eth[012]
				
				sed -i 's#200#61#g' /etc/sysconfig/network-scripts/ifcfg-eth[012]
				sed -i '/UUID/d' /etc/sysconfig/network-scripts/ifcfg-eth[012]
		补充：克隆好的主机无法远程连接：
			解决方式：
				长时间的Ping
				关闭xshell重新连接
	05.	备份服务器说明
		作用：
			01.	数据备份的服务器
			02. 进行数据日志统一保存
				grep -r "test-date" /backup/ 递归查询
		如何部署搭建备份服务器：rsync服务
	06.	什么是rsync服务
		Rsync开源、快速、多功能的，可实现全量及增量的本地或远程的数据备份
			全量
			增量
	07.	rsync软件使用方法
		rsync命令	lv4
		
		a. 本地备份数据
			cp
			rsync /etc/hosts /tmp
		b. 远程备份
			scp -rp /etc/hosts root@172.16.1.41:/backup
				-r	递归复制传输数据
				-p	保持文件属性信息不变
			rsync -rp /etc/hosts root@172.16.1.41:/backup/hosts_rsync
			
			rsync远程备份目录
				rsync -rp /etc root@172.16.1.41:/backup --- 备份目录后面没有 /
				rsync -rp /etc/ root@172.16.1.41:/backup --- 备份目录后面有 /
			总结：rsync备份目录时
				备份目录有斜线时，只将目录下面的内容进行备份
				没有时，会将目录本身以及下面的内容进行备份
		c.	删除备份
			rm
			rsync -rp --delete 一个空目录 172.16.1.41:/backup
			rsync -a --delete /null/ /backup
				--delete	实现无差异同步数据
		d.	替代查看命令ls
			rsync 172.16.1.41:/etc/hosts
		面试中：有一个存储数据信息的目录，目录中数据存储了50G数据，如何将目录中的数据快速删除
			rm /目录/* -rf
	08.	rsync 语法格式
		Local:  rsync [OPTION...] SRC... [DEST]
		本地备份数据
			src 要备份的数据信息
			dest 备份到什么路径
			
		Access via remote shell:
		Pull: rsync [OPTION...] [USER@]HOST:SRC... [DEST]
		Push: rsync [OPTION...] SRC... [USER@]HOST:DEST
		远程备份数据
			user@	-- 以什么用户身份拉取/上传数据，若不指名则为当前用户
			host	-- 远程主机ip/主机名称

		Access via rsync daemon:
		 Pull: rsync [OPTION...] [USER@]HOST::SRC... [DEST]
			   rsync [OPTION...] rsync://[USER@]HOST[:PORT]/SRC... [DEST]
		 Push: rsync [OPTION...] SRC... [USER@]HOST::DEST
			   rsync [OPTION...] SRC... rsync://[USER@]HOST[:PORT]/DEST
		守护进程方式备份数据 备份服务
			01. 可以进行一些配置管理
			02. 可以进行安全策略管理
			03. 可以实现自动传输备份数据据
	09.	rsync服务部署安装过程
		linux系统安装部署服务流程：
			1.	下载安装软件 yum
			2.	编写配置文件
			3.	搭建服务环境	备份目录/目录权限
			4.	启动服务程序	开机自动启动
			5.	测试服务功能
作业：
	将其他几台服务器克隆好
	rsync守护进程部署方法
	
企业项目：
	全网备份数据项目
	
课程总结
	01. 网站架构组成
	02.	网站架构规划（主机名称 主机地址 系统优化）
	03. 虚拟主机克隆操作
		a 关闭主机 -- 链接克隆
		b 克隆好的主机一台一台按顺序启动，修改配置（主机名称 主机地址）
	04.	rsync备份服务
		rsync命令用户	1v4
		rsync语法格式 本地备份 远程备份
	