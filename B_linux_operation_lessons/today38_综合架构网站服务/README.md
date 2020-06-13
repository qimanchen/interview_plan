# 课程说明
	1. 常见的网站服务
	2. nginx网站服务特点
	3. nginx服务部署安装 yum
	4. nginx目录结构介绍 (站点目录)
	5. nginx配置文件默认参数说明
	6. nginx实现简单网站搭建（html代码）
	7. nginx服务一些常见应用（模块功能）
# 课程回顾
	1）用户访问网站流程
	2）http协议的报文结构
	3）报文结构中重点内容
		请求方法 get post
		协议版本 1.0 1.1 2.0
		状态码
	4）网站资源信息
		URL URI
		静态资源
		动态资源	LNMP架构
		伪静态资源
	5）网站评测指标
		IP
		PV
			统一那个页面访问的人数更多，取出前10名
		UV
			根据用户访问的cookie信息，统计访问的用户数量
		网站并发：
			单位时间内同时处理的请求数 ab
		如何统计，一个页面（www）一天访问网站最多的前10个地址 （awk数组功能，sort uniq）
			- awk数组
				cat test.txt |awk '{a[$1]+=1;} END {for(i in a){print a[i]" "i;}}'
				a 数组中数据为a[ip] 出现的次数 key:value
				for循环格式 { for i in a print a[i] i }
		access.log -- 访问用户源地址信息
