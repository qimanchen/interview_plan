# 操作命令以及目录结构
# 课程回顾
	- 文件相关的命令
		cp 命令使用时，注意，当目标目录不存在时，那么对文件进行重命名（要检查文件目录是否存在
		cp test.txt ../today06/ 最后最好加上"/"
	- 快捷键的方式
		- 移动
			ctrl + a 移动到行首
			ctrl + e 移动到行尾
			ctrl + <- -> 以单词为单位进行移动
		- 剪切
			ctrl + u 从光标所在位置到行首进行剪切
			ctrl + k 从光标所在位置到行尾进行剪切
			ctrl + w 删除光标所在位置进行删除
		- 粘贴
			ctrl + y 将剪切的内容进行剪切
		- 锁定输出
			ctrl + s 将终端界面锁定
			ctrl + q 解锁界面的显示
		- 取得上一条命令的后一部分调取
			esc+. 
	- vi编辑一个文件
# 课程内容
	- 操作命令进行补充
	- 快捷方式的使用方法
	- vi的详细使用技巧
	- 系统的目录结构，系统文件进行解释说明
		windows按照盘符划分
		linux 一切从根开始
		- Linux挂载
			让用户可以将一个目录作为一个存储设备的挂载点，作为磁盘的入口
		linux系统中一切皆文件
		- 挂载过程
			1. 拥有一个存储设备，光驱
				/dev/cdron
			2. 使光驱加载光盘
			3. 需要将设备进行挂载才能看到内部的命令
				- 挂载命令格式
					# mount 挂载设备文件信息 挂载点（目录信息）
					mount /dev/sda1 /mnt
					ps：挂载点目录必须存在
			4. 卸载
				# umount 挂载点（目录信息）
	- 系统的基础目录结构
		FHS 文件标准 -- linux目录结构规范
		/bin -- /usr/bin的软连接 命令，二进制文件存放目录
		/sbin -- 只有root用户的命令
		/boot -- 系统引导程序+系统内核
		/dev -- 设备 光驱 磁盘
		/etc -- 配置文件目录
		/home -- 普通用户的家目录
		/root -- root用户的家目录
		/lib
		/lib64 -- 库文件存放目录（64位）
		/lost+found -- 临时存放文件系统
		/mnt -- 临时挂载点目录
		/opt -- 第三方软件安装
		/proc -- 虚拟目录，显示内存中信息（进程 服务信息 内核）目录中的数据都存储到内存中
		/etc/selinux selinux安全目录，配置文件
		/srv
		/sys 虚拟的目录，内存的信息
		/tmp 临时文件的存放位置
		/usr 存放程序的目录
		/var 经常变化的目录，系统日志，相关服务的文件
	- 详细了解目录结构中的重要信息
		- 网卡配置文件
			/etc/sysconfig/network-scripts/ifcfg-eth0
			- Type=Ethernet 指定网络类型 以太网Ethernet,FastEthernet
			- BOOTPROTO=none/dhcp 网络启动协议 如何让主机得到ip（none/static静态设置或dhcp自动获取）
			- NAME=eth0 主机网卡的名称，逻辑名称
			- UUID 设备的统一资源定位符
				# blkid 查看系统中设备的UUID
			- DEVICE=eth0 设备名称
			- ONBOOT=yes 设置网卡是否处于开启状态
			- IPADDR 静态配置的ip，表示主机身份
			- PREFIX=24 定义网络中可以有多少主机
				10.0.0.0/24
			- GATEWAY 不同网络间通信的接口
			- DNS1 别名/域名解析系统
		# nmtui
		# vi /etc/sysconfig/network-scripts/ifcfg-eth0 进行网卡信息调整
		linux系统中服务配置文件被修改后，不会立即生效
		需要重启服务后才会重新生效
		- 重启服务
			# systemctl restart network 这是重启网络服务
			- 重启单块网卡的服务
				# ifdown eth0
				# ifup eth0
			# ifdown eth0 && ifup eth0 前一个命令执行成功后在执行后一个命令
			# systemctl stop NetworkManager 关闭网络管理的服务
			# NetworkManager是响应nmtui的设置
		- DNS解析配置文件
			1. 直接修改网卡中的DNS参数
			2. 修改 /etc/resolv.conf中修改 nameserver 114.114.114.114
			重启网络服务时，这是以网卡服务中配置优先
		- dmesg | grep -i eth 可以查看网卡mac地址
# 课程作业
	1. 总结命令快捷方式
	2. 总结存储设备挂载
	3. 总结目录结构
			
			
