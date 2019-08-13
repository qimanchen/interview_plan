# LNMP -- Linux + nginx + mysql + php 的安装

# 删除已安装的nginx
# $ sudo apt-get purge nginx

# 若用源码安装
# nginx的依赖表
# 注意版本问题
# ssl -- 需要openssl库
# gzip -- 需要zlib库
# rewrite -- 需要pcre库

# LNMP中各自的角色
"""
# Linux -- 平台
# Nginx高性能HTTP和反向代理服务器
	安装方式
		1. apt-get
			$ sudo apt-get update
			$ sudo apt-get install -y nginx
			如果安装失败可以尝试更新一下源
		2. 源码
			a. 将nginx源代码解压编译安装好
				最好把源代码放在/usr/local/src文件夹中
	# 1. 启动
	sudo /etc/init.d/nginx start
	or
	sudo service nginx start
	# 打开http://localhost测试
	# 2. 停止
	sudo /etc/init.d/nginx stop
	or
	sudo service nginx stop
	# 3. 重启
	sudo /etc/init.d/nginx restart
	or
	sudo service nginx restart

	
	# 初级配置
	sudo vim /etc/nginx/sites-avaliable/default
	修改54行位置，添加location ~ \.php的文件
	# 测试配置文件
	并修改
	添加：
	root /usr/share/nginx/html;
	fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
	sudo nginx -t # 测试成功会显示出来
	
	# 重新载入文件
	sudo service nginx reload
"""
# M
"""
安装mysql
sudo apt-get install mysql-server mysql-client

sudo service mysql start # 启动mysql 用户名为root，密码为空

# 配置mysql
sudo vim /etc/myql/my.cnf
将bind-address=127.0.0.1注释掉，允许远程连接
"""
#P
"""
nginx 本身不能处理 PHP，它只是个 web 服务器，
当接收到请求后，如果是 php 请求，
则发给 php 解释器处理，并把结果返回给客户端。

php-fpm 是一个守护进程（FastCGI 进程管理器）
用于替换 PHP FastCGI 的大部分附加功能，
对于高负载网站是非常有用的

# sudo apt-get install -y php5-fpm
# sudo vim /usr/share/nginx/html/phpinfo.php # 设置php文件
# sudo service php5-fpm start # 启动php5-fpm服务
http://localhost/phpinfo.php -- 页面访问


# 想让php支持mysql还需要安装对应的
$ sudo apt-get install php5-mysql
重启php
sudo service php5-fpm restart

#改变监听端口
改变nginx中的端口
/etc/nginx/sites-avaliable/default
将server{
	listen 80 ->9000
http://localhost:9000/phpinfo.php

"""
# 注意事项
# 1. 如果运行不正常，用service nginx status 查看运行状态
# 2. 启动/重启/关闭nginx都要sudo，不然可能会失败
#3. 如果还不能启动，查看log
# tail /var/log/nginx/error.log会告诉你失败的原因
