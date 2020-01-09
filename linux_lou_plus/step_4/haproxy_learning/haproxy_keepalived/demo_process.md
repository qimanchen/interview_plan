# 实验步骤
	1. 初始化docker容器，set_docker.sh
		docker run --privileged --name=HAProxy-master -tid ubuntu
		docker run --privileged --name=HAProxy-backup -tid ubuntu
		docker run --privileged --name=nginx-server-1 -tid ubuntu
		docker run --privileged --name=nginx-server-2 -tid ubuntu
		docker run --privileged --name=nginx-server-3 -tid ubuntu
	2. 安装与配置 nginx 服务器
		docker attach nginx-server-1
		apt-get update
		apt-get install vim nginx -y
		service nginx start    # 启动 nginx 服务
		vim /usr/share/nginx/html/index.html
	3. HAProxy 节点的安装
		docker attach HAProxy-*
		apt-get update 
		apt-get install vim keepalived haproxy -y
	4. HAProxy 的 Keepalived 配置
		# 进入 HAProxy-master
		docker attach HAProxy-master 

		# 编辑配置文件
		vim /etc/keepalived/keepalived.conf  
	5. HAProxy 的配置
		docker attach HAProxy-master
		vim /etc/haproxy/haproxy.cfg
			global 配置部分：这部分一般用来设定全局的配置参数，是属于进程级别的配置，一般和操作系统的配置相关，所以很少去修改它。

			defaults 配置部分：配置默认参数，在这部分配置的内容，默认会自动被引用到下面的 frontend 和 backend、listen 配置部分，
			         可以配置某些公共的参数，如果下面部分配置的参数与 defaults 部分的配置相同，则会覆盖 defaults 的配置参数。

			frontend 配置部分：这部分用于设置接收用户请求的前端虚拟节点。frontend 部分可以根据 ACL 规则动态指定要使用的后端(backend)。
			         与此对应的部分是 backend。

			backend 配置部分：这部分配置内容主要用于设置后端集群服务器，即可以提供 web 服务真实的服务器。
			        一个 backend 部分通常对应一个后端服务器或一组后端服务器集群。其类似于 LVS 的 Real-Server 。
					
			listen 配置部分：此部分是 frontend 与backend 部分的结合体。
	6. 修改 hosts 文件
	
	7.  服务运行
		service rsyslog start
		service keepalived start
		service keepalived start
		haproxy -c -f /etc/haproxy/haproxy.cfg #检查配置文件是否存在语法错误
		haproxy -d -f /etc/haproxy/haproxy.cfg    #以调试模式启动 HAProxy
		
		若是想通过 service 命令来启动我们的 HAProxy 的话我们首先需要修改 /etc/default/haproxy 文件，
		将其中的 ENABLED 变量值修改为 1 即可，修改之后我们就可以通过
		service haproxy start
	8. 使用web监视
		192.168.0.10:3000/haproxy-status -- listen中设置的参数