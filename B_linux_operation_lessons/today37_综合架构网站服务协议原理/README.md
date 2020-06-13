# 课程介绍
	1. 用户访问网站的流程
	2. HTTP协议的数据包
	   HTTP请求报文
	   HTTP响应报文
	3. 状态码信息
	4. 请求访问的资源信息
		静态资源/动态资源
	5. 网站好坏评测环境
	6. 常用的网站服务
	7. nginx软件部署
# 课程回顾
	1. ansible批量管理软件概念
	2. ansible批量管理软件组成
		a 软件模块
		b 软件主机清单
		c 软件的剧本编写
	3. ansible软件的部署安装
		基于秘钥的远程连接
		a 安装
		b 配置主机清单
		c 测试
	4. ansible模块使用方法
		ansible hosts -m module -a " params"
	5. ansible主机清单配置方法
		a 利用分组进行配置
		b 设置变量信息管理 -- 基于秘钥连接
		c 利用嵌入方式配置
	6. ansible软件的剧本编写方法
		语法规范：空格 冒号 短横线
		剧本扩展功能：变量 循环 
		剧本角色功能
		
		server 和 client整合
		- import_tasks: server
		  when: ansible_ip_address
		- import_tasks: client
	7. ansible常见问题总结
		1. 无法远程管理
			秘钥没法合理分发
			主机清单配置有关
			远程服务是否开启
		2. 剧本批量执行
			检查剧本语法
			检查剧本模块应用 -- 尽量不要都使用shell模块
			剧本执行卡死 -- ansible-playbook -vv 显示详细运行过程
# 课程内容
	01. 网站页面访问流程
		00. 客户端 浏览器输入网址信息点击回车(www.oldboyedu.comd)
		01. 客户端 完成域名的解析过程（DNS）
		02. 客户端 直接访问相应网站服务器 建立TCP三次握手过程
		03. 客户端 访问网站服务器	发送http请求报文	多次
		04. 服务端 响应客户端请求	回复Http响应报文	多次
		05. 客户端 获得请求内容
		06. 客户端 结束访问网站过程 完成TCP四次挥手过程
	02. HTTP协议请求和响应
		HTTP 超文本传输协议
		超文本 -- 有超链接的文本
		HTTP请求报文
			1）请求行
				请求方法：	Get -- 读/看--获取/拿过来
							Post -- 写/提交
				请求信息：	index.html（首页文件）
				请求协议：	HTTP:1.1	TCP长连接
							HTTP:1.0	TCP短连接
							HTTP:2.0	TCP长连接优化	提高用户并发（同时）访问的数量
				GET index.html HTTP 1.1
			2）请求头
				请求主机信息	HOST: www.baidu.com
								User-agent: 
			3）空行
				
			4）请求主体
				使用get方法时，没有请求主体信息
				使用post方法时，才能有请求主体
		HTTP响应报文：
			1）起始行
				HTTP/1.1 200
				协议	状态码 -- 访问请求是否成功相应
					200 - Ok
					301 - 永久页面跳转
					302 - 临时跳转
						两者区别：
							301 会被缓存为重定向后的网址
							302 只是临时的地址
					400 - 请求错误，服务器无法理解
					403 - 禁止访问
					404 - Not Found
					
					500 - 内部服务器错误，无法完成请求
					501 - 服务器不支持请求的功能，无法完成请求
					502 - 网关错误
					503 - 系统维护，或超载而导致服务器无法处理请求
					504 - 网关超时
					505 - 服务器不支持http协议版本
			2）响应头
				Server: nginx
				Date:
				Content:
				charset
				vary:
			curl 命令
				curl www.baidu.com
				curl -v www.baidu.com --- 显示详细访问网站的过程
					请求的访问
					请求的相应
				
			3）空行
			4）响应主体
				<html>
				<\html>
	03. HTTP协议资源信息
		URL：统一资源定位符
		URI：统一资源标识符
		
		docs.ansible.com	/	ansible/latest/user_guide/playbooks_reuse_includes.html#
		URL						URI
		
		1. 网站页面静态资源
			要什么给我什么
			特点：
				1. 网页内容固定不变，容易被搜索引擎收入
				2. 网站维护难度大
				3. 网站交互性差
				4. 直接返回数据，不做任何解析
		
		2. 网站页面动态资源
			要什么信息，需要进行查询数据库进行解析后发送给客户端
			特定：
				.asp,php,js,.do,.cgi
				1. 动态交互
				2. 动态资源出现"?"“&”，不便于被搜索引擎收录
				3. 接收到用户请求，需要让动态服务和数据库服务响应
		3. 伪静态资源（动态页面）
			1. 可以便于搜索引擎收录
			2. 有数据库服务支持，实现网页交互
	04. 评测网站好坏的指标
		IP： 根据用户IP地址数量进行统计
			局域网
			拨号
		PV:	页面访问量
			参考值
		UV：记录独立访客数量
			cookie：客户端 标识用户身份信息，保存到客户端
				减少数据传输的压力
				cookie绑定用户信息
			session：服务端 记录用户的一些会话操作 eg. 记录用户登录信息 内存中
		chinaz.com -- 统计
		
		网站的并发：
			网站服务器在单位时间内能够处理的最大连接数
