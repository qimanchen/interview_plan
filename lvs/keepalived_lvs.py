# LVS+keepalived实战

# 模拟环境结构
"""
宿主机（本实验桌面环境）模拟客户端；
启动一台 docker container 作为我们的 Load Balancer 1 (VIP：192.168.0.10，作为主路由)；
启动一台 docker container 作为我们的 Load Balancer 2 (VIP：192.168.0.10，作为备份路由)；
启动一台 docker container 作为我们的 Real Server 1（VIP：192.168.0.10）；
启动一台 docker container 作为我们的 Real Server 2（VIP：192.168.0.10）；
"""

# 验证步骤
 # LoadBalancer1 的 /var/log/syslog 日志中看到当前的节点为 Master
 # 可以通过看日志，发现LoadBalance的身份转变
"""
LVS 成功测试一：我们能够通过 VIP 访问我们的 Nginx 站点，经过多次的刷新我们能够访问另一个站点的内容
（以显示的内容以作区分，因为负载并不高，所以需要很多次刷新，点击地址栏，按住 F5 不放）

LVS 成功测试二：当我们停止当前访问节点的 nginx 服务时，我们还能通过虚拟 IP 访问我们的站点，
说明 LVS 在工作，能够将请求分发给另外一台 Real Server

keepalived 成功：我们使用 arp -a 查看当前的虚拟 IP 指向的 MAC 地址是 Master 节点的，然后停止 Master 节点的 keepalived 服务，
然后还能通过我们的虚拟 IP 访问我们的节点，并且此时通过 arp -a 可以看到 虚拟 IP 指向的 Backup 节点的 Mac 地址
"""

# 设置模拟服务器池和均衡器池
"""
docker run --privileged --name=LoadBalancer1 -tid ubuntu
docker run --privileged --name=LoadBalancer2 -tid ubuntu
docker run --privileged --name=RealServer1 -tid ubuntu
docker run --privileged --name=RealServer2 -tid ubuntu
"""

# 配置两台RealServer的环境
"""
1. 安装vim与nginx工具
	docker attach RealServer1
	apt-get update
	apt-get install nginx vim
2. 修改默认的nginx展示页面
	vim /usr/share/nginx/html/index.html
3. 启动nginx服务
	service nginx start 
4. 修改内核参数，抑制arp
	修改 arp 的内核参数配置，来防止 LVS 的集群的 arp 表，从而影响负载均衡机器数据包的接收
	echo "1" > /proc/sys/net/ipv4/conf/lo/arp_ignore
	echo "1" > /proc/sys/net/ipv4/conf/all/arp_ignore
	echo "2" > /proc/sys/net/ipv4/conf/lo/arp_announce
	echo "2" > /proc/sys/net/ipv4/conf/all/arp_announce
	
	# 配置说明
	arp_ignore：定义了本机响应 ARP 请求的级别。
		0表示目标 IP 是本机的，则响应 ARP 请求。默认为 0
		
		1如果接收 ARP 请求的网卡 IP 和目标 IP 相同，则响应 ARP 请求
		
	arp_announce：定义了发送 ARP 请求时，源 IP 应该填什么
		0 表示使用任一网络接口上配置的本地 IP 地址，通常就是待发送的 IP 数据包的源 IP 地址 。默认为 0

		1 尽量避免使用不属于该网络接口(即发送数据包的网络接口)子网的本地地址作为 ARP 请求的源 IP 地址。大致的意思是如果主机包含多个子网，而 IP 数据包的源 IP 地址属于其中一个子网，虽然该 IP 地址不属于本网口的子网，但是也可以作为ARP 请求数据包的发送方 IP。

		2 表示忽略 IP 数据包的源 IP 地址，总是选择网络接口所配置的最合适的 IP 地址作为 ARP 请求数据包的源 IP 地址(一般适用于一个网口配置了多个 IP 地址)
5. 创建网卡别名与添加路由
	只有在相应 RealServer 中配置了虚拟 IP 地址，该机器才会接收并处理负载均衡机器上发来的数据包
	# 添加网卡别名
	ifconfig lo:0 192.168.0.10 broadcast 192.168.0.10 netmask 255.255.255.255 up

	# 添加路由
	route add -host 192.168.0.10 dev lo:0
"""

# 配置两台LoadBalancer环境
"""
1. 安装 ipvsadm 与 Keepalived
	# 因为镜像中默认是 ubuntu 原生源，所以有时候比较慢
	apt-get update

	# 安装 ipvsadm 与 keepalived
	apt-get install ipvsadm keepalived vim

	# 验证 ipvsadm
	ipvsadm -l
	
2. 修改 Keepalived 的配置文件修改
	Keepalived 就是为 LVS 而诞生的，它会调用 IPVS 模块，所以此时我们并不需要再去通过 ipvsadm 工具来编写规则，
	我们直接将我们要做的配置写在配置文件中，Keepalived 会根据配置文件自动的为我们配置
	
	vim /etc/keepalived/keepalived.conf
	
	将 LoadBalancer1 作为我们的主路由器
	
	以上配置内容为 LoadBalancer1 的 Keepalived.conf 配置内容。在编写配置内容时。
	一定要注意文字和语法格式，因为 Keepalived 在启动时并不会检测配置文件的正确性，
	及时没有配置文件，Keepalived 也能正常启动，所以一定要保证配置文件内容的正确性。

	紧接着我们在 LoadBalancer2 中做相同的配置，主需要将 "Master" 修改成 "BACKUP"，以及优先级的调整即可。
3. 启动 Keepalived 使配置生效
	service rsyslog start
	service keepalived start 
	可以通过ipvsadm -l 查看设置效果
"""