# 虚拟软件使用方法（vmware）/远程连接排错/linux系统命令
# 课程回顾
	- 系统安装部署
		- 系统网络配置
			1. 网卡名称eth0  
			2. 网卡地址IP地址 网关配置	DNS:223.5.5.5/114.114.114.114
			3. 系统的主机名称进行修改
		- 系统分区配置
			1. 通用分区
			2. 特殊需求分区
			3. 灵活分区
		- 系统预装软件
			最小化安装，软件1236
		- 检查网络功能
			检查网卡配置 ip a
			检查网络通讯 ping
		- 远程连接配置 xshell
# 课程介绍
	- 虚拟软件使用方法
		软件启动多次，可能出现启动虚拟机启动失败，多实例
		关机，选择挂起虚拟主机
		虚拟主机快照
		虚拟主机删除 - 到配置文件中删除
	- 虚拟软件网络配置（虚拟软件网络模式）
		- 虚拟软件网络模式
			1. NAT网络模式
				虚拟主机和宿主机网络信息可以不一致 10.0.3.x 10.0.0.0
				不容易出现局域网中IP地址冲突
				其他宿主机不能直接访问宿主机的虚拟主机
			2. 桥接网络模式
				虚拟主机和宿主机网络信息一致 10.0.3.x 10.0.3.x
				其他宿主机可以访问其他宿主机的虚拟主机
			3. 仅主机模式
				虚拟主机网络仅能与宿主机或其他虚拟主机相连
				不能访问外网
	- 远程连接排错思路
		1. 网络链路通畅
			- ping
			- 不通畅的原因
				1. 物理线路的问题/物理主机被关闭了
				2. 网络安全设备拦截了ping的功能
					尝试ping同一网络中的其他主机
				3. 虚拟主机网卡地址是否设置正确
				4. 虚拟网卡有没有开启并且配置正确
				5. 虚拟主机的网络服务是否关闭
		2. 有网络安全策略进行组织访问
			1. 防火墙没有关闭
			2. ssh服务配置中也可以阻止用户远程连接
		3. 远程服务没有开启
			- 检查远程服务是否开启 telnet 192.168.90.200 22(ssh)
			ssh服务端口
				systemctl start ssh
			- 连接失败的原因
				1. 远程服务关闭
					systemctl start sshd
					systemctl status sshd
				2. 虚拟网络网卡设置出错
				3. 虚拟软件程序运行出问题
					检查虚拟软件服务是否正常
					windows +r -- service.msc
					
	- 系统管理的基础知识
		- 系统命令行提示组成
			1. 命令提示符
			# -- root
			$ -- 普通用户
			用户名称@主机名称 当前所在文件目录 #（命令提示符）
				ctrl+d 注销
		- 系统命令格式
			command params dict/file
		- 系统的目录结构
	- 系统的基础常见命令
		- 系统相关运行命令
			- 系统关机
				linux是多用户的系统
				# shutdown
				# shutdown -c 取消关机
				# shutdown -h (halt) time(minutes) [message] 短暂时间关机
				# shutdown -r [time]
				# shutdown -h now/0 立即关机
				# reboot 
				# halt 
				# poweroff 
		- 目录相关命令
			$ ls dict 检查某个目录是否存在
				$ ls -d dictname 查看目录
			$ mkdir dictname
				$ mkdir -p dict1/dict2/dict3 多级目录创建/忽略错误提示
			$ cd dict 切换目录
				相对路径/绝对路径(以根目录为参考)
				$ cd - 返回上一次所在的目录
				$ cd ~ 到家目录
			$ pwd 查看所在目录
		- 查看命令帮助信息
			$ man command
		- 快捷方式
			tab	命令或参数补充
			方向键上下	历史命令调用
	# 视频中today05
		- 命令操作
			- 查看文件信息
				$ ls -l 查看文件/目录详细信息
			- 创建空文件
				$ touch filename
			- 编辑文件
				1. 将文件打开直接编写
					$ vi/vim filename -- 编辑文件
				2. 将文件不用打开直接编辑
					将屏幕上的信息保存到文件
						$ echo "message" > file.txt
						$ cat > file.txt < "EOF" 注意cat不会自动创建文件
			- 查看文件内容
				$ cat filename
				$ cat -n filename 列出行号
			- 复制/保存
				$ cp source_file destination_file
				omitting directory 忽略目录
				$ cp -r .. 复制目录recursion
				$ \cp -r .. 强制目录覆盖（如果目录已存在）
			- 删除数据命令
				centos具有删除根目录的保护机制
				$ rm -rf (recursion force)
				$ \rm filename 强制删除命令
			- 移动目录或文件
				mv source dest
				mv在当前目录下移动，重命名
		- 快捷方式操作
			ctrl + l 清屏/但不会修改当前行的命令输入
			ctrl + c 中断程序
			ctrl + d 结束输入
			tab
			上下方向键
			终端快捷方式
				ctrl + a 将光标移动到行首
				ctrl + e 将光标移动到尾部
				ctrl + u 从后往前删除
				ctrl + k 从前往后删除
				ctrl + w 删除光标位置所在单词
				ctrl + p/ctrl+n 等效于方向上下键
				ctrl + y 粘贴有ctrl+u,ctrl+k,ctrl+w删除的内容
				ctrl + r 搜索历史输入命令
				快速移动
					按住ctrl+左右方向键 按照英文单词移动
		- 符号介绍
			> 重定向
			>> 追加重定向