# 课程总结
	DNS TCP
	请求报文 响应报文
	状态信息 http1.0 1.1 2.0
	资源信息 -- URL/URI,资源类型
	评测网站指标 -- IP/PV/UV/并发
作业：
	01. 301跳转和302跳转区别
	02. 总结命令
		curl
			1. 不带任何参数，curl发出的为GET请求
				$ curl https://www.example.com
				curl -H host:www.oldboy.com 172.16.1.15/index.html -- 指定域名解析为172.16.1.15
			2. -A 指定user-agent
				$ curl -A ’new user-agent' https://google.com
			3.	$ curl -H "user-agent: php/1.0' https://google.com 直接修改User-Agent
			4. 	$ curl -b "foo=bar"/ cookies.txt https://google.com 向服务器发送cookie
			5. 	$ curl -c cookies.txt https://google.com 将服务器设置的cookie写入一个文件
			6.	$ curl -d "login=ema&password=123" -X POST https://google.com -- POST请求
				$ curl -d "login=ema" -d "password=123" -X POST https://google.com
				$ curl -d "@data.txt" https://google.com 读取本地文本文件数据，向服务器发送
			7.	--data-urlencode "comment=hello world" -- 与-de相同，可以发送前进行url编码
			8. -e 设置HTTP标头 Referer 表示请求来源
				$ curl -e "https://google.com?q=example" https://www.example.com
				或-H 直接指定
			9. -F 上传二进制文件
				-F "file=@photo.png;type=image/png"
								   ;filename=me.png
			10. -G构造URL查询字符串
				$ curl -G -d "q=kitties" -d "count=20" https://google.com/search
					-- https://google.com/search?q=kitties&count-20
			11. curl -i 打印服务器响应的HTTP头
			12. -I 发送HEAD请求，获取http响应头
			13. -k 跳过SSL检测
			14. curl -L -d "tweet=hi" https://api.twitter.com/tweet -- 跟随服务器的重定向
			15. --limit-rate 100k 限制请求和响应的带宽
			16. -o 将服务器响应保存成文件
				curl -o example.html https://www.example.com
			17. -O 将服务器响应保存成文件,并将URL最后部分作为文件名
				curl -O example.html https://www.example.com/bar.html 
			18 -s 不输出错误信息
				-S 输出执行错误信息
			19. -u 设置服务器认证的用户名和密码
				$ curl -u "bob:12345" https://google.com
				$ curl https://bob:123456@google.com
			20 -v 输出整个通信过程，用于调试
			21. -x 指定HTTP请求代理
				$ curl -x socks5://james.cats@my.com:8080 https://www.example.com
							代理协议：。。。
			22. -X 指定HTTP请求的方法
			
		wget
			1. wget http://test.com/test.file 下载指定文件到当前文件夹
			2. wget -O wordpress.zip http://test.com/download 指定保存的文件的名称
			3. --limit-rate=300k 限制下载速度
			4. -c 断点续传
			5. -b 后台下载
			6. wget --user-agent="ddd" URL
			7. wget --spider url 测试下载
			8. wget --tries=40 URL 设置重试次数
			9. wget -i filelist.txt -- 从*txt中获取下载地址
			10. wget --reject=gif url -- 下载一个网站，不希望下载图片
			11. wget -o download.log URL -- 存入下载信息
			12. wget -r -A.pdf url 下载指定格式文件
			13. wget ftp-url 
	03. 提前部署安装好nginx服务 yum安装
		