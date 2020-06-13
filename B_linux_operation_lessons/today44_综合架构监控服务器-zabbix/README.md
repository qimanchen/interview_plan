# 课程介绍
	1 662 824 525
	1）综合架构监控服务概念说明
	2）综合架构服务器如何监控
		a 手动执行命令进行监控	df w top ps netstat
		b 自动执行命令进行监控	shell脚本
	3）综合架构监控体系结构
		你的原公司是如何对架构服务器进行监控
	4）综合架构监控服务软件 -- zabbix
		a zabbix软件结构组成
		b zabbix软件安装步骤(LAMP) wordpress 网站页面部署 （LNMP)
		c zabbix软件初始监控
	5）综合架构监控服务详细配置
		a zabbix软件功能组成
		b zabbix软件功能实现
# 课程回顾
	1. 综合架构高可用服务
	2. 综合架构高可用服务部署（配置）keepalived heartbeat
	3. 综合架构高可用服务原理 vrrp
	4. 综合架构高可用服务应用
		a 解决脑裂问题
		b 释放资源
		c 双主问题
		d 访问安全问题
	keepalived配置文件中
		global_defs {
		   router_id lb01
		}
		
		vrrp_script check_web { -- 
			script "/server/scripts/check_web.sh"  -- 定义要监控的脚本（绝对路径，脚本具有执行权限）
			interval 2	-- 执行脚本的间隔时间（秒）
			weight 2	-- 查询这个服务
		}  -- 放置到全局和vrrp中间
		# weight参数：权重参数，主要用于和优先级进行运算
			1. 求和运算：weight数值必须为正数，weight + priority 自动提升优先级，使得主机可以成为主服务器
			2. 求差运算：weight数值必须为负数，weight - priority 自动降低优先级，使得主机可以成为备用服务器
		运行一个脚本，执行脚本结束后，脚本的执行脚本可以为真 看脚本执行返回值 $?==0
			if [ conditions ]; then
				exit 0 # 为真 -- 指定脚本的返回值
			else
				exit 1 # 为假
			fi
		运行一个脚本，执行脚本结束后，脚本的执行脚本可以为假 看脚本执行返回值 $?<>0
		
		如何，结合weight和脚本真假
			a 权重值为正数
				vrrp_script
				1. 脚本运行后为真 weight + priority
				2. 脚本运行后为假 priority
				wireshark 抓包测试 --  查看priority
					
			b 权重值为负数
				1. 脚本运行后为真 priority
				2. 脚本运行后为假 weight - priority
				wireshark 抓包测试
		# 可以通过设置weight自动监控资源的状况，不会关闭keepalived服务
			weight -60 -- 脚本执行为假执行求差
			#!/bin/bash
			netstat -tunlp | grep ":80"
			if [ $? == 0 ];then
				exit 0
			else
				exit 1 -- nginx 停止做求差运算，改变优先级值
			fi
		vrrp_instance oldboy {
			state MASTER
			interface eth1
			virtual_router_id 51
			priority 150
			advert_int 1
			authentication {
				auth_type PASS
				auth_pass 1111
			}
			virtual_ipaddress {
			192.168.90.90
			}
		}
