# 课程介绍
	1. nginx服务一些常见应用(模块功能)
	2. LNMP架构
	
# 课程回顾
	利用nginx搭建单个网站
	利用nginx搭建多个网站(尽量每一个网站有单独的虚拟主机配置文件,每个网站有独立的站点目录)
	利用nginx配置安全控制功能
		域名
		认证
	
# 课程内容
	02. nginx的企业应用
		1) 利用nginx服务搭建网站文件共享服务器
			a 编写配置文件
				ngx_http_autoindex_module
					autoindex on
					location / {
						autoindex on; --- 开启nginx站点目录索引功能
					}
				ps: 注意location目录中不要存在index.html 文件，否则会直接显示index.html文件
				index_module
				ps:当首页文件存在时，则该文件共享功能不能实现
					1. 进入站点目录，删除首页文件
				ps:当打开文件时无法直接下载
					有的文件下载
					mime.types --- 在里面设置的文件，可以被读取
				mime.types作用
					文件中有的扩展名资源，进行访问时会直接看到里面内容
					文件中没有的扩展名资源，进行访问时会直接下载
		网站页面出现中文文件名乱码
			设定字符集
				charset utf-8;
			浏览器打开文件乱码 -- 浏览器设置
				开发者工具 -- charset
		2）利用nginx搭建网站别名信息
			a 修改配置文件
				server_name		www.oldboy.com old.com;
			b 修改访问主机的hosts文件
			作用：
				01. 便于网站访问测试 -- 以用户访问进行测试
				02. 定位要访问的网站服务器 -- 多台web服务器
					代码上线：
						先找一台，上线代码，设置别名，测试，再上线进行测试
		3）利用nginx状态模块功能对网站进行监控
			访问量达到服务器极限 --- 检测
			http_stub_status_module
			1. 编写配置文件
				server {
					listen	80;
					server_name	state.oldboy.com
					stub_status;
				}
			2. 重启nginx服务，并且编写解析文件hosts
				实现短连接
					keepalive_timeout 0;
				Active connections: 2  # 激活的连接数，同时访问的连接 4000 -- 2000 警告 -- 监控
				server accepts（发送的连接数，访问了几次--综合） handled （处理的连接数） requests （总计的请求的数量 -- 请求资源的次数）
				 2 2 1 
				Reading(正在读取请求报文的数量）: 0 Writing（正在响应报文的数量）: 1 Waiting（队列，正在等待的请求报文的数量）: 1 监控
	04. nginx日志功能配置
		错误日志 /var/log/nginx/access.log
			core functionality
			error_log file [level]; 指定错误级别
			错误级别：
				debug	调试级别 服务运行的状态信息和错误信息详细显示 信息很多
				info	信息级别 只显示重要的运行和错误信息
				notice	通知
				warn	警告
				error	错误	一般推荐的级别
				crit,	严重
				alert,	严重警告
				or emerg	灾难
		访问日志 /var/log/nginx/error.log
			ngx_http_log_module
			log_format main "" --- 定义日志的格式
				'$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
				$remote_addr -- 显示用户访问源IP地址信息
				$remote_user -- 显示认证的用户名信息
				$time_local -- 访问网站时间
				$request -- 请求报文的请求行
				$status -- 访问网站的状态码
				$body_bytes_sent -- 相应数据的大小
				$http_referer -- 友情链接跳转到，防止用户盗链（图片）
				$http_user_agent -- 访问客户端的user-agent
				$http_x_forwarded_for	-- 负载均衡
			access_log logfile main; -- 不同的网站服务，设置不同的服务日志保存到不同的文件中
			ps: 日志文件信息需要做切割处理 logrotate
	05. nginx location作用说明
		ngx_http_core_module
			location 进行匹配（uri)
			错误页面优雅显示
			location /oldboy {
				root /html/www;
				error_page 404 /oldboy.jpg --- 相对于oldboy目录中
			}
		location 详细配置方法
			syntax: location [ = ~ ~* ^~] uri { .. }
				= 精确匹配 优先级最高
				/ 默认匹配 优先级 03 优先级最低 04
				/documents/ 按照目录匹配，其他所有条件都没匹配时，采用
				^~ 优先匹配 优先级 02 -- 不识别uri中的符号信息
				~* 不区分大小写匹配
				~ 区分大小写进行配置
				location = / {
					return 404；
				}
	06. 利用nginx实现页面跳转
		oldboy.com ---跳转到 www.oldboy.com
		nginx_http_rewrite_
			synatax -- rewrite regex replacement [flag]; rewrite 匹配的正则信息 替换成什么信息
				rewrite ^/(.*) http://www.etian.org/$1 permanent; 重写规则配置
					301会存在一个问题，如果缓存的跳转地址换了 -- 可能访问失败
					跳转方式：	permanent  301 永久跳转 会将跳转信息进行缓存
						redirect 302 临时跳转
			防止位置：
				server
				location
		# 访问时，如果没有找到域名匹配的location 则通过访问第一个匹配
			server {
				listen	80;
				server_name www.baidu.com baidu.com; 通过别名，以匹配对应的域名
			}
			把rewrite 放到server模块中 --- 会导致很多次访问
				^/(.*) -- 一直跳转
			curl -L oldby.com --- 查看跳转后的内容
			curl -Lv oldboy.com --- 查看访问详细过程
		# 出现无限跳转解决
			1. 利用不同server虚拟主机跳转访问
				server {
					listen 80;
					server_name oldboy.com; -- 待跳转的
					rewrite ;
				}
				server {
				}
			2. 利用if判断实现打破循环功能
				if -- server location
				if ($host ~* '^oldboy.com") {
					rewrite ^/(.*) http://www.oldboy.com/ permanent;
				}
				$host -- URL
			www.oldboy.com/oldboy01/oldboy02/oldboy.jpg --- www.oldboy.com/oldboy.jpg
			ps； rewrite 中跳转的内容要写全 http://...
		
# 作业
	01.利用命令取出状态页面信息中的数值