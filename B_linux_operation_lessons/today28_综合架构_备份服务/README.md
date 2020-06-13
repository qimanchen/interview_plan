# 课程介绍
	1. 完成rsync守护进程模式搭建
	2. rsync备份传输数据原理
	3. rsync命令常用参数
	4. 企业应用rsync技巧
	5. rsync常见错误
	6. 企业项目：全网备份项目（脚本）
# 课程回顾
	1. 综合架构的组成部分
		前端
			防火墙 负载均衡 web服务器
		后端
			数据库 存储 备份 缓存
		扩展
			批量管理 跳板机 监控 VPN服务
	2. 综合架构的规划
		IP地址规划
		主机名称
		系统的优化部分
		目录结构
		用户
		脚本
	3. 虚拟主机克隆部分
		a 模板机关机克隆 -- 链接克隆
		b 克隆好的主机需要一台一台按顺序进行配置
			1. 不要随意修改调整虚拟主机的mac地址
			2. NetworkManager网络管理服务
				影响网络服务：
					network			/etc/sysconfig/network-scripts/ifcfg-eth[012] 配置文件的配置
					NetworkManager	nmtui	关闭服务
	4. 备份服务
		rsync 全量和增量备份的软件
	5. rsync命令使用方法，cp scp rm ls
	6. rsync命令语法 rsync
		本地
		远程
		守护进程
# 课程内容
	02. rsync守护进程部署方式
		第一个进程：下载并安装软件
			安装软件
			rpm -qa | grep rsync
			
		第二个进程： 编写配置文件 -- 服务端配置文件
			man rsyncd.conf
			vim /etc/rsyncd.conf
		第三个进程：创建rysnc服务的虚拟用户
			useradd rsync -M -s /sbin/nologin
		第四个进程: 创建备份服务器的认证文件
			ll /etc/rsync.password
			chmod 600 /etc/rsync.password 
		第五个进程：创建备份目录
			mkdir /backup
			chown rsync.rsync /backup
		第六个进程：启动备份服务
			systemctl start rsyncd
			systemctl enable rsyncd
			systemctl status rsyncd
		需要熟悉守护进程的名称语法
			Access via rsync daemon:
			客户端做拉的操作：恢复数据
			Pull: rsync [OPTION...] [USER@]HOST::SRC... [DEST]
				 rsync [OPTION...] rsync://[USER@]HOST[:PORT]/SRC... [DEST]
			推：备份数据
			Push: rsync [OPTION...] SRC... [USER@]HOST::DEST
				src：要推送备份数据信息
				[USER@]：指定认证用户信息 rsync_backup
				HOST：指定远程主机的IP地址或者主机名称
				::DEST：备份服务器的模块信心 [backup]
				rsync -avz /etc/hosts rsync_backup@172.16.1.41::backup
					参数说明：
						-a
						-v
						-z
				# 执行原理
					1. 进行用户认证
						-- 进入服务端时，则通过配置文件中用户进行数据存储
						-- 需要改变文件的属组，属主
					2. 进行目录确认
					3. 进行目录的用户确认
					4. 完成数据存储
				rsync: chgrp ".hosts.8RN6hI" (in backup) failed: Operation not permitted (1)
					# 错误原因，rsync用户无法修改用户属组
					# 解决：传输前修改文件的权限
					# /etc/rsyncd.conf -- fake super 伪装成超级管理员
				sent 292 bytes  received 124 bytes  118.86 bytes/sec
				total size is 422  speedup is 1.01
				rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1178) [sender=3.1.2]

				   rsync [OPTION...] SRC... rsync://[USER@]HOST[:PORT]/DEST
			
	03. 常见错误
		no route host -- 防火墙
		auth failed on module qiman -- 密码错误，配置文件和创建文件不一致，权限不正确，认证文件中的密码后有空格（echo
		# vim -- set list查看行后面的空格
		unknown module： -- 模块名称不一致 
		permission denied -- 备份目录的属主和属组不正确，用户错误
		chair dir -- 目录创建错误
	04. rsync守护进程客户端配置：
		1. 创建一个密码文件
			echo "centos" > /etc/rsync.password
			chmod 600 /etc/rsync.password
		2. 进行免交互传输
			rsync -avz /etc/hosts rsync_backup@172.16.1.41::backup --password-file=/etc/rsync.password
	05. rsync参数说明
		-v	--verbose 显示详细的传输信息
		-a	--archive 命令的归档参数 包含 rtopgDl
		-r	--recuri 递归参数
		-t	--times 保持文件属性时间信息不变，修改时间
		-o	--owner 保持文件的属主信息不变
		-g	--group 保持文件的属组信息不变
			vim /etc/rsyncd.conf
			以root用户作为管理用户
			# fake super = no 才能保证这个参数生效
		-p	--perms 保持文件权限信息不变
		-D			保持设备文件信息不变
		-l	--links	保持软连接属性信息不变
		-L	--		保持链接文件数据信息不变
			rsync -rtopgD -L
		-P(大写)			显示数据传输的进度信息
		--exclude=patterm 排除指定数据不被传输，单个排除
		--exclude-from=file 批量排除
		--bwlimit=rate	限制传输的速率 100M/8 = 12.5MB
			企业案例：人人网
		--delete		无差异同步参数，保持两台服务高度一致（慎用）
						我有的你有，我没有的你也不能有
			rsync -avz --delete /空目录 rsync_backup@172.16.1.41::backup
			意义：
				当存储服务器中删除了时，则无差异数据同步到备份服务器中
	06. 守护进程服务企业应用
		1 守护进程多模块功能配置
		sa sa_data.txt
		22,24copy24
			/etc/rsyncd.conf
			[dev]
				path = /dev
			[dba]
				path = /dba
			# 创建目录
			# 修改文件属主和属组
			# 重启服务
		
		2. 守护进程的排除功能实践
			准备环境，
			需求1，将a中的所有数据，b不要1.txt c不要
			rsync -avz /etc --exclude=b/1.txt --exclude=c/ rsync_backup@172.16.1.41::backup --password-file=/etc/rsync.password
				# --exclude是相对目录，相对于前面的/etc目录
			--exclude-from=绝对路径
				# 先编辑一个排除文件
					b/1.txt
					c/1.txt
					c/3.txt
					find 命令找出要排除的文件
				# 实现排除命令
		3. 守护进程创建备份目录 -- 多台服务器
			rsync -avz /etc/hosts rsync_backup@172.16.1.41::backup/10.0.2.17/ --password-file=/etc/rsync.password
			PS：不能创建多级目录
		4. 守护进程的访问控制配置 -- 黑名单，白名单
			hosts allow = 172.16.1.0/24			# 允许传输备份数据的主机--白名单
			hosts deny = 0.0.0.0/32				# 禁止传输备份数据的主机--黑名单
			1. 只有白名单，没有黑名单
				只看白名单，如果有，才可以传输数据
			2. 只有黑名单，没有白名单
				只有黑名单内的数据无法传
			3. 都有
				先看白名单信息
				再看黑名单
				其余的默认允许
				-- 即允许，又阻止，白名单优先于黑名单
		5.	守护进程的列表功能
			rsync rsync_backup@172.16.1.41::
作业：
	1. 完成全网备份项目
		三台服务器，web1，nfs01
		web服务器的配置文件
		本地按日期进行备份
		a 所有服务器有backup目录
		b /var/spool/cron/root
			/etc/rc.local
			/server/scripts
			/var/html/www
			/app/logs
		只保留7天的 -- web
		backup -- 只保留6个月的,保留每周一的数据副本
		
					
			