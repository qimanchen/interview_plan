# 课程回顾
	
# 课程介绍
	01. TCP协议重要原理
		三次握手
			01. 主机A向主机B发送TCP报文
				SYN = 1， 请求建立
			02. 主机B向主机A发送TCP响应报文
				SYN = 1, ACK=1
			03. 主机A向主机B发送TCP报文
				ACK = 1，确认主机B的确认消息
			seq 序列号，标记数据段顺序
			确认号ack，占四个字节，期望收到下一个字节编号
			ACK：为1时，ack才有效
			SYN：只用于建立连接，其他时候设置为0
			终止FIN：用来释放一个连接，FIN=1，表示报文数据发送完毕
			A											B
			CLOSED		------->						CLOSED
						SYN=1,seq=x						LISTEN
			SYN-SENT
						<------
						SYN=1,ACK=1,seq=y,ack=x+1		SYN-RCVD
						------>
						ACK=1,seq=x+1,ack=y+1
			ESTABLISHED									ESTABLISHED
			ps:数据包传输过程中包拆分与组合
				数据包拆分，每个数据包都有着相应的编号
				seq，确认号码
			1）第一次握手
				发送SYN请求建立连接控制字段，发送seq序列号信息0，第一个数据包的序列号默认为0
			2）第二次握手
				发送SYN请求建立连接控制字段，同时还会发送ack确认控制字段
				发送seq序列号信息也为0，还会发送ACK确认号，（上一个seq序列号+1）信息，对上一个数据序列号信息进行确认
			3）第三次握手
				发送ack确认控制字段，发送seq序列号信息（1），发送ack确认号（1）
		四次挥手
			A											B
			ESTABLISHED									ESTABLISHED
						------>
						FIN=1,seq=u
			FIN-WAIT1									CLOSE-WAIT
						<------
						ACK=1,seq=v,ack=u+1
			FIN-WAIT2
						<------
						FIN=1,ACK=1,seq=w,ack=u+1
			TIME-WAIT									LAST-ACK
						------>
						ACK=1,seq=u+1,ack=w+1			CLOSED
			2MSL
			
			CLOSED
			1）第一次挥手
				发送FIN请求断开连接控制字段
			2）第二次挥手
				发送ACK确认报文字段
			3）第三次挥手
				发送FIN请求断开连接字段，发送ACK确认字段
			4）第四次挥手
				发送ACK确认号字段
		netstat -an 查看连接的转态码
	02. TCP的十一种状态集
		TCP的三次握手 5中状态
			A											B
			CLOSED		------->						CLOSED
						SYN=1,seq=x						LISTEN
			SYN-SENT
						<------
						SYN=1,ACK=1,seq=y,ack=x+1		SYN-RCVD
						------>
						ACK=1,seq=x+1,ack=y+1
			ESTABLISHED									ESTABLISHED
			00：两台主机都处于关闭状态 CLOSED
			01：服务端将相应服务进行开启	CLOSED --- LISTEN
			02: 客服端向服务端发出连接请求	CLOSED --- SYN_SENT
			03: 服务端接收到连接请求，进行确认	LISTEN -- SYN_RCVD
			04:	客户端再次进行确认	SYN_SENT -- ESTABLISHED
			05: 服务端接收到确认信息	SYN_RCVD -- ESTABLISHED
			tcp        0     36 192.168.90.200:22       192.168.90.1:52352      SYN_RCVD
		TCP的四次挥手
			A											B
			ESTABLISHED									ESTABLISHED
						------>
						FIN=1,seq=u
			FIN-WAIT1									CLOSE-WAIT
						<------
						ACK=1,seq=v,ack=u+1
			FIN-WAIT2
						<------
						FIN=1,ACK=1,seq=w,ack=u+1
			TIME-WAIT									LAST-ACK
						------>
						ACK=1,seq=u+1,ack=w+1			CLOSED
			2MSL
			
			CLOSED
			01. 客户端发送请求断开连接信息	ESTABLISHED --- FIN-WAIT1
			02. 服务端接收断开连接请求，并进行确认		ESTABLISHED --- CLOSE-WAIT
			03. 客服端接收到了确认信息			FIN-WAIT1 -- FIN-WAIT2
			04. 服务端发送ACK和FIN字段			CLOSE-WAIT -- LAST-ACK
			05. 客户端接收到请求断开连接信息，发送确认	FIN-WAIT2 -- TIME-WAIT
			06. 服务端接收确认信息		LAST-ACK -- CLOSED
			07. 客户端会等待2MSL		TIME-WAIT -- CLOSED
			- 三次挥手的情况
				FIN-WAIT1 直接接收到FIN包，直接进入closing状态 -- TIME-WAIT -- CLOSED
	03. 网络中重要协议原理
		DNS 域名解析系统
			www.baidu.com --- 14.215.177.39
		0：打开浏览器，输入www.baidu.com,回车
		1：在本地主机上寻找域名对应IP地址信息
			a 本地dns缓存中
				windows -- ipconfig/displaydns
			b 找寻本地hosts文件
				windows -- c:/windows/system32/drivers/etc/hosts
			c LDNS服务器
		2：LDNS服务器会查看本地缓存中是否有百度ip地址
			0-2 递归查询
		3：根域名服务器
			www.baidu.com.
			.	根域名服务器
			.com	一级域名服务器
			baidu	二级域名服务器
			www		网站主机记录
			- 可以去问顶级域名服务器
		4：顶级域名服务器 .com
		5: 二级域名服务器 baidu.com ,授权dns服务器
			www.baidu.com 192.168.1.1
			A记录信息
			- 将A记录返回LDNS服务器
			3-5迭代查询记录
		- dig www.baidu.com 
			dig www.baidu.com +trace 显示域名解析过程
			CDN --- 缓存加速，蓝讯
		ARP: 已知IP地址，解析mac地址
			IP头部
			IP源 10.0.0.1
			IP目标 10.0.0.2
			MAC
			mac源 01
			mac目标 FFF
			- 建立arp表， mac -- ip
				arp -a 查看arp表
			a 发送mac地址 FF 广播信息
				确认后，然后目标主机会发送一个包
			同时每台主机会更新各自的arp表
			- 作用：减少网络中的广播数量
	04. IP地址概念
		192.168.1.1 --- IP报文
		源IP，目标IP，在报文中占32位 2^32
		每八位一组，分成四组
		192.168.1.1 -- 点分十进制地址
		11000000.10101000.00000001.00000001
		
		- 二进制到十进制的转换关系 -- 做求和运算
			2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
			128	64	32	16	8	4	2	1
		- 十进制到二进制的转换关系 -- 做求差运算
			172 - 128
			44 - 32
			12 - 8
			4 - 4
			10101100
	05. IP地址分类
		a 按照地址的范围进行划分
			A	前8位-网络位，后面的为主机位		1.0.0.0 - 126.255.255.254
				保留
					10.0.0.0 - 10.255.255.255
				127.0.0.1 -- 本机地址
			B	前16位-网络位，后面为主机位			128.0.0.1 - 191.255.255.254
				172.16.0.0 - 172.31.255.255
			C	前24位-网络位，后面为主机位			192.0.0.1 - 223.255.255.254
				192.168.0.0 - 192.168.255.255
			D										224.0.0.1 - 239.255.255.254
			E	保留
		b 按照地址用途进行划分
			公网地址：全球唯一
			私网地址：重复利用地址，避免地址枯竭，私网地址网段不能出现在互联网的路由器路由表中
		NAT 网络地址转换
		c 按照通讯方式划分
			单播地址：
				网卡上配置的地址
			广播地址：
				主机位全为1的地址
					192.168.1.255
				主机位全为0的地址 -- 网络地址 256 -2 -1（网关地址）
					192.168.1.0
				网络中主机数量=2^n - 2
					n -- 多少个主机位
					-2 -- 一个广播地址 一个网络地址 是不能配置在往卡上
				
				c类地址，一个网络中可以有 253个主机
				b类地址，一个网络中65536 -3 = 65533
				a类地址，一个网络中2^24 -3
			组播地址：D类地址
		- 子网划分概念，将一个大的网络划分成几个小的网络
			1）一个大的网络不做子网划分，会造成地址浪费
			2）一个大的网络不做子网划分，会造成广播风暴
			3）一个大的网络不做子网划分，会造成路由压力
			做子网划分
				1）节省ip地址
				2）减少广播影响
				3）减轻路由压力
		- 如何进行子网划分
			172.16.10.0/16 子网掩码标识 255.255.0.0
			子网掩码：32位二进制的数
				-- ip地址网络位对应子网掩码置为1
			网段：主机位
			172.16 |.10.0
			172.16.| 00		|000000 00000000
					子网位
			子网划分后的子网掩码 255.255.128.0
			172.16.0.1 172.16.127.254
			172.16.128.1 172.16.255.254
			- 子网划分
				1. 子网的个数 n
					2^n 向主机位借的位数
	06. 办公环境上网管理
		路由器配置：
			01. 配置上网的用户名和密码信息 实现拨号访问外网 自动获取一个公网地址
				静态地址配置，在路由器外网接口配置运营商给你的公网地址
			02.	需要在路由器上配置dhcp服务信息
			03. 需要配置路由信息（静态默认路由）
				ip route show
				外网，直接发往静态默认路由
				ip route 0.0.0.0 0.0.0.0 10.0.1.1
		虚拟主机上网原理
			internet -- Router -- 交换机 -- windows（网卡）
															vmware（虚拟主机）
																			虚拟主机1 -- vnet8
																虚拟交换机	虚拟主机2 -- vnet8
																			虚拟主机3 -- vnet8
												xshell -- vnet8
																虚拟路由器
																- 访问外网的方式
																	NAT模式 -- ip翻译
																	桥接模式 -- 虚拟交换机 -- 直接和真实交换相连
																host only模式 -- 不连接外网
	07. 系统中路由设置
		设置方法
			centos6：和网络相关的命令 net-tools
				route
				- route -n 查看路由
				- 静态默认路由
					a 编写网卡配置文件
						gateway
					b 利用命令临时配置
						route add default gw 10.0.0.254
						route del default gw 10.0.0.254
						作用：实现主机访问外网，用于测试新的网关地址
				- 静态网段路由
					多块网卡,一内网，一外网，不同网关
					route add -net 10.0.3.0 netmask 255.255.255.0 gw 10.0.1.2
						如果主机中没有10.0.1.2,那么要使用 dev eth1 来设置
					route del -net 10.0.3.0 netmask 255.255.255.0 gw 10.0.1.2
				- 静态主机路由
					多块网卡，一内网指定主机访问
					route add -host 10.0.3.201 dev eth1
					route del -host 10.0.3.201 dev eth1
			centos7：和网络相关的命令 iproute
				ip route
				- ip route show 查看路由
				- 静态默认路由
					a 编写网卡配置文件
						gateway
					b 利用命令临时配置
						ip route add default via 10.0.0.254
						ip route del default via 10.0.0.254
							ip route del 192.168.5.0/24
				- 静态网段路由
					ip route add -net 10.0.3.0 netmask 255.255.255.0 via 10.0.1.2
						ip route add 192.168.5.0/24 dev eth0
					ip route del -net 10.0.3.0 netmask 255.255.255.0 via 10.0.1.2
						ip route add 192.168.10.0/24 via 192.168.5.100 dev eth0
				- 静态主机路由
					ip route add -host 10.0.3.201 via eth1
					ip route del -host 10.0.3.201 via eth1
					dhclient
				ip子网掩码计算器
			
# 课程总结
	
# 练习
	为什么断开连接需要4次？
		
	可不可以断开连接利用3次完成？
	
	172.16.0.0/18
	可以划分几个子网
		4 -- 2的n次方
	子网掩码信息
		255.255.192.0
	子网主机地址范围
		172.16.0.0
		172.16.0.1 - 172.16.63.254
		
		172.16.64.0
		172.16.64.1 - 172.16.127.254
		
		172.16.128.0
		172.168.128.1 - 172.16.191.254
		
		172.168.192.0
		172.168.192.1 - 172.168.255.254
		
	
# 拓展