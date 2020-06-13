# 课程说明
	nginx的一些常见模块

# 课程回顾
	1. nginx服务一些特定介绍
		a 支持高并发能力比较强 消耗资源少
		b 软件功能比较多样
		c 支持系统平台比较广泛
			可以制作yum仓库
			yum 安装很慢 -- 制作yum仓库 yum源
			1. 下载软件
				vim /etc/yum.conf
				keepcache 1 -- 保存安装包
			2. 客户端访问到制作yum仓库 -- nginx (linux windows)
	2. nginx部署安装
		a yum安装方式
		b 编译安装软件
		nginx -V 看下默认nginx安装时的配置参数
	3. nginx目录结构
	4. nginx配置文件参数说明

# 课程内容
	01. nginx服务的企业应用
		1. 利用nginx服务搭建一个网站（www网站）
			a 编写虚拟主机配置文件
				/etc/nginx/conf.d
				vim www.conf  # nginx.conf文件中规定了导入的文件的类型
				server {
					listen       80;
					server_name  www.oldboy.com;
					location /oldboy {
						root   /usr/share/nginx/html;
						index  oldboy.html;
					}
				}
				ps: location说明
					a 访问www.oldboy.com -- /
						请求行Get / http1.1
						直接到站点目录中找配置文件
						请求找的是 /oldboy 中的./html 目录
						没有指定需要的资源，默认返回首页目录
						
						http://www.oldboy.com/oldboy -- oldboy
						.html/oldboy 目录 -- 在站点目录中是否有相应文件
					location	/oldboy
						
					location /
				location 做一个URI的匹配
					/ -- 表示默认的匹配的URI
						
			b 获取开发人员的代码
			c 重启nginx服务 -- 平滑启动
				systemctl reload nginx
				nginx -s reload # 编译安装时的命令
			ps: nginx命令参数
				nginx -v 查看nginx安装时的拓展模块
				nginx -t 检查配置文件的语法
				nginx -T 测试的同时，并把所有的配置信息打印出来
				-s 是否停止 stop quit reload
			d 编写dns配置信息
				真实域名进行配置：阿里云 -- 域名解析
				模拟域名配置：在windows主机的hosts文件中配置	C:\Windows\System32\drivers\etc
					A 记录
						CNAMe
					主机记录 www
					记录值， 服务器公网地址
					TTL
			e 进行测试访问
				http://www.oldboy.com
		部署搭建网站服务的常见错误：
			hosts 文件错误 -- 系统的设置问题
			01. 网站服务配置文件编写不正确
				404错误
					a 修改nginx配置文件 -- location
					b 在站点目录中创建相应目录或文件数据信息
				403错误
					a 没有默认的首页文件
					b 不要设置禁止访问
			02. DNS配置信息不正确
			03. 配置文件修改一定要重启服务；站点目录中代码文件信息调整，不需要重启服务
	02. 利用nginx服务搭建多个网站 （www bbs blog)
		1. 创建多个虚拟主机的文件
			bbs.conf blog.conf
			www.oldboy.oom
			bbs.oldboy.com
			blog.oldboy.com
			/html/
			index.html
		2. 创建站点目录和首页文件
			for name in {www,bbs,blog};do echo "10.0.0.7 $name.oldboy.com" > /html/$name/index.html; done
		3. 修改访问主机的hosts文件
		4. 进行测试
			1. windows
				通过goole浏览器的无痕浏览模式进行
				或
			2. Linux
				直接通过linux主机进行测试
					curl www.oldboy.com
	3. 企业中虚拟主机访问方式
		多个网页访问：
			通过include的顺序确定
			include       /etc/nginx/mime.types;
		a 基于域名的方式访问
		b 基于地址的方式进行访问	--- 负载均衡 + 高可用服务
			只能通过指定的地址访问
			1. 修改conf.d文件中
				listen		10.0.0.7:80	# 只能通过
			2. 只要涉及到地址修改时
				必须restart不能reload
			
		c 基于端口的方式进行访问	--  zabbix服务(apache)等需要web访问的端口
			listen	8080;
			
		页面访问原理
			01. 将域名进行解析	www.oldboy.com --- 10.0.0.7
			02.	建立tcp的连接（四层协议）
				10.0.0.7	目标端口 80
			03. 根据应用层http协议发出请求
				请求报文: hosts www.oldboy.com 
			04. 没有相同域名的server主机，会找相同端口的
				显示主机的网站页面
	03 企业中网站的安全访问配置
		a 根据用户访问的地址进行控制
			10.0.0.0/24 www.oldoby.com/AV 不能访问
			172.16.1.0/24 www.oldboy.com/AV -- 在站点目录中找AV目录 可以访问
			
			nginx 阻止访问模块：
				ngx_http_access_module
					举例说明
					location / {
						deny  192.168.1.1;
						allow 192.168.1.0/24;
						allow 10.1.1.0/16;
						allow 2001:0db8::/32;
						deny  all;
					}
				指令的用法
					Syntax:	deny address | CIDR | unix: | all;
					Default:	—
					Context:	http, server, location, limit_except
				1. 编写配置文件
					location /AV {
						deny 10.0.0.0/24;
						allow 172.16.1.0/24;
					}
					
					先找location /AV
					然后找站点目录
					--- 遇到的问题
						访问出现404
						解决方法
						将站点目录放成全局
						root ... 
						index ...
				补充:
					location外面的信息，全局
					location内部的信息，局部
			
		b 根据用户进行访问认证
			ngx_http_auth_basic_module
			举例配置
				location / {
					auth_basic           "closed site"（验证窗口提示内容）;		-- 开启认证功能
					auth_basic_user_file conf/htpasswd;		-- 加载用户密码文件
				}
			1. 编写虚拟主机配置文件
				location / {
					auth_basic           "说明文件";		-- 开启认证功能
					auth_basic_user_file password/htpsswd(相对路径) 认证密码文件;		-- 加载用户密码文件
				}
			2. 创建密码文件
				文件中密码信息必须是密文的
				htpasswd # yum install -y httpd-tools
				htpasswd
					参数
						 -c  Create a new file.
							创建一个新的密码文件
								htpasswd -c ./newfile user
						 -n  Don't update file; display results on stdout.
							不更新密码文件，只显示密码信息
						 -b  Use the password from the command line rather than prompting for it.
							免交互输入密码信息
								htpasswd -bc ./newrile user password
						 -i  Read password from stdin without verification (for script usage).
							读取密码信息，通过
						 -m  Force MD5 encryption of the password (default).
							使用md5的加密算法
						 -2  Force SHA-256 crypt() hash of the password (secure).
						 -5  Force SHA-512 crypt() hash of the password (secure).
						 -B  Force bcrypt aencryption of the password (very secure).
						 -C  Set the computing time used for the bcrypt algorithm
							 (higher is more secure but slower, default: 5, valid: 4 to 31).
						 -r  Set the number of rounds used for the SHA-256, SHA-512 algorithms
							 (higher is more secure but slower, default: 5000).
						 -d  Force CRYPT encryption of the password (8 chars max, insecure).
						 -s  Force SHA-1 encryption of the password (insecure).
							
						 -p  Do not encrypt the password (plaintext, insecure).
							不进行加密
						 -D  Delete the specified user.
							删除指定用户
							htpasswd -bc ./newrile user
						 -v  Verify password for the specified user.
				修改密码文件权限:
					最好把权限改为600
					-- 直接访问文件出现500错误
						1. 内部程序代码编写有问题
						2. 文件权限不正确 
							浏览器 -- nginx服务器（接收认证请求）www用户 -- htpasswd
								修改密码文件属主
								chown www ./htpasswd
				curl -u oldboy:centos www.oldboy.com
3 课程总结
	1. 如何搭建一个网站（服务器 域名 网页代码 数据库支持）
	2. 如何搭建多个网站
	3. 如何访问网站（3种 域名 地址 端口）
	4. 网站服务安全配置
		根据用户访问域名