# 课程内容
	03. 综合架构监控服务概念说明
		a 掌握架构服务的运行情况
		b 用于分析公司网站运行情况
	04. 综合架构服务器监控常用命令
		CPU: top, htop 
		%Cpu(s):  6.7 us,  6.7 sy,  0.0 ni, 86.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
			1. us: user state 用户态信息
			2. sy: system state 内核态信息 Mysql进程
			3. id：idle 空闲状态
			用户态 --- 用户下达的命令
			内核态 --- 内核调配任务处理
			-- 优先处理用户态的工作
			cpu的任务切换 -- 上下文切换
		内存： top free
			              total        used        free      shared  buff/cache   available
			Mem:           991M         89M        773M        6.7M        128M        757M
			Swap:          2.0G          0B        2.0G
			-- dd测试 dd if=/dev/zero of=/dev/1G bs=100M count=10
			监控：内存可用率，swap使用率
		磁盘：df -h，iotop （检查磁盘io消耗）
			监控：磁盘使用情况,io消耗的情况
		-- 电脑卡，io cpu
		网络：iftop
			监控：网络带宽使用情况
		进程 top ps htop
			监控：占用内存情况 tomcat（java）-- 内存占满（内存溢出）-- 服务出现僵死（重启服务，做java优化）
			占用cpu情况
			-- 空闲 id 高于50%
		负载 w top uptime glances
			监控 10分钟和15分钟负载 -- 小于cpu内核数量
		- yum install -y glances
	05. 综合架构监控服务编写脚本
		- 练习题
			01. 如何监控内存使用情况
				正常：可使用率80%
				异常：可使用率20%
				free | awk 'NR==2{print int($NF/$2)}'  -- 取整数
			02. 如何监控服务运行状态
				ps -ef | grep -c nignx
				netstat -tunlp | grep port
				ps:tomcat服务 --- 僵死 -- 需要模拟用户访问一下
	06. 综合架构监控服务体系结构
		a 硬件
			服务器 路由器 交换机 防火墙（SNMP）
		b 系统监控
			CPU 内存 磁盘 网络 进程 TCP
		c 服务监控
			nginx php tomcat redis memcache mysql
		d 网站监控
			请求时间 响应时间 加载时间 页面监控
		e 日志监控
			ELK (收集 存储 分析 展示）日志易
		f 安全监控
			Firewalld（4层和4层以上） WAF(nginx+lua)（应用层面） 安全宝 牛盾云 安全狗
		g 网络监控
			smokeping 监控宝 站长工具 奇云测 多机房
		h 业务监控（数据库信息）
			活动产生多少流量 产生多少注册量 带来多少价值
	07. zabbix监控服务说明 -- Nagios(系统监控） Cacti(流量监控）Prometheus（容器）
		a 结构组成
			zabbix_server -- zabbix_agent -- zabbix_web服务(apach) -- zabbix_proxy + 数据库
			zabbix_server: 监控服务端
			zabbix-agent: 监控客户端
			zabbix-web:监控网站服务
			php: 处理动态请求
			mysql:数据库存储监控数据
			zabbix-proxy: 负责收集agent信息汇总告知zabbix-server
		b zabbix软件安装部署过程
			服务端
				1. 下载安装zabbix yum 源文件
					LTS
					官方源
					rpm -ivh 下载源
					aliyum zabbix yum 源
					清华源
						rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/zabbix/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
						
						# 官方源存在问题，切换为阿里源
						rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
						sed -i "s@zabbix/.*/rhel@zabbix/4.0/rhel@g" /etc/yum.repos.d/zabbix.repo
						sed -i 's@repo.zabbix.com@mirrors.aliyun.com/zabbix@g' /etc/yum.repos.d/zabbix.repo
				2. 安装zabbix软件
					zabbix-server-mysql -- 服务
					zabbix-web-mysql httpd php web服务
					mariadb-server
					yum install -y zabbix-server-mysql zabbix-web-mysql httpd php mariadb-server
				3. 软件配置
					vim /etc/zabbix/zabbix_server.conf
					126 DBPassword=zabbix
					vim /etc/httpd/conf.d/zabbix.conf
					21 php_value date.timezone Asia/Shanghai
				4. 编写配置数据库服务
					systemctl start mariadb
					systemctl status mariadb
					创建zabbix数据库-zabbix
						create database zabbix character set utf8 collate utf8_bin;
					创建数据库管理用户
						grant all privileges on zabbix.* to zabbix@localhost identified by 'zabbix';
					在zabbix数据库中导入相应的表信息
						zcat /usr/share/doc/zabbix-server-mysql-4.0.20/create.sql.gz | mysql -uzabbix -pzabbix zabbix
						# 插入数据报错
							[root@m01 yum.repos.d]# zcat /usr/share/doc/zabbix-server-mysql-4.0.20/create.sql.gz | mysql -uzabbix -pzabbix zabbix
							ERROR 1118 (42000) at line 1278: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline.
						# 解决方法
							在/etc/my.conf.d/server.conf
							[mysqld]
							innodb_strict_mode = 0
						zgrep 从压缩文件中过滤数据
				5. 启动zabbix程序相关服务
					数据库 zabbix httpd
					systemctl start zabbix-server.service httpd mariadb.service
					systemctl start zabbix-server.service httpd mariadb.service
					
					LAMP: apache(php模块） mysql 不需要启动服务
				6. 登录zabbix服务端web界面，进行初始化配置
					http://192.168.90.61/zabbix/setup.php
					chown -R apach 
					
					10051 zabbix-server 服务端端口号
					10050 zabbix-agent 客户端端口号
					/etc/zabbix/web/zabbix.conf.php -- 记录web页面初始化信息
				7. 登录zabbix服务web页面
					用户名：Admin
					密码：zabbix
					
			客户端
				1. 下载yum源
					rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/zabbix/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
					
					# 官方源存在问题，切换为阿里源
						rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
						sed -i "s@zabbix/.*/rhel@zabbix/4.0/rhel@g" /etc/yum.repos.d/zabbix.repo
						sed -i 's@repo.zabbix.com@mirrors.aliyun.com/zabbix@g' /etc/yum.repos.d/zabbix.repo
				2. 安装zabbix软件
					yum install -y zabbix-agent
				3. 编写zabbix客户端配置文件
					vim /etc/zabbix/zabbix_agentd.conf
					98 Server=172.16.1.61
				4. 启动zabbix-agent服务
					systemctl start zabbix-agent
					netstat -tunlp | grep 10050
	08. 实现zabbix默认第一台主机的监控
		1. 配置 -- 主机 -- 创建主机（创建要监控的主机）
		2. 配置监控的主机
			主机信息中：名称 主机组 监控的主机地址
			模板信息中：指定需要链接的模板信息
		3. 保存退出，进行监控检查
			检查主机有没有变绿
			检测 -- 最新数据 -- 主机（选择出
		-- 监控项
			Agent ping -- ping主机
			available memory -- 内存
	09. 实现zabbix自定义配置监控
		1. 监控项: 自定义监控收集主机的信息
			- 监控nginx服务是否启动
			1) 在zabbix-agent进行配置文件编写
				a 编写自定义监控命令
					netstat -tunlp | grep nginx
					ps -ef | grep [n]ginx
				b zabbix-agent配置文件
					UserParameter
						zabbix-agentd.conf 中修改
						/etc/zabbix/zabbix_agentd.d/web_server.conf
					格式：
						UserParameter=键（变量名），值（变量信息）
						UserParameter=ps -ef | grep -c [n]ginx
				c 重启zabbix-agent服务
			2) 在zabbix-server命令进行操作
				a 检测自定义监控信息是否正确
					yum install -y zabbix-get
					zabbix_get -s 172.16.1.17 -k 'web_state' # key值名称必须与zabbix-agent中配置的一样
						-s 访问的地址必须在agent中配置的项
						参数说明：
							-s 指定监控的主机
							-k 指定要查看的键的值
			2) 在zabbix-server网站页面进行配置
				a 进入到创建监控项页面
					配置 -- 主机 -- 监控项
				b 进行配置
					名称 -- 任意
					类型 -- 不要改
					键值 -- web_state
					单位（对应参数的单位） -- 命令返回值
					更新间隔 -- 3s
					自定义时间间隔 -- 在上面更新间隔基础上单独设置的时间间隔
					历史数据保留时长 -- 90d
					趋势存储时间 -- 365d
					新的应用集 -- 分类处理 server_status
					-- 直接添加 -- 状态
				c 检查是否搜寻到对应的信息
		-- 监控远程服务是否正常启动	
			 ps -ef | grep -c [s]shd -- 进程的个数
		-- 自定义监控项没有指定信息
			管理 -- general -- other -- refresh unsupported items 设置监控项刷新时间
		2. 应用集：将多个类似的监控项进行整合 便于查看检查
		3. 模板：将多个监控项 触发器 图形都配置在模板中，方便调用配置
			-- 多台主机的配置
				1. 创建模板
				2. 所有的监控项写在模板中，类似的监控项 -- 可以直接克隆实现
		4. 动作		指定将报警信息发送给谁/定义报警的信息/定义报警的类型（邮件
			条件：
				触发器的条件 -- 如何指定了触发器，不指定，所有的都不触发
			操作：
				默认持续时间 -- 持续问题存在的时间
				默认标题 -- 宏 -- 查看zabbix官网
				操作 -- 多个阶段
				仅送到 -- 选定媒介
		5. 触发器：可以实现报警提示（条件表达式），默认页面提示报警
		6. 图形
			配置 -- 图形
			-- 创建图形 -- 将多个数据聚合到一起
			聚合图形 -- 多个图形放到一个现实面板上
				
		7. 报警媒介 定义报警的方式
	10. 自定义监控多个服务
		# 定义一个模板
			UserParameter=server_state[*],netstat -tunlp | grep -c $1
			UserParameter=server_state[*],ps -ef | grep -c $1
				测试 server_state[nginx]
		# 测试
			zabbix_get -s 172.16.1.17 -k 'server_state[22]' 传参
			-- 出现这个错误的问题
				(Not all processes could be identified, non-owned process info will not be shown, you would have to be root to see it all.)
			netstat 命令执行通过普通用户执行时，导致的错误
			
		# 修改配置页面
			键值： server_state[22]
	11. 实现zabbix报警功能 -- 触发器/动作
		报警方式：
		01. 页面提示信息报警（值班运维）
		02. 页面声音提示报警
		03. 邮件信息报警
		04. 微信功能报警
		05. 短信报警/电话报警
		
		- 页面提示和声音报警实战
			1. 创建触发器
				配置 -- 触发器 -- 选择相应监控主机触发器 --- 创建触发器
				名称： -- server_state_trigger
				严重性： -- 
				表达式：-- 添加 -- 根据选择进行
				{监控主机名称:键值名称.调用的表达式函数}<=2
				{web01:server_state[nginx].last()}<=2
				-- 表达式总结
					last()	收集到的最新信息
					max()	在一定周期内，收集到的最大值
					min()	在一定周期内，收集到的最小值
					diff() 	在一定时间内，判断收集的信息是否不同 -- 文件的md5值
						<> 不等于0
					change() 在一定时间内，判断收集的信息是否不同
					avg()	取一段时间的平均值 -- 负载，服务器温度
			2.	页面报警
				企业工作遇见告警信息处理思路步骤
					a 看到告警提示信息，定位主机信息
					b 看到主机信息之后，定位报警原因 获得监控项key值
					c 根据key值获得对应的参数，然后定位到对应的配置的值
				-- 主要关注严重的级别
			3.	声音告警，修改网页配置，有提示声音报警
				小人头 -- 前端信息中 -- 播放声音
				- 通过web界面添加对应的声音
				PS：如何修改报警铃声
					1. 找到文件所在目录（在站点目录中找）
						find
						- 可以通过修改对应的php文件
					2. 将原有声音文件做替换
					3. 需要清除缓存，进行配置
				- 网页上的东西一定在站点目录上，通过修改代码和对应的文件进行修改对应的告警声音
				zabbix配置中添加声音文件
			4. 邮件报警
				a 修改动作配置
					配置 -- 动作 -- 将默认动作启用
				b 建立和163邮箱服务关系
					管理 -- 报警媒介类型 -- 创建报警媒介
						名称： email_163
						smtp helo 163.com
						ps: 密码设置的需要是指定的邮箱认证密码
				c 定义接收报警的邮件地址
					小人头 -- 报警媒介 -- 设置收件人信息
						类型
						收件人
					注意更新配置
						
			5. 微信报警
				a 需要注册企业微信，并进行配置
					我的企业 -- 获取企业id --二维码 -- 添加成员
						企业ID wwc4aeeb2e6b2ef06d
						企业名称 Qiman_Fast
						
					管理工具 -- 审核通过
					应用小程序 -- 创建应用 -- 应用名称
						AgentId 1000002
						Secret m81zpd9JH4HsBlRn6vSucJB5ZF4vpFPV8zt7lAx0Ncw
						收集：AgentId，Secret
				b 编写脚本 -- python
					zabbix-server.conf -- AlertScrisPath -- 设置放置告警脚本
						weixin.py  -- chmod +x weixin.py
					执行脚本：pip install -y python-pip
				c 修改添加报警媒介 -- 定义了发微信的配置
					类型：脚本
					脚本名称：wenxin.py
					参数：脚本传参的参数
						ALERT.SENDTO
				d 定义添加的人
					报表 -- 动作日志
			6. 短信和电话：
				1. 利用第三方短信电话报警平台
					阿里大鱼
				2. 利用onealert发送
					a 配置报警平台
						-- zabbix脚本 -- 将对应的脚本添加到告警脚本中
					管理用户： http://192.168.90.61/zabbix
	# 总结
		报警媒介 -- 动作（报表 -- 动作日志） -- 触发器（问题） -- 监控项（设置 agentuserparamenter） --图形（多个监控项图形进行整合）
		
		创建监控主机 -- 链接模板
		自动发现 -- 
# 课程总结
	1. 架构监控服务概念说明
	2. 架构监控服务命令说明
	3. 架构监控服务脚本编写
	4. 架构监控服务体系说明
	5. 架构监控服务组成部分
	6. 架构监控服务部署安装 zabbix-server
# 练习