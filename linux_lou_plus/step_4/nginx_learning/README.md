Nginx参数说明
	location中的参数：
		设置解析超时时间
			resolver_timeout 指令
			resolver_timeout time; # DNS解析时间
			
		代理连接超时时间
			proxy_connect_timeout 指令
			proxy_connect_timeout time; # 正向代理连接时间
			
			proxy_send_timeout 指令
			proxy_send_timeout time; # 请求发送（多长时间不发，关闭连接时间）
			
			proxy_read_timeout 指令
			# 等待相应超时时间
			
	# 通过设置代理服务器
	http_proxy
	https_proxy