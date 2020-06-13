# 课程介绍
	1）实现实时同步数据的原理
	2）实现实时同步数据的方法
		a 部署好rsync守护进程服务
		b 部署好inotify监控服务
		c 部署好sersync实时同步服务
	3）实现实时同步数据的验证
# 课程回顾
	1）NFS存储服务概念介绍
		a 实现数据的共享存储
		b 节省成本（磁盘）
	2）NFS存储服务工作原理
		a 部署好一台存储服务器，设置好存储目录
		b 客户端利用网络挂载的方式进行挂载存储目录
		c 将数据存储到相应的数据中  --- 实际存储到存储服务器中
	3）NFS服务部署流程
		RPC：类似租房中介 NFS服务启动会有多个进程多个端口（随机端口），客户端不方便连接服务器
		rpc      10934     1  0 02:42 ?        00:00:00 /sbin/rpcbind -w
		rpcuser  11074     1  0 02:43 ?        00:00:00 /usr/sbin/rpc.statd # 检查数据存储一致性
		root     11082     2  0 02:43 ?        00:00:00 [rpciod]
		root     12102     1  0 12:34 ?        00:00:00 /usr/sbin/rpc.idmapd # 让用户做映射转换
		root     12103     1  0 12:34 ?        00:00:00 /usr/sbin/rpc.mountd # 权限管理验证
		root     12108     2  0 12:34 ?        00:00:00 [nfsd4_callbacks]
		root     12112     2  0 12:34 ?        00:00:00 [nfsd]
		root     12113     2  0 12:34 ?        00:00:00 [nfsd]
		root     12114     2  0 12:34 ?        00:00:00 [nfsd]
		root     12115     2  0 12:34 ?        00:00:00 [nfsd]
		root     12116     2  0 12:34 ?        00:00:00 [nfsd]
		root     12117     2  0 12:34 ?        00:00:00 [nfsd]
		root     12118     2  0 12:34 ?        00:00:00 [nfsd]
		root     12119     2  0 12:34 ?        00:00:00 [nfsd]
		服务端部署
			安装 nfs-utils rpcbind
			配置/etc/exports
			设置系统环境
				创建存储目录，并修改属主服务
			启动服务
				rpcbind
				nfs
		客户端部署
			安装nfs服务软件
			实现网络存储服务挂载
		NFS服务挂载不上排查方法
		服务端进行排查
			1. 检查nfs进程信息是否注册
				rpcinfo -p localhost/172.16.1.31
				问题原因：
					服务启动顺序不对，没有启动nfs服务
			2. 检查有没有可用存储目录
				showmount -e 172.16.1.31 查看是否有共享的目录
				问题原因：配置文件，重启nfs服务
			3. 在服务端进行挂载测试
				是否能够在存储目录中是否创建或删除文件
		客户端测试：
			1. 检查nfs进程信息是否注册
				rpcinfo -p localhost/172.16.1.31
				问题原因：
					服务启动顺序不对，没有启动nfs服务
			2. 检查有没有可用存储目录
				showmount -e 172.16.1.31 查看是否有共享的目录
				问题原因：配置文件，重启nfs服务
				网络问题
					ping
					telnet
	4）NFS服务端配置参数
		xxx_squash
	5）NFS客户端配置说明
		mount -t
		实现开机自动挂载
			/etc/rc.local 文件要有执行权限
			/etc/fstab 实现fstab实现开机自动挂载nfs，必须让remote-fs.target服务开机自启
				centos7 必须启动 remote-fs.target
				centos6 必须启动 netfs
		需求问题：如何找到一台服务中开机自动启动的服务
			/etc/systemd/system/multi-user.target.wants/
		
