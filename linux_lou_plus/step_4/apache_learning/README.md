# Apache 安装与配置
	Apache 的安装方式有两种：
		1. 安装包管理工具安装
			$ sudo apt-get install apache2
		# 安装最新版
			# 若是没有添加源工具需要该步骤
			$ sudo apt-get install software-properties-common

			# 实验环境 python3 默认指向的是 python3.5，但后面要用到的 add-apt-repository 工具不支持 python3.5，
			  需要执行下面的命令来切换 python3 版本为 python3.4
			$ sudo update-alternatives --config python3

			# 添加源与密钥
			$ sudo add-apt-repository ppa:ondrej/apache2

			# 更新源
			$ sudo apt-get update

			# 安装最新版
			$ sudo apt-get install apache2
			$ sudo apt-get install apache2
		2. 手动编译安装
			下载与解压 Apache 源码，官方链接
			安装编译所需的依赖包与依赖库，如 gcc 等等
			通过 configure 可执行文件添加编译参数，创建编译文件，可以添加的参数项非常多
			通过 make 编译源码
			通过 make install 安装编译好的源码
	Apache 的配置
		默认的配置文件位于 /etc/apache2 中（当然在 Red Hat 系列中，Apache 名为 httpd，所以位于 /etc/httpd 中）
			apache2.conf：是 Apache 的主要配置文件，全局的一些配置都会在这里面
			ports.conf：是 Apache 监听端口的配置文件，由主配置文件所包含读取
			envvars：是 Apache 环境变量的配置文件
			magic：是在 Apache 加载了 mod_mime_magic 模块之后，用户辅助判断文件的 MIME 类型的配置文件
		主要起作用的是 apache2.conf 主配置，其他的配置文件都是在主配置文件中通过 Include 指令包含读取
		主配置文件中只会读取 enable 中的配置文件，而 enable 中的配置文件是我们确认并加载 available 中配置文件的一个软连接
	
	# 配置新apache网页
		# 设置新的/etc/apache2/sites-available/网页配置
		sudo vim /etc/apache2/sites-available/test1.conf
			修改对应的端口
			修改ServerName ops1.shiyanlou.com
			修改DocumentRoot /home/shiyanlou/test1/
		# 在对应的enable文件中创立link文件
		sudo a2ensite test1.conf
		# 修改/etc/apache2/ports.conf
			Listen 8080
		# 修改/etc/apache2/apache2.conf
			配置目录访问许可
			<Directory /home/shiyanlou/test1/>
			....
			</Directory>
		# 添加dns /etc/hosts
			127.0.0.1	ops1.shiyanlou.com
		# 重启服务
		sudo service apache2 reload