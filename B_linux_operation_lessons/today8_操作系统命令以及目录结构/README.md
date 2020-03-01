# 系统结构及命令
# 课程回顾
	- 变量信息配置文件
		/etc/profile
		/etc/bashrc, 变量和别名的配置，最好在此文件中
		- 变量
			1. 普通变量 简化脚本的编写
			2. 环境变量 系统的环境配置有关
		- 别名
			1. 让命令操作更简单
			2. 让危险的操作更安全（rm）
			实现rm隐藏
				1. 修改/etc/profile文件（加入alias）
				2. 重新加载配置文件中
				3. 修改用户家目录中的~/.bashrc
			总结 系统中配置相关的文件
				01 /etc/profile == /etc/bashrc 国法，全局生效
				02 ~/.bashrc == ~/.bash_profile 家规，指定用户生效
					用户配置更优先
		
# 课程介绍
	补充：
		系统中将命令分为两个大类
			1. 内置命令		所有系统都有的命令
				# help
				# type command 检查某个命令是否为内置命令
			2. 外置命令 	需要进行安装
		
	- 重要目录中数据文件
		- 用户登录之后提示文件
			/etc/motd
			- 作用
				可以对操作系统的注意事项进行说明
			
		- 用户登录之前提示文件
			/etc/issue
			/etc/issue.net -- 网络登录
			- 如何清空文件
				echo "">/etc/issue -- 清空文件
				>/etc/issue -- 清空文件
		- 和程序软件安装相关的目录
			/usr/local
		- 日志文件保存目录
			/var/log/
				两个重要的系统文件
					messages -- 记录系统或服务运行的状态信息 和错误信息
					secure -- 记录用户登录信息，进行监控，检查是否有过多失败的记录
						- 动态查看日志文件命令
							tail -f /var/log/rescue
							tail 默认看倒数10行信息
					Feb 16 22:38:52 qiman polkitd[2557]: Loading rules from directory /etc/polkit-1/rules.d
					01				02		03			04
					01 用户登录时间
					02 登录的主机名称
					03 使用什么方式登录
					04 登录情况说明
						a 正确登录
						b 错误登录
	- 操作系统安装软件方法
		- 系统中如何安装软件
			1. yum安装软件 简单快捷
				从远程仓库中安装
				- 指定软件仓库的软件，yum源文件
					1. 本地配置yun源文件
						/etc/yum.repos.d/
							Centos-Base.repo
						- 更新阿里云
							curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
							从阿里云下载源，更新默认源
					2. 安装软件命令
						yum install 软件名称
						yum install -y 软件
						yum install -y vim wget net-tools nmap bash-completion
							bash-completion 可以补全centos7的提示
				yum安装软件的问题
					排错流程
						01. 能不能访问外网
							a 能不能访问外网ip
								ping ip(dns ip)
							b 能不能访问外网名称
								修改网卡dns设置
								修改/etc/sysconfig/network-scripts/ifcfg-eth0
						02. 检查是否已经有下载的进程
							查看进程：ps -ef PID进程编号
							关闭进程：kill -9 pid 强制删除
						03. yum源文件被修改调整了
			2. rpm安装软件 需要有软件安装包
			3. 编译安装软件 可以灵活调整
	- 如何查看系统一些硬件信息
		CPU
			- 利用文件进行查看
				/proc/cpuinfo
				model name	: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz -- cpu品牌型号
				physical id	: 0 -- 表示cpu颗数 1颗
				processor	: 0 -- 表示cpu的核数 1核 编号从0开始
				cpu cores	: 1
			- 利用命令查看
				lscpu -> 调取cpuinfo文件中的内容
				Socket(s):             1 -- 显示cpu颗数
				Core(s) per socket:    1 -- 每个cpu有几核
				CPU(s):                1 -- 整个系统有几核
		内存：内存使用情况
			1. 利用文件查看
				cat /proc/meminfo
				MemTotal:        2047164 kB -- 内存总的容量
				MemFree:         1569828 kB -- 内存空闲的总量
				MemAvailable:    1750296 kB -- 内存可用容量
				Buffers:            2076 kB
				Cached:           303516 kB
				SwapCached:            0 kB
			2. 命令
				free -h
		磁盘信息/挂载信息
			1. 文件
				cat /proc/mounts
			2. 命令
				df -h
		负载
			1. 文件
				cat /proc/loadavg
					0.00 0.01 0.05 2/105 4212 1分钟，5分钟，15分钟
					负载值和cpu核数有关
					服务器4核 -- 负载值为3左右，就要关注
			2. 命令
				w
	- vi使用方法
# 课程知识总结
	1. 环境变量和别名配置文件
		/etc/profile /etc/bashrc
		~/.bash_profile ~/.bashrc 优先
	2. 如何在系统中安装软件
		yum安装软件
			1. 更新yum源
				/etc/yum.repos.d/CentOS-Base.repo
			2. 直接下载安装软件
	3. 查看硬件信息
		cpu lscpu
		内存 free
		负载 w
		磁盘 df

课程作业
	1. 课程回顾
	2. 命令总结
	3. vim的使用技巧
		
		
		