# 课程内容
	01. 实时同步服务原理/概念
		1. 确定要传的数据 rsync
		2. 监控存储目录数据变化
			inotify
		3. 监控到数据用变化，利用rsync进行传输 -- sersync实时同步
		
		-- 1）需要部署好rsync守护进程服务，实现数据传输
		-- 2）需要部署好inotify服务，实现目录中数据变化监控
		-- 3）将rsync服务和inotify服务建立联系，将变化的数据进行实时备份传输
	02. 实时同步服务部署
		1）部署好rsync守护进程
			服务端配置操作
			客户端配置操作
		2）部署inotify监控服务
			a 安装软件
				yum install -y inotify-tools
			b 熟悉命令的使用
				rpm -ql inotify-tools
				/usr/bin/inotifywait --- 监控目录数据信息变化
				/usr/bin/inotifywatch --- 对监控的变化信息进行统计
					文件改变的次数
			inotifywait命令使用方法：
				inotifywait [参数] 监控的目录
				-m|--monitor  --- 实现一直监控目录的数据变化
				-r|--recursive --- 进行递归监控
					不加该参数，子目录中的部分监控
				-q|--quiet --- 尽量减少信息的输出
				--format <fmt> --- 指定输出信息的格式
					inotifywait -mqr --timefmt “%F" --format "%T  %w %f 事件信息：%e"-e CREATE /data
					--format
						%T 时间信息
						%w 监控变化的数据的目录信息
						%f 文件
						%e 事件信息 CREATE
						
				--timefmt --- 指定输出的时间格式
				-e|--event --- 指定监控的事件信息
					inotifywait -m -e CREATE /data
					监控的事件
						create
						delete
						moved_to
						close_write
			创建文件进行监控信息
				--- 一个文件被创建
				--- 打开创建的文件
				--- 修改文件的属性信息
				--- 保存关闭一个文件
			删除文件监控信息输出
				--- 删除文件
			修改文件监控信息输出
				--- 创建
				--- 打开
				--- modify
				--- close-write
			sed命令修改文件原理
				--- 打开文件
				--- 创建出一个临时文件（内存）
				--- 临时文件进行打开
				--- 读取源文件内容
				--- 修改临时文件
				--- 临时文件属性变化
				--- 不编辑直接关闭源文件
				--- 写入关闭临时文件
				--- 将临时文件移除
				--- 移入一个新的user10源文件
			inotify事件信息
				access
				modify
				attrib
				close_write
				close_nowrite
				close
				open
				moved_to
				moved_from
				move -- 数据移动
				create -- 创建
			inotify监控命令格式
				inotifywait -mrq --timefmt "%F" --format "%T  %w %f 时间信息:%e" -e CREATE /data
				create创建,delete删除,moved_to移入,close_write修改
			企业应用：防止系统重要文件要被破坏
				需要用到inotify进行实时一直监控 /etc /var/spool/cron/root
			rpm -e inotify-tools --nodeps
		3）部署sersync同步服务
			a 下载安装软件,先下载，再上传到linux服务器中
				https://github.com/wsgzao/sersync
				上传linux服务器
				rz -y
				ps：软件安装包尽量保存到/server/tools
			b 解压软件压缩包
				[root@nfs01 sersync-master]# tree sersync_installdir_64bit/
				sersync_installdir_64bit/
				└── sersync
					├── bin		--- sersync软件命令目录
					│?? └── sersync
					├── conf	--- sersync软件配置目录
					│?? └── confxml.xml
					└── logs	--- sersync软件日志目录
				mv sersync /usr/local
			c 编写配置文件
				vim conf/confxml.xml
				实现数据过滤
					<filter start="false">
						<exclude expression="(.*)\.svn"></exclude>
						<exclude expression="(.*)\.gz"></exclude>
						<exclude expression="^info/*"></exclude>
						<exclude expression="^static/*"></exclude>
					</filter>
					排除指定数据信息不要进行实时传输同步
				inotify：
					<inotify>
						<delete start="true"/>
						<createFolder start="true"/>
						<createFile start="false"/>
						<closeWrite start="true"/>
						<moveFrom start="true"/>
						<moveTo start="true"/>
						<attrib start="false"/>
						<modify start="false"/>
					</inotify>
					加载inotify事件信息 -- 需要监控的事件
				核心部分
					<localpath watch="/data"> -- rsync的备份目录
						<remote ip="172.16.1.41" name="nfsbackup"/> -- 备份服务器的地址，模块信息
						<!--<remote ip="192.168.8.39" name="tongbu"/>-->  -- 多个备用服务器
						<!--<remote ip="192.168.8.40" name="tongbu"/>-->
					</localpath>
					<rsync>
						<commonParams params="-az"/> -- rsync参数备份
						<auth start="true" users="rsync_backup" passwordfile="/etc/rsync.passsword"/> 指定rsync认证用户 指定rsync认证文件
						<userDefinedPort start="false" port="874"/><!-- port=874 -->
						<timeout start="false" time="100"/><!-- timeout=100 -->
						<ssh start="false"/>
					</rsync>
			d 启动sersync
				sersync/bin/sersync
				chmod a+x sersync/bin/sersync
				export PATH=$PATH:/usr/local/sersync/bin
				
				sersync 
				参数-d:启用守护进程模式
				参数-r:在监控前，将监控目录与远程主机用rsync命令推送一遍
					进行同步测试
				参数-o:指定配置文件，默认使用confxml.xml文件
					-o /usr/local/sersync/conf/confxml.xml 可以编写多个配置文件
					
				sersync -dro /usr/local/sersync/conf/confxml.xml	# 启动实时同步服务
				默认无差异备份
				关闭服务
					ps -ef|grep sersync
					kill pid
					
					yum install -y psmisc
					killall sersync		# 停止实时同步服务
				#开机自启动
					/etc/rc.local -- sersync -dro /usr/local/sersync/conf/confxml.xml
		05. 实时同步服务概念总结
			1）实现实时同步的原理
				监控目录数据变化 --- inotify
				将数据进行传输 --- rsync
				将监控和传输进行整合 --- sersync
			2）实现实时同步部署方法
				1. 部署rsync守护进程
				2. 部署inotify软件
				3. 部署sersync软件
作业：
	--- 实时同步软件
		数据库实时同步
		windows -- windows同步
	--- 批量管理服务ansible 安装过程 简单配置 应用（模块 剧本）

					


		

		