# 课程介绍
	1）远程管理服务器介绍
	2）SSH远程管理服务远程连接的原理
	3）SSH远程连接方式 秘钥连接方法
		password
		public key 秘钥
	4）SSH服务的配置文件 /etc/ssh/sshd_config
	5）SSH远程连接安全防范思路（防止入侵）
	6）总结SSH服务相关命令
		ssh scp
	7）ansible批量管理服务介绍
		saltstack
	8）ansible软件部署
	9）ansible服务简单应用
		
# 课程回顾
	1）实时同步服务原理
		a 部署rsync， 传输数据
		b 部署好inotify软件，监控数据变化
		c 部署安装sersync软件 将rsync+inotify软件结合
	2）相关软件部署安装
		总结一下这些服务的安装
	3）sersync的配置过程
		rsync命令掌握sersync服务配置方法
# 课程内容
	01. 远程管理服务概念介绍
		SSH -- 安全的远程连接	数据信息时加密的 22 ssh服务默认可以root用户远程连接 系统远程连接
		telnet -- 不安全的远程连接 数据信息是明文的 23 默认不能让root用户远程连接 网络设备远程连接
			yum install -y telnet.server
			systemctl start telnet.socket
			ps -ef | grep 23
			telnet 192.168.90.41 23 # 连接数据包
		补充：什么是shell？
			1. 每连接登录到一个linux系统中，就是一个shell
			2. 可以连接一个iinux系统有多个会话连接，每一个会话都是一个shell
			3. 系统中用户可以实现相互连接，每转换一个用户就是一个shell
			shell特点说明：
				1. 一般命令行临时配置的信息，只会影响当前shell
				2. 命令行配置的信息如果想要生效，需要切换shell才会生效
					bash -- exit
			shell 不同命令行会话 -- 多台主机
			shell -- 同一台主机多个会话
			shell -- 同一个终端，多个不同的用户
	02. SSH服务连接工作原理（数据加密）
		私钥：钥匙  --- 
			/etc/ssh/
			ssh client --- ssh 10.0.0.41 --- ssh server
			.ssh/known_hosts				 /etc/ssh/*.pub
					   --- TCP连接		 ---
					   --- 建立远程连接  --->
					   <--- 公钥信息|询问确认 ---
					   --- 	yes			 --->
					   <--- 公钥信息|确认密码信息 ---
					   ---	正确密码信息 --->
					   <--- ssh连接建立 ---
			>.ssh/known_hosts
		公钥：锁头
		a 客户端				执行远程连接命令
		b 客户端	服务端		建立三次握手过程
		c 服务端				让客户端进行确认是否接受公钥信息
		d 客户端				进行公钥确认，接收公钥信息
		e 服务端				让客户端确认登录用户密码信息
		f 客户端				进行密码信息确认
		g 服务端	客户端		远程连接成功
		
		私钥和公钥作用：
			1 利用私钥和公钥对数据信息进行加密处理
			2. 利用公钥和私钥进行用户身份认证
		基于密码的方式进行远程连接：公钥和私钥只能完成数据加密过程
		基于秘钥的方式进行远程连接：公钥和私钥可以完成身份认证工作
	
	03. ssh远程连接的方式
		a 基于口令的方式进行远程连接 连接比较麻烦 连接不太安全
			-- 每次都需要进行密码确认
		b 基于秘钥的方式进行远程连接 连接方便	  连接比较安全
			私钥和公钥放置于客户端（客户端的公钥和私钥）
			1. 客服端（管理端） 执行命令创建密钥对 私钥/公钥生成
			2. 客户端（管理端） 建立远程连接（基于口令的方式），发送公钥信息
			3. 客户端（管理端） 再次建立远程连接
			4. 服务端（被管理端） 发送公钥质询信息（你可以解析我的锁头吗）
			5. 客户端（管理端） 处理公钥质询信息（钥匙将锁头打开）将质询结果发送到服务端
			5. 服务端（被管理端） 接收到质询结果，建立好远程连接
	04. SSH实现基于秘钥连接的部署步骤
		准备
			准备好一台管理服务器
		1. 管理端创建密钥对
			ssh-keygen -t dsa
				-t 加密方式
			生成的目录会包存到/root/.ssh/id_dsa
		2. 管理端需要将公钥进行分发
			ssh-copy-id 分发公钥
			ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.41
				-i /root/.ssh/id_dsa.pub 
			服务端 /root/.ssh/authorized_keys
			
			# 发现当发送公钥后仍然需要密码 -- 查看/var/log/secure日志文件
				Apr 26 23:58:32 nfs01 sshd[16383]: Authentication refused: bad ownership or modes for directory /root
				/root目录权限不正确
			
			ssh 172.16.1.41 command
		3. 进行远程连接测试
			ssh 172.16.1.41 -- 不用输入密码信息。
			
		问题：
			01. 如何是吸纳批量管理多台主机
				如何编写脚本进行批量分发公钥
			编写脚本最简单的方式：堆命令
				#/bin/bash
				for 变量名	in 变量设置的值
				do
				done
				
				for ip in 31 41
				do
					ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.$ip
				done
				ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.41
				# 问题：有交互过程
				01. 需要有确认yes或no
				02. 需要输入密码信息
				03. 服务端端口号变化了，如何分发公钥
				
				# 如何不用交互输入密码信息，进行远程连接分发公钥：
					1. 安装一个软件
						yum install -y sshpass
						sshpass -p密码
					2. 执行免交互方式分发公钥命令
						sshpass -p密码 ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.41
				# 如何不要输出确认的输出信息
					>/root/.ssh/known_hosts -- 显示出确认信息
					sshpass -p密码 ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.41 "-o StrictHostKeyChecking=no"
				# 端口变了
					sshpass -p密码 ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.41 -p 22 "-o StrictHostKeyChecking=no"
			# 分发公钥脚本
				mkdir -p /server/scripts
				distribution_pub_key.sh
				脚本ip配置文件
				#!/bin/bash
				for ip in `cat ip.txt`
				do
					echo “=host 172.16.1.$ip pub-key start distribution ="
					sshpass -pcentos ssh-copy-id -i /root/.ssh/id_dsa.pub  root@172.16.1.$ip "-o StrictHostKeyChecking=no" &>/dev/null && echo "host 172.16.1.$ip success."
					echo “=host 172.16.1.$ip pub-key start distribution ="
				done
				
				check_ssh_key_link.sh
				#!/bin/bash
				for ip in `cat ip.txt`
				do
					ssh 172.16.1.$ip hostname
				done
				# 脚本传参
					sh *.sh hostname
					sh *.sh "ip a"
				# 脚本的批量管理 -- 串行的方式批量管理
	05. ssh服务配置文件
		/etc/ssh/ssh_config #客户端
		/etc/ssh/sshd_config #服务端
			# ssh中注释的服务，则为默认的服务
			Port 22 -- 服务端口
			ListenAddress 0.0.0.0 -- 监听地址 指定一块网卡能够接受远程访问请求
										ps: 指定监听地址只能是本地网卡上有的地址
			PermitEmptyPasswords no -- 是否允许远程用户使用空密码进行登录，默认是不允许
			PermitRootLogin yes --- 是否允许用户使用root用户远程连接主机，建议改为no，使用sudo命令进行
			GSSAPIAuthentication no --- 是否开启GSSAPI认证功能，不用的时候关闭
			UseDNS no --- 是否开启反向DNS解析功能
		# 当服务出现错误，则将error的信息进行修改
	06. ssh远程服务被入侵的案例
		top
			us sy -- cpu
			id -- 空闲的状态
		1. 用密钥登录，不用密码登录
		2. 牤牛阵法：解决ssh安全问题
			a. 防火墙封闭ssh，指定源ip限制（局域网，信任公网）
			b. 开启ssh只监听本地内网IP（ListenAddress 172.16.1.61）
		3. 尽量不给服务器外网IP
		4. 最小化（软件安装-授权）
			权限最小化安装
			软件最小化安装 -- 减少开放端口数
				服务分散开
		5. 给系统的重要文件或命令做一个指纹
			MD5
			/etc/passwd MD5sum -- 监控
			inotify /usr/bin -- 监控目录
		6. 给他锁上 chattr +i +a
	07. ssh相关的命令总结
		ssh-keygen
		ssh-copy-id
		sshpass
		ssh
		scp
		sftp
			sftp 172.16.1.41
			sftp> help -- 查看命令
				cd -- 切换服务端的目录
				lcd -- 切换本地的目录位置
				lls -- 查看本地目录内容
				get -- 下载内容
					get 待下载数据
				put -- 上传数据
				quit/bye -- 退出ftp连接
		
# 习题
01. 利用脚本实现实时同步
	while循环
02. 如何xshell也是基于密钥方式连接主机
03. 提前安装部署好ansible软件
	yum install -y ansible