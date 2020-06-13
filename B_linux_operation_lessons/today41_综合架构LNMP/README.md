# 课程介绍
	1. LNMP架构的组成 (作用)
	2. LNMP架构的部署
	3. LNMP通讯原理
	4. LNMP服务之间如何建立管理
		nginx + php 运维负责
		php + mysql 开发负责
	5. 运维人员代码上线 （www bbs blog)
	6. NFS服务和web服务
		mysql服务和web服务（企业案例：数据库迁移方法）
		补充：企业经验总结（简历项目）
		01. 全网备份项目（项目背景 项目实施 项目时间）
		02. 实时同步项目
		03. 网站服务自动化 （网站服务自动化部署 网站应用自动化部署）ansible
		04. 网站LNMP环境搭建
		05. 数据库迁移项目

# 课程回顾
	1. nginx服务的企业应用（nginx模块）
		a 实现网站页面目录索引功能（yum仓库搭建）
		b 实现网站访问别名功能
		c 实现网站页面用户访问监控
		d 实现网站服务日志功能配置
			自动化分析日志 ELK
		e 根据用户访问uri进行匹配处理
			location =  精确匹配
			location ^~ 优先匹配
			location ~
			location ~* 不区分大小写
			location uri 根据uri匹配
			location / 默认匹配
		f 网站页面跳转功能
			rewrite 匹配地址 跳转成什么地址
			return 
# 课程内容
	01. 网站的LNMP架构是什么
		L -- linux系统
			ps:selinux关闭，防火墙关闭
			/tmp 1777 mysql服务无法启动
		N -- nginx服务部署
			作用：用于处理用户的静态请求
		P -- php服务部署
			作用：
				1. 处理动态的页面请求
				2. 负责和数据库建立关系
		M -- Mysql服务部署
			MariaDB
			作用：存储用户的字符数据
	02. 网站的LNMP架构部署
		nginx服务 -- ansible一键化部署
		mysql服务部署：
			1. 安装数据库软件
				curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
				yum -y install mariadb mariadb-server
			2. 数据库初始化过程
				mysql_install_db 
				--basedir=path       The path to the MariaDB installation directory.
					程序目录
				--datadir=path       The path to the MariaDB data directory.
					指定数据信息保存的目录
				--user=mysql 指定用户管理数据
				创建密码
					mysqladmin -u root password 'new-password' -- 给本地数据库设置密码
					mysqladmin -u root -h web01 password 'new-password' -- 给远程数据库设置密码
					
			2. 启动数据库服务
				systemctl start mariadb.service
				systemctl enable mariadb.service
			3. 给mysql数据库服务设置密码
				mysqladmin -u root password 'centos' -- 设置密码（仅仅是设置密码，不能重置密码）
		php服务部署
			1. 更新yum源/卸载系统自带的php软件
				yum remove php-mysql php php-fpm php-common
				rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
				rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
			2. 安装php软件	
				yum -y install php71w php71w-cli php71w-common php71w-devel php71w-embedded php71w-gd php71w-mcrypt php71w-mbstring php71w-pdo php71w-xml php71w-fpm php71w-mysqlnd php71w-opcache php71w-pecl-memcached php71w-pecl-redis php71w-pecl-mongodb
				
				yum install php71w php71w-cli php71w-common php71w-devel php71w-embedded php71w-fpm php71w-gd php71w-mbstring php71w-mysqlnd php71w-opcache php71w-pdo php71w-xml
			3. 编写配置文件
				/etc/php-fpm.d/www.conf
					user = www
					group = www
				ps:保证nginx进程管理用户和php的管理用户保持一致
			4. 启动php服务
				systemctl start php-fpm
				systemctl enable php-fpm
	03. LNMP的原理
		nginx + php + mysql
		
		用户 -- 访问网站	
				1. 静态资源		-- nginx直接返回需求
				2. 动态资源 -- mime.typs中无法直接处理
					-- fastcgi_pass (FastCGI接口) -- php server（fastcgi 通用网关接口)
												-- php-fpm.conf（wrapper处理）--- php.ini（解析） -- mysql
	04. 实现LNMP之间建立关系
		1. 实现nginx + php 建立关系
			编写配置文件
				/etc/nginx/conf.d/blog.conf
				location ~ \.php$ {
					root /html/blog; -- 站点目录
					fastcgi_index index.php;	-- 首页文件
					fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
						-- 			url 		uri 确保访问的信息url和uri处理后的消息能够发送到访问的用户
					fastcgi_pass 127.0.0.1:9000; -- 服务端口
					include fastcgi_params;
				}
			重启nginx服务
			2. 编写动态资源文件
				index.php
			3. 进行访问测试
				blog.oldboy.com/index.php
		2.实现php和数据库建立关系
			php + mysql
			test_mysql.php
			<?php
			$servername = "localhost";
			$username = "root";
			$password = "centos";
			//$link_id=mysql_connect("主机名", "用户", "密码");
			//mysql -u 用户 -p密码 -h主机
			$conn = mysqli_connect($servername, $username, $password)s;
			if ($conn) {
					echo "mysql successful by oldboy !\n";
			} else{
					die("Connection failed: ", mysqli_connect_error());
			}
			?>
	05. 部署搭建网站 -- 代码上线
		1. 获取代码信息（git) -- 使用开源的网站代码
			www网站页面 -- dedecms -- 织梦
			bbs网站页面 discuz.net 
			blog网站页面 wordpress
			知乎的网站页面 wecenter
		2. 将代码解压，将解压后的目录放到站点目录中
			tar xf wordpress
			PS：站点目录之前需要进行备份
		3. 修改站点目录权限
			chmod -R www.www blog -- 权限不正确会导致无法连接到服务
		4. 网站初始化
			blog.oldboy.com/index.php
			表前缀设置
		5. 对数据库服务进行配置
			create database wordpress; -- 创建数据库
			show databases;
			创建用户
				wordpress
				# 用户授权
				grant all on database.* to 'wordpress'@'localhost'identified by 'centos'
			mysql.user 中存储了用户的信息
			mysql> use wordpress;
		6. 发布博文
			显示403错误 -- 默认后面没有指定访问内容，则通过默认访问主页来进行访问
			/etc/nginx/conf.d/blog.conf
				index index.php
			-- 切换wordpress主题
				将文件上传至 blog站点目录中的wp-contents/themes/中
# 练习
	01.上传主题 -- 提示上传文件过大如何解决(413) -- nginx中需要添加一个指令
		/etc/nginx/conf.d/blog.conf 中对应虚拟主机里设置变量
		nginx.conf
			client_max_body_size 20M;
		/etc/php.in -- 修改上传文件大小限制
		php.ini
			upload_max_filesize = 20M
	02. 图片保存到服务器什么位置 -- 如何将图片保存到存储服务器中
		# 上传的文件
		http://blog.oldboy.com/wp-content/uploads/2020/05/logo_img-3.png
		wp-config.php 文件 -- 修改文件上传到存储服务器的共享目录中
		define( 'WP_CONTENT_DIR', '/home/lyblog/public_html/my_content' );
		define( 'WP_CONTENT_URL', 'http://域名道/user_content' );
	03. 数据库服务安装在web服务器本地有没有问题
	04. 如何将数据库数据迁移到指定服务器中
	05. nginx反向代理负载均衡
	06. keepalived高可用服务
	07. zabbix监控服务
# 课程总结
	
		