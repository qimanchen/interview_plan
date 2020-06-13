# 命令
	
# 内容
	1. 什么是daemon与服务service
		daemon
			守护进程，持续性，周期性执行的服务
			服务名称后面都有个d，如atd crontabd
		service
			系统为了实现某些功能而提供的一些服务
		1.1 systemV的init主要分类
			- 服务的启动脚本都放置在/etc/init.d中，
				/etc/init.d/daemon start
				/etc/init.d/daemon stop
				/etc/init.d/daemon restart
				/etc/init.d/daemon status
			- init服务的分类
				- stand alone
					常驻内存中，提供本机或用户的服务
				- super daemon
					inetd,xinetd所管理的socket进程
			- 服务的依赖
				init无法执行依赖启动
			- 执行等级分类
				0,1,2,3,4,5,6
				/etc/rc.d/rc[0-6]/SXXdaemon
			- 指定相应执行等级下，服务的开机启动
				chkconfig daemon on 开机启动服务
				chkconfig daemon off 开机不启动
				chkconfig --list daemon 查看服务是否开机启动
			- 执行等级的切换
				init run-level
		1.2 systemd
			- 平行处理所有服务，加速开机
				init的服务启动，是一项一项依序启动
			- 通过systemd即可管理所有的服务
			- 服务的依赖性自我检查
			- 根据daemon功能分类
				systemd将服务分为 service，socket，target，path，snapshot，timer
			- 多个daemons集合成一个服务
			- 向下兼容init服务
			- 缺点
				systemd都是通过systemctl来管理的，具有语法的限制
				如果服务不是通过systemctl启动的，那么systemd无法检测到该服务
			- systemd的设置文件
				/usr/lib/systemd/system 类似/etc/init.d下的文件，每个服务的启动脚本
				/run/systemd/system/ 系统执行过程中产生的服务脚本，这些脚本优先级更高
				/etc/systemd/system/ 类似于/etc/rc.d/rc5.d/SXX,执行优先级比前面两者更高
				- 修改某个服务的启动设置，到/usr/lib/systemd/system/中
				- /etc/systemd/system/ 仅是真正执行脚本的链接
			- systemd的unit分类
				.service 系统服务，服务器本身的服务以及网络服务等
				.socket 内部程序通信服务
				.target 多个unit的集合，如multi-user.target
				.mount
				.automount 文件系统挂载服务，如网络的自动挂载，nfs文件系统挂载
				.path 打印服务，需要检测特定的目录
				.timer 定时服务，类似于anacrontab
				
	2. systemctl管理服务
		2.1 systemctl管理单一服务启动/开机自启，查看状态--service
			systemctl [command] [unit]
				- commnd
					start
					stop
					restart
					reload 重新载入设置
					enable
					disable
					status
					is-active
					is-enabled
			- 几种常见状态
				active(running) 正在执行
				active(exited)	仅执行一次
				active(waiting)	正在执行，但需要等待其他事件执行完成
				inactive	服务没有执行
			- 开机是否自启状态
				enabled	开启自启
				disabled 开机不自启
				static 这个daemon不可以自己启动，但可能被其他服务调用（依赖性服务）
				mask 这个daemon无论如何都无法被启动，服务被注销（非删除）
					systemctl unmask 改回原来状态
					systemctl mask 注销服务
		2.2 systemctl观察系统上的服务
			systemctl [command] [--type=TYPE] [--all]
				- command
					list-units 列出目前启动的unit，加上--all，列出没有启动的
					list-unit-files /usr/lib/systemd/system/文件中设置的内容
					--type=TYPE 列出指定unit type的服务
		2.3 systemctl管理不同的操作环境 -- target
			systemctl list-units --type=target --all
				graphical.target 图形界面
				multi-user.target 文字界面
				rescue.target 
				getty.target 可以修改tty的数量
			systemctl [command] [unit.target]
				- command
					get-default 取得当前的target
					set-default 设置默认target
					isolate 切换到后面的模式
			systemctl reboot
			systemctl rescue
		2.4 systemcl查看服务的依赖关系
			systemctl list-dependencies [unit] [--reverse]
				--reverse 谁在使用这个unit
		2.5 与systemctl的daemon运行有关的文件目录
			/usr/lib/systemd/system/ -- 预设启动脚本，修改到/etc/systemd/system/
			/run/systemd/system/ -- 系统运行中所产生的脚本
			！！/etc/systemd/system/ -- 系统需求所建立的执行的脚本
			/etc/sysconfig/ -- 服务的一些初始化的设置文件
			/var/lib/ -- 会产生数据的服务，将数据放入在此目录中
			/run/ -- lock file,PID file
			
			- 服务端口
				/etc/services 服务与端口对应
		2.6 关闭网络服务
			
	3. systemctl对service类型的设置文件
		3.1 systemctl相关设置目录
			修改/etc/systemd/system/
			- vsftpd.service
				/etc/systemd/system/vsftpd.service.d/custom.conf
					在/etc/systemd/system/下加入相同设置文件名后面加.d
					同样该目录下的配置文件名为*.conf
				/etc/systemd/system/vsftpd.service.wants/* -- 启动该服务后，最好启动的服务
				/etc/systemc/system/vsftpd.service.requires/* -- 启动该服务前，必须先启动的服务
		3.2 相关systemctl设置文档的内容
			- /usr/lib/systemd/system/sshd.service
				[Unit] -- 这个unit的解释、执行服务的依赖关系
				[Service] -- 这个unit执行相关指令的参数 -- 不同unit type的设置
				[Install] -- 此unit要挂载在哪个target下面
		3.3 通过设定文件，实现一个服务双开
		3.4 getty多重的重复设置方式
			/usr/lib/systemd/system/getty@.service
				-/sbin/agetty --noclear %I $TERM
				原始文件：服务名称@.service
				执行文件：服务名称@范例名称.service
			- 减少tty的数量
				/etc/systemd/logind.conf
					- NAutoVTs=4
					- ReserveVT=0
				新增一个tty
					systemctl start getty@tty8.service
		3.5 自己制作服务
		
	4. systemctl对timer的设置
		- timer.target
		systemd可以实现到秒甚至是毫秒单位
		systemctl daemon-reload
		
	5. centos7开机启动服务简易说明
		chronyd 系统校准时间服务
		rc-local 开机自启
		
# 练习