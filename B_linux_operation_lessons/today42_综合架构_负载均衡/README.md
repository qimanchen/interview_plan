# 课程介绍
	1. LNMP架构和存储服务器建立关系
	2. LNMP架构和数据库服务器建立关系（数据迁移)
	3. nginx负载均衡概念介绍
	4. nginx负载均衡环境准备
	5. nginx负载均衡设置过程
	6. nginx负载均衡扩展说明
	7. nginx负载均衡企业应用
		a 根据用户的访问uri信息进行负载均衡（动静分离的架构）
		b 根据用户的agent信息进行负载均衡（手机和客户端显示不同页面）
# 课程回顾
	1）网站服务器nginx服务概念
	2）网站服务器nginx服务部署
	3）网站服务器nginx服务配置
	4）网站服务器nginx服务应用
	5）网站LNMP架构（搭建网站页面-wordpress)

# 课程内容
	01. 课程疑问：
		1. 上传wordpress主题，报413错误，如何解决 -- 上传文档大小超过设置值
			cd /etc/nginx/conf.d
				client_max_body_size 20m; -- http server location
			vim /etc/php.ini
				upload_max_filesize = 20m;
		2）如何将LNMP架构与存储服务器建立连接
			a 找出图片存储的目录
				-- 找到图片存储的位置
					1. 根据图片链接地址
					2. 先定位数据存放在站点目录中，再通过find命令在站点目录中查找
						find /html/blog -type f -mmin -5 "*.jpg"
						inotifywait -mrq /html/blog
			b 使web服务器和存储服务器建立连接
				检查存储服务是否正常
					showmount -e 172.16.1.31
					编辑配置文件 /etc/exports
				wp-content/uploads/2019/05
				移动文件
					mv 2019 /tmp
					mount -t nfs 172.16.1.31:/data/blog /html/blog/wp-content/uploads
				再将原来的文件移动回来文件
					cat /var/lib/nfs/etab
				无法存储文件
					管理用户无法存储 -- root_squash
						- 使root用户可以创建 -- 将映射用户改为www而不是默认的nfsnobody
						vim /etc/exports 
						sed -i.bak 's#(sync)#\1,anonuid=1001,anongid=1001#\g'
					普通用户服务存储 -- no_all_squash
					1. 修改映射用户为www
						web端和nfs端都为www
					2. 修改目录权限
						chown -R www.www /data
		3. 如何让LNMP架构和数据服务器建立关系
			-- 为什么要将web服务和数据库服务分离 -- 数据共享
			1. 将web服务器本地数据进行备份
				mysqldump -uroot -pcentos --all-database > /tmp/web_back.sql
			2. 将备份数据进行迁移
				scp -rp /tmp/web_back.sql 172.16.1.51
			3. 恢复数据信息
				curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
				-- 恢复数据时，注意数据库版本的限制问题
				yum install -y mariadb-server mariadb
				systemctl start mariadb.service
				mysqladmin -u root password 'centos'
				mysql -uroot -pcentos < web_back.sql -- 恢复数据
			4. 修改数据库服务器中用户信息
				错误：ERROR 1449 (HY000): The user specified as a definer ('mariadb.sys'@'localhost') does not exist
					错误原因 -- 对应的数据库的管理用户不存到导致的错误
				优化 -- 删除无用的用户信息 -- 没有用户名的用户
					delete from mysql.user where user="" and host="localhost";
					delete from mysql.user where user="" and host="web01";
				添加 -- 添加新的用户信息
					grant all on wordpress.* to 'wordpress'@172.16.1.%' identified by 'centos'
					flush privileges; # 刷新权限
					测试：
						mysql -uwordpress -pcentos -h 172.16.1.51
						问题：
							发现无法登录时,需要将数据库服务器上的数据库服务进行重启
			5. 修改web服务器代码文件信息
				 cd wp-config.php -- 改为远程服务
					DB-host
			6. 停止web服务器上的sql服务
				# 尝试测试连接时无法连接到数据库 -- 
			问题：
				数据库服务没用启动 -- 3306无法连接
				php服务未开启 -- 502 网关错误 -- cgi接口
		4. web01代码信息迁移到web02中，会出现显示错误问题
			迁移代码后 -- blog.etiantian.org 会跳转到blog.oldboy.org(如果它废弃了)
			那么需要将默认访问地址改为blog.etiantian.org 中进行设置
			-- 访问新域名会自动跳转到老的域名
				1. 修改wordpress后台设置信息，将后台中老的域名改为新的域名
				2. 修改数据库中一个表，在表中修改一个域名有关条目信息（update）
	03. 负载均衡的概念说明
		什么是集群
			完成相同任务或工作的一组服务器（web01 web02 web03 -- web集群)
			-- 为什么要集群
				高可用性服务
				价格有效性
				可伸缩性
		什么是负载均衡
			1. 实现用户访问，分配调度
			2. 实现用户访问压力分担
		什么是反向代理
			反向代理 -- 外网 -- 代理服务器 -- 公司网站服务器web（内网）
			正向代理 -- 内网的主机 -- 代理服务器 -- 访问外网服务器
			
	04. 准备负载均衡环境
		a 集群服务器部署
			ps：集群中每台服务器的配置一模一样
			企业中
			01. 先部署好一台LNMP服务器，上传代码信息
			02. 进行访问测试
			03. 批量部署多台web服务器
			04. 将nginx配置文件进行分发
			05. 将站点目录分发
			教学中 -- 直接将web01作为模板机
				sed -i 's#\.7#.8#g' 
				hostnamectl set-hostname web02
			-- 利用手动方式实现负载均衡
				- 通过指定不同的ip域名对应配置
			-- df -h 服务器卡死的问题 -- nfs服务器挂载多次
				需要先将所有的nfs挂载卸载，并进行重新挂载
		b 负载均衡服务器部署
			 -- 通过主模板机进行克隆
				
			1. 安装部署nginx软件
				-- 更新yum源
				-- 安装
			2. 编写nginx负载服务配置文件
				ngx_http_upstream_module -- upstream 负载均衡 -- http
				ngx_http_proxy_module -- proxy_pass 反向代理 -- location,if
				cp nginx.conf{,.bak}
				调整用户为www
				新建lb.conf文件
					# 注意测试时只开了两台web服务器
					upstream oldboy {
						server 172.16.1.17:8080;
						server 172.16.1.18:8080;		-- 定义可以将请求分配给哪些web服务器
						server 172.16.1.19:80;
					}
					server {
						listen	80;
						server_name www.oldboy.com;
						location / {
							proxy_pass http://oldboy;	-- 将请求分配给指定集群
						}
					}
			3. 实现负载功能测试
				搭建集群测试 -- 准备测试文件
					for name in www bbs blog;do echo "$name $(hostname -i)" > /html/$name/wenwen.html;done
				修改windows解析文件
					10.0.0.5 www.odlboy.com blog.oldboy.com bbs.oldboy.com
				-- 可以通过抓包软件进行测试 -- http数据包
		负载均衡访问网站异常排错思路 -- 从实际访问流程来思考
			1. 负载均衡 测试后端web节点服务器是否能够正常访问
			2. 负载均衡 利用curl命令访问负载均衡服务器
				curl www.oldboy.com
				curl -H host:www.oldboy.com 10.0.0.7/wenwen.html -- 指定将www.oldboy.com解析为10.0.0.7
				curl -L 显示对应的网页的（302直接显示跳转后的网页）
			3. 打开一个xshell连接 ping www.oldboy.com，测试能否ping通
			4. 配置文件编写不正确
	04. 负载均衡配置模块详细说明
		ngx_http_upstream_module -- upstream
		-- 实现不同调度功能
			1. 轮询分配请求 （平均） -- 默认
			2. 权重分配请求
				upstream oldboy {
						server 172.16.1.17:80 weight=3;
						server 172.16.1.18:80 weight=2;
						server 172.16.1.19:80 weight=1;
					}
			3. 实现热备功能
				upstream oldboy {
						server 172.16.1.17:80;
						server 172.16.1.18:80;
						server 172.16.1.19:80 backup; -- 所有的web节点坏了，才会访问
					}
			4. 定义最大失败次数 -- 健康检查参数
				upstream oldboy {
						server 172.16.1.17:80 max_fails=5;
						server 172.16.1.18:80;
						server 172.16.1.19:80;
					}
			5. 定义失败后重发的时间 -- 健康检查参数
				upstream oldboy {
						server 172.16.1.17:80 max_fails=5 fail_timeout=30s;
						server 172.16.1.18:80;
						server 172.16.1.19:80 down;  -- 服务器下线
					}
				fail_timeout = 10s 会给失败的服务器一次机会
			
		-- 实现不同的调度算法
			1. rr 轮询调度算法
			2. wrr 权重调度算法
			3. ip_hash 算法 -- 出现反复登录的时候
				# 多次登录的情况 -- 通过负载均衡多次访问不同后台服务器
				-- 解决
					1. 通过将登录信息放到缓存服务器（memcache）中
					2. 通过指定ip_hash功能
				-- 通过ip hash 导致局域网内多台主机访问一台服务器（负载不均）
				upstream oldboy {
						ip_hash;
						server 172.16.1.17:80;
						server 172.16.1.18:80;
						server 172.16.1.19:80;  -- 服务器下线
					}
			4. least_conn 根据服务器连接资源调度
		ngx_http_proxy_module
			server {
				listen	80;
				server_name www.oldboy.com;
				location / {
					proxy_pass http://oldboy;	-- 将请求分配给指定集群
					proxy_set_header Host $host;
					# 这样会导致，负载均衡服务器访问后台服务器时，会将其host看为 oldboy
				}
			01. 访问不同的网站地址，不能显示不同的网站页面 -- host 解析错误 -- 面试问题
				-- 主要由于直接访问后端web服务器的为负载均衡服务器，因此负载均衡服务器访问时，使用的是集群的名称
				-- 若web服务器中没有对应域名的虚拟server，那么只会找对应端口符合的服务
				sed -i "s#(include).*#\#include#g"
				proxy_set_header Host $host; -- 将客户端的主机名解析过来
			02. 访问网站用户地址信息无法进行分析统计 -- 负载均衡后，后台服务器显示是负载均衡服务器的ip
				--- 记录真实的客户端主机地址
				http_x_forwarded_for
				proxy_set_header X-Forwarded-For $remote_addr;
			03. 访问负载均衡会出现错误页面，会影响用户体验
				 -- 某个后台web服务器的页面被删除了,对错误的显示将其跳过
				 proxy_next_upstream  error timeout http_404 http_502 http_503;-- http server location
		负载均衡 LVS haproxy	 
# 课程总结

# 练习
	1. 总结ngx_http_upstream_module
	2. ngx_http_proxy_module
	3. 高可用服务 keepalived
		提前克隆好一台lb02主机 lb01+lb02 高可用集群（HA)