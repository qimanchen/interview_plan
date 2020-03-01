# 系统安装部署
	- x86_64 系统架构（识别内存的能力不同
		i386 2的32次方=4G
		DVD
	- 介绍部分
		1. 安装部署操作系统
			步骤
				1. 选择引导部分，troubleshooting 排错
					centos7系统网卡名称，默认系统的网卡名称 ens33
					- 调整网卡名称
						tab，输入net.ifnames=0 biosdevname=0
				2. 对系统语言设置
					English(United States)
				3. 对系统安装过程进行配置
					- 系统网络的配置
						systems - network
					- 系统分区的配置
						- 如何对linux系统分区
							1. 通用分区方案
								/boot	引导分区 200M
								swap	交换分区 建议内存的1.5倍，若大于8G==8G 1G
								/ 根分区 剩余的空间
							2. 数据信息比较重要的分区方案
								/boot 200M
								swap 1.5*内存
								/	20G~200G
								/data	剩余空间
							3. 灵活的分区方案
								/boot 200M
								swap
								/ 20G~200G
								剩余空间不分，系统内在进行配置
					- 系统安全的配置 - 关闭 系统的安全策略配置
						system -kdump 将当机错误信息记录
						system - security policy
					- 系统时区的设置
					- 系统软件包的安装
						最小化安装，1236
					- 创建系统用户
						系统管理用户
						普通用户
			运维工程流程
				1. 准备/检查好环境
				2. 进行操作前的备份 网络配置文件
				3. 进行配置之后注意保存
				4. 配置完成需要检查 -- cp 重要文件 /data
				5. 编写项目文档
		2. 系统中的网络设置
			- 网络检查
				检查网卡配置 ip address show/ip a 
				测试网络连通性 ping www.baidu.com
				ctrl+l 清屏
			- 网络不通
				网卡地址和虚拟主机的网卡不统一
				网卡和DNS的信息不正确
			- 处理网络配置
				nmtui 图形界面修改网卡配置
					edit
				IP地址：网络通讯标识信息
				子网掩码：在局域网中，可以有多少个主机
				网关地址：从一个局域网到另一个局域网的接口
				- 使配置可以生效
					systemctl restat network 重启网络服务
			- 向日葵软件
				远程控制
		3. 利用远程工具进行远程shell
			- Xshell 免费，功能实用
				sesions可以进行复制，并发送给其他人使用
			- scureCRT 收费
			- putty 功能简单
		4. 系统基本命令操作