# 内容
	01. 常用的网站服务
		处理静态的网站服务
			apache http://apache.org/
				yum install -y httpd
			nginx http://nginx.org
				具有高并发 -- 特别是静态资源
				还具有反向代理负载均衡功能和缓存服务功能
				跨平台使用
		处理动态资源的服务
			php: php.net 终端浏览器进行访问
			Tomcat: java 利用移动端查看网页
			python		开发难度较低
	03. nginx服务的软件特点
		1）高并发，消耗内存资源少
		2）具有多种功能
			网站web服务功能 -- apache
			网站负载均衡 -- lvs
			网站缓存服务 -- squid
		3）在多种系统平台都可以进行部署
		4）nginx实现网络通讯时使用的是异步网络IO模型：epoll模型 （apache -- select 模型）
			epoll模型：事件注册 随着连接数增加网站性能变化不大
			select模型：轮询
	04. nginx软件的安装部署过程
		两种安装方式
			01. yum安装软件
				a 使用官方yum源进行安装 安装的是最新版本 软件目录结构比较标准
				b 使用非官方yum源进行安装 目录结构会产生变化
			02. 编译安装软件
				-- 总结nginx编译安装的过程
				1. wget 软件包
					ps:安装前解决依赖 openssl-devel pcre-devel
				2. 解压下载好的软件
					tar -xzvf 
				3. 进入软件目录
					编译安装三部曲
						a 进行配置操作
							./configure
							--prefix=path 设置安装目录
							--user=USER 设置一个虚拟用户管理worker进程
							--with 开启模块
							--without 关闭模块
						b 进行软件的编译过程
							make 编译 -- 将程序转换为机器码
						c 安装
							make install
		yum官方源安装
			1. 更新nginx官方源
				http://nginx.org/en/linux_packages.html#RHEL-CentOS
				vim /etc/yum.repos.d/nginx.repo
			2. yum安装nginx软件
				yum install -y nginx
				echo $? -- 查看上一条指令执行是否成功
			3. 启动nginx服务，检查是否安装正确
				systemctl start nginx
				测试访问网站服务
				10.2.0.17
	04. 查看软件的目录结构
		/etc/logrotate.d
			实现nginx日志文件定时切割处理
			日志切割方法：
				1. 利用脚本进行切割处理
					#!/bin/bash
					mv /var/log/nginx/access.log /var/log/nginx/access_$(date +%F).log
					systemclt restart nginx
				2. 利用专用文件切割程序 -- logrotate
					/etc/logrotate.conf
					
					# rotate log files weekly
					weekly			-- 定义默认切割日志的周期，daily monthly

					# keep 4 weeks worth of backlogs
					rotate 4		-- 定义只保留几个切割后的文件

					# create new (empty) log files after rotating old ones
					create			-- 创建出一个相同的源文件

					# use date as a suffix of the rotated file
					dateext			-- 定义角标信息(扩展名）

					# uncomment this if you want your log files compressed
					#compress		-- 是否对切割后的文件进行压缩处理

					# RPM packages drop log rotation information into this directory
					include /etc/logrotate.d	-- 加载包含该目录中的文件配置

					# no packages own wtmp and btmp -- we'll rotate them here
					/var/log/wtmp {		单独对某个文件进行切割配置
						monthly
						create 0664 root utmp
						minsize 1M 		-- 文件大小
						rotate 1
					}

					/var/log/btmp {
						missingok
						monthly
						create 0600 root utmp
						rotate 1	-- 备份文件数量
					}
					# system-specific logs may be also be configured here.
					sharedscripts
					postrotate -- 执行切割后的处理
							if [ -f /var/run/nginx.pid ]; then
									kill -USR1 `cat /var/run/nginx.pid` -- 平滑的启动
							fi
					endscript
		/etc/nginx/mime.types -- 可以加载的文件
		总结：
			/etc/nginx 配置文件
			/var/log/nginx 日志文件
			/usr/bin/nginx nginx命令文件
			/usr/share/nginx/html 站点目录
				图片	附件信息	视频	音频
	05. nginx服务配置文件
		ps -ef | grep nginx
			存在两个进程 master和worker
		/etc/nginx/nginx.conf --- 主配置文件
			1. 配置文件主区域配置
			user  nginx;  -- 定义worker进程管理的用户
			改为 www
				ps:nginx的进程
					master -- 主进程 -- 管理服务是否能够正常运行 -- root用户管理
					worker -- 工作进程 -- 处理用户的访问请求 -- 普通用户的管理
			worker_processes  1;		-- 定义有几个worker进程 == CPU核数/核数的两倍
			error_log  /var/log/nginx/error.log warn;	-- 定义错误日志路径信息
			pid        /var/run/nginx.pid;		-- 定义pid文件路径信息
			
			2. 配置文件事件区域
			events {
				worker_connections  1024;		-- 一个worker进程可以同时接收1024个访问请求
			}
			
			3. 配置http区域
			http {
				include       /etc/nginx/mime.types;		-- 加载一个配置文件
				default_type  application/octet-stream;		-- 指定默认识别文件类型
				log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
								  '$status $body_bytes_sent "$http_referer" '
								  '"$http_user_agent" "$http_x_forwarded_for"';
								--- 定义日志的格式
				access_log  /var/log/nginx/access.log  main;	-- 指定路径信息， main 引用上面的那个日志格式
				sendfile        on;
				#tcp_nopush     on;
				keepalive_timeout  65;			-- 超时时间
				#gzip  on;						-- 
				include /etc/nginx/conf.d/*.conf;			-- 加载一个配置文件
			}

		/etc/nginx/nginx.d/default --- 扩展配置文件（虚拟主机配置文件）
			4. 第四个部分 server区域信息，配置一个网站 www/bbs/blog -- 一个虚拟主机
				更新缓存
					1. 清除浏览的缓存的数据
					2. 
			server {
				listen       80;			-- 指定监听端口
				server_name  localhost;		-- 指定网站域名，需要dns解析
				location / {
					root   /usr/share/nginx/html;	-- 定义站点目录
						想要的文件 -- 站点目录 -- root 指定的站点目录
					index  index.html index.htm;	-- 定义首页文件
						未指定想要的文件，返回首页文件
				}
				error_page   500 502 503 504  /50x.html;		-- 优雅显示页面信息
				# 防止直接显示404错误
				location = /50x.html {
					root   /usr/share/nginx/html;
				}
			}
# 课程总结
	1. 常用的网站web服务 （静态请求 动态请求）
	2. nginx服务的特点 apache
	3. nginx软件安装部署 yum 官方源
	4. nginx重要目录结构
	5. nginx服务配置文件默认参数
作业：
01. 熟悉排序和去重命令，对文件数值信息进行统计分析
02. 如何对网站进行压力测试