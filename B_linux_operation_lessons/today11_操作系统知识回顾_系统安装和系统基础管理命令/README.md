# 操作系统知识回顾
# 课程知识回顾
	1. 安全相关优化
		a 关闭防火墙服务
		b selinux 服务关闭
	2. 字符集优化
		a 避免出现乱码 （中文）
		b 可以让部分信息显示中文
	3. 加快ssh的远程连接
	4. 第一个阶段服务器硬件复习
# 课程介绍
	- 第二阶段回顾：系统安装部署与远程连接
		1. 虚拟化环境部署 -- 进行修改时，进行配置
			- 确认网络相关配置
				vmware - 编辑 - 虚拟网络编辑器 - vmnet8的配置 模式（NAT模式）
					NAT模式：不容易出现ip地址，其他宿主机不能直接访问这个虚拟主机
						其他宿主机连接
							NAT配置 -- 添加（指定虚拟机ip和端口）-代理
					桥接模式：其他宿主机可以直接访问，容易造成ip地址冲突
					仅主机模式：安全，不能访问外网
			- 确认vmnet8虚拟网卡配置正确
				在windows主机中查看虚拟网卡的配置 - 类似正常网卡的配置
			- 确认虚拟软件服务是否开启
				win键+r --- service.msc -- vmware开头的服务是否开启
			-  确认宿主机中是否开启虚拟化功能
				windows 修护模式
		2. 新建虚拟主机
		3. 系统安装说明
			- 磁盘分区（3个分区方案）
			- 预装什么软件 （centos7 最小化安装 1236（软件包组） centos6 最小化安装 235）
				yum list 查看可以安装和已安装的所有软件
				会更新相应的软件索引库
				yum grouplist -- 可以安装和已安装的软件包组
				yum groupinstall -y 软件包组 安装软件包组
		4. 远程连接主机
			01. xshell 免费 功能强大，分屏显示
			02. 如何配置xshell，缓冲区
			03. 进行远程连接
		5. 远程连接异常
			1. 检查链路是否通畅
				ping 192.168.90.200
				不通原因
					- 物理线路
						检查网卡连接
						ssh
						clients ---- 互联网/运营商 ---- server
					- 检查网卡配置
						clients and servers configurations
					- 网络安全策略阻止
					- 虚拟网卡是否配置正确（重新初始化虚拟化网络配置）
			2. 远程连接请求被阻止了
				客户端测试
					telnet 10.0.0.200 22
				a 安全策略被阻止了	
			3. ssh服务是否运行正常（server）
				只能在服务端进行测试
					systemctl status sshd
					netstat -tunpl
						yum install -y net-tools
					ss == netstat（centos7预装ss）
					Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
					tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      2894/sshd           
					tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      3124/master         
					tcp6       0      0 :::22                   :::*                    LISTEN      2894/sshd 
					-l list --- 列表显示网络服务
					-n      --- 服务以端口方式显示
					-t tcp  --- 网络协议
					-u udp
					-p      --- 显示服务的进程信息（pid，服务名称）
				1. 已知一个服务的名称，它对应的端口号是什么
				2. 已知一个服务的端口，请给出端口号的服务的信息
	- 第三阶段 系统基础管理命令
		- 必须掌握
			1. 系统命令提示符组成
				用户名+主机名+当前所在目录 标识符#
			2. 系统命令语法格式
				command [options] operations
			3. 系统目录结构
				一切从根开始
				相对路径
				绝对路径
		- 系统管理命令
			1. 所有基础命令熟记
				- 文件目录创建
					mkdir
					mkdir -p 递归创建目录
					touch 文件创建
					ps：修改文件的时间
				- 文件编辑命令
					vi
						- 光标快速移动
							纵向：gg G nG
							横向：0，$
						- 移动光标并进入编辑模式
							i I a A o O C cc
						- 快速编辑文本内容信息
							dd ndd yy nyy p np
						- 特殊操作编辑文本信息
							1. 显示或取消显示行号
								:set nu
								:set nonu
							2. 撤销操作
								u
								ctrl + r 返回对应的撤销操作
								. 重复上一次操作
							3. 快速搜索内容
								/search_string -- n 进行选择
								ps:忽略大小写
									1. 输入设置信息
										:set ic
										:set noic 取消
										:set ignorecase
									2. /odlboy\c 忽略大小写
							4. 高亮显示
							
							5. 快速删除内容到行尾
								dG 删除光标内容到行尾
					vim 
						1. 取消高亮显示
							:set noh
							/fafafaf 找一个文件中没有的信息
						2. 快速移动或复制数据信息
							:2,4move9 --- 将第几行到第几行的内容移动到指定行内容
							:2,4copy9 --- 复制到指定行
						3. 文件内容进行修改替换
							"#" 也可以换成 "/"
							:%s#odl#old#g -- 将文件中指定信息全部替换
							s substitute 替换
							g global 替换整行中所有所有，不加g只替换第一个
							
							:2,4s#odl#old# -- 替换修改文件部分内容
							:2,$s#odl#old# -- 从第二行到行尾
						4. 批量修改文件内容
							- 批量进行注释
								a 进入批量处理模式 ctrl +v
								b 选中需要加入的内容
								c shift+i 编辑内容
							- 批量删除信息
								a 进入批量处理模式 ctrl +v
								b 选中需要加入的内容
								c d/x
							
			2. 拓展应用实践命令
作业：
	1. 总结网络中的服务端口号
		这是有tcp/udp协议格式所决定的
		- 端口号范围为 1~65535
		- 1~1024被RFC 3232 通用端口
		- 1025~65535 动态端口
		- 21,20 FTP服务器开放端口，用于上传和下载,21 -- 用户认证，20 -- 传输数据文件
		- 22 SSH
		- 23 Telnet 远程登录
		- 25 smtp 用户发送邮件
		- 53 dns服务器开放端口
		- 69 Trival File Transfer 从系统下载代码
		- 80 HTTP
		- 110 RPC服务
		- 161 SNMP 远程管理设备
		- 179 BGP 边界网关管理协议
		- 443 HTTPS
		- 389 LDAP 轻型目录访问协议
		- 636 LDAP over SSL
		- 873 rsync 日志管理
		- 1080 Socks socks代理
		- 1521/tcp Oracle数据库
		- 3306/tcp,udp Mysql数据库
		- 3389 windows远程登录，RDP
		- 5432/tcp PostgreSQL数据库系统
		- 8080 WWW代理服务
		https://www.cnblogs.com/sztom/p/10810834.html
	2. 总结vi/vim使用方法
	3. vi/vim异常错误