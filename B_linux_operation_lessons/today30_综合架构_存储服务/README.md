# 课程介绍
	
# 课程回顾
	01. NFS存储服务概念介绍：
		NFS -- 实现文件共享，主要存储图片视频音频等内容信息
		
		存储服务的种类：
			用于中小型企业：实现数据共享存储
				FTP（文件传输协议）
					权限（用户认证的权限 存储目录的权限（用户））
					获取数据的方式 SSH服务
				samba 实现windows-- linux之间数据传输 Linux部署samba
				NFS 只能实现 linux -- linux之间数据传输
			用于门户网站：
				一个用户 -- 存储服务器
				上万个用户
				
				存储数据量大 -- raid
				-- 利用分布式存储
					多台存储服务器
					类似raid
				Moosefs (mfs)	比较落伍，学习使用
				GlusterFS
				FastDFS		企业应用较多
	02. NFS存储服务作用
		1. 实现数据共享存储
		2. 便于数据操作管理
		3. 节省购买服务器磁盘开销
	03. NFS服务部署流程
		RPC 远程过程调用程序 -- 相当于租房的中介（网络编程支持）
			租房的过程：
				租客 -- client
					最后和房东交接
				中介 -- RPC服务
					中介向租客反馈
				房源 -- NFS服务
					向中介注册
			-- 为什么要有RPC服务
				rsync客户端			rsync服务端
				服务端端口号：
				服务端IP
				
				NFS客户端			NFS服务端
				服务端口号
				！！ NFS存在多个端口号，随机端口号
				通过rpc服务收集服务请求 -- 端口号111
			
		服务端部署
			1. 下载安装软件
				rpm -qa | grep -E "nfs|rpc"
				yum install -y nfs-utils rpcbind
			2. 编写配置文件
				/etc/exports
				配置文件格式		01		02(03)
					01 设置数据的存储目录 /data
					02 设置网络白名单
					03	配置存储目录的权限信息，存储目录的一些功能
				/data   172.16.1.0/24(rw,sync)
			3. 创建一个存储目录
				mkdir -p /data
				- 权限修改
					chown nfsnobody:nfsnobody /data
			4. 启动服务程序
				注意启动顺序
					a 先启动rpc服务
						systemctl start rpcbind.service
						systemctl enable rpcbind.service
						netstat -tunlp | grep rpc 验证启动
					b 启动nfs服务
						systemctl start nfs
						systemctl enable nfs
						rpcinfo
		客户端部署
			[root@web01 ~]# mount -t nfs 172.16.1.31:/data /mnt
			mount: wrong fs type, bad option, bad superblock on 172.16.1.31:/data,
				   missing codepage or helper program, or other error
				   (for several filesystems (e.g. nfs, cifs) you might
				   need a /sbin/mount.<type> helper program)

				   In some cases useful info is found in syslog - try
				   dmesg | tail or so.
			1. 安装nfs服务软件
				yum install -y nfs-utils # 支持nfs文件类型
			2. 实现远程挂载共享目录
				mount -t nfs 172.16.1.31:/data /data
	04. NFS服务工作原理
		客户端：
			1. 建立TCP网络连接
			2. 客户端执行挂载命令，进行远程挂载
			3. 实现数据的远程部署
		
		服务端：
			1. 启动rpc服务， 开启111端口
			2. 启动nfs服务
			3. 实现nfs服务进程和端口号的注册
				只有重启服务后，才会重新注册端口号
			补充检查nfs服务端口注册信息
				rpcinfo -p 172.16.1.31/localhost(本地)
				100000    4   tcp    111  portmapper
				100000    3   tcp    111  portmapper
				100000    2   tcp    111  portmapper
				100000    4   udp    111  portmapper
				100000    3   udp    111  portmapper
				100000    2   udp    111  portmapper
				100024    1   udp  36302  status
				100005    1   udp  20048  mountd
				100003    3   tcp   2049  nfs
				100227    3   tcp   2049  nfs_acl
				100021    1   udp  51180  nlockmgr
				100021    1   tcp  46475  nlockmgr
	05. nfs服务的配置说明
		- 配置格式
			目录	主机/网段(权限)
			多个网段
				a
					/data	172.16.1.0/24(rw,sync)	10.0.2.0/24(rw,sync)
					systemctl restart nfs
				b
					/data	172.16.1.0/24(rw,sync)
					/data	10.0.2.0/24(rw,sync)
			man exports
			
		- 共享目录的权限和那些因数有关
			1）和存储目录的本身的权限有关
				755 属主：nfsnobody
			2）和配置文件中的权限配置有关
				/data	172.16.1.0/24(ro,sync) 只读
				squash
				anonuid
				anongid
			3）和客户端挂载命令参数有关 mount -o rw
		- NFS配置参数权限
			rw	-- 存储目录是否有读写权限
			ro 	-- 存储目录是否为只读权限
			sync -- 同步方式存储数据
				直接将数据存储到磁盘中 （数据可靠性高）
				优点：
			async -- 异步方式存储数据
				直接将数据保存到内存中	（存储速度快，存储效率高）
				秒杀服务 -- 磁盘io消耗大
					缓存服务器 -- 内存空间
					数据库
			用户身份转换：
				no_root_squash	-- 不要将root用户身份进行转换
					不用权限改变也可以存储数据，数据的属主不改变
				root_squash		-- 将root用户身份进行转换
					root用户的身份进行转换
				all_squash		-- 将所有用户身份进行转换
					所有用户可以将数据进行存储
					并且文件属主变为nfsnobody
				no_all_squash	-- 不要将所有用户身份进行转换
					改变用户权限
			操作演示all_squash：
				/data	172.16.1.0/24(rw,sync,all_squash)
				systemctl start nfs
		- 企业互联网公司如何配置NFS配置
			实际存储数据：
				数据进入web服务，会映射为www用户
				/www/data --(mount 172.16.1.31:/data)-- nfs服务器 --rsync 172.16.1.41::backup-- 备份服务器
			为保证数据能存
				no_all_squash -- 针对普通用户
				no_root_squash (转换成root_squash,会导致任意人员可以改变数据内容）
			- 保证网站存储服务器用户数据安全性：
				no_all_squash 需要进行配置 -- 设置共享用户，服务端和客户端用户 uid一致
				PS：共享目录权限改为www
					导致任何用户都无法访问
					两台服务器看用户是否相同，看用户uid
					多个用户使用相同的uid的用户
				root_squash 需要进行配置 root --- nfsnobody (默认转换），而实际的/data的管理用户改为了www
				-- 以上默认配置（很多服务默认配置都是从安全角度出发）
				/data	172.16.1.0/24(rw,sync,root_squash,no_all_squash)
		- 如何查看nfs的默认配置
			cat /var/lib/nfs/etab -- 记录nfs服务的默认配置记录文件
		- 若想root可以删除数据 -- 如何让root用户可以操作管理www用户管理的data目录 -- web服务器中
			root -- root_squash -- www -- 操作 
			/var/lib/nfs -- nfs的家目录（nfsnobody)
			anonuid=65534,anongid=65534 -- 指定默认映射用户
			
		- 企业中如何编辑nfs配置文件
			01. 通用方法
				/data 172.16.1.0/24(rw,sync)
			02. 特殊服务器 （让部分人员不能操作存储服务器，可以查看数据）
				开发人员只能看代码，不能修改代码
				/data 172.16.1.0/24(ro,sync)
			03. 修改默认的匿名用户
				/data 172.16.1.0/24(ro,sync,anonuid=xx,anongid=xx)
		nfs -- 无法只针对用户进行设置访问权限
		
		- nfs服务问题：
			01. nfs服务重启，挂载后创建数据比较慢
				服务重启方式不正确
				- 服务重启：
					01. restart 重启服务 -- 强制断开所有连接	用户感受不好
						服务完全重启，不管是否连接建立了
						每次重启服务都需要重新执行服务的配置
					02. reload 重新载入配置文件 -- 强制断开没有数据传输的连接	提升用户感受
						将没有数据传的断开
						有数据传的，则让它传完，最后再重新传完后再建立新的连接
	06. nfs客户端详细配置说明
		mount -t nfs 172.16.1.31:/data /mnt
		存储服务的目录实现自动挂载
		1. 利用rc.local
			echo "mount -t nfs 172.16.1.31:/data /mnt" >> /etc/rc.local
		2. 利用/etc/fstab
			vim /etc/fstab
			172.16.1.31:/data       /mnt    nfs     defaults        0 0
			特殊的服务已经开启了
		centos6： 无法实现网络存储服务自动挂载原因
			系统服务的启动顺序
			服务按照顺序依次启动  network -- sshd -- crond --- rsync -- rpcbind
			先加载/etc/fstab -- 再实现network服务 -- autofs服务
			
			autofs服务程序 -- 开机自动启动
				服务启动好后，重新加载fstab
		
		centos7： 无法实现网络存储服务自动挂载原因
			系统服务的启动顺序
			服务并行启动
			先加载/etc/fstab
		- 客户端mount参数说明：
			mount -o defaults 指定挂载参数
			defaults包含的参数：rw, suid, dev, exec, auto, nouser, and async
			rw --- 实现挂载后挂载点可读可写（默认）
			ro --- 实现挂载后挂载点为只读
			suid --- 在共享目录中可以让setuid权限位生效（默认）
			nosuid --- 在共享目录中所有的setuid权限位失效 （提高共享目录的安全性）
				演示：将cat命令移动到共享目录中的，使得普通用户可以通过cat命令查看/etc/passwd
				chmod u+s /data/cat
			exec --- 共享目录中的执行文件可以直接执行（默认）
				挂载的目录中的可执行文件（脚本，程序）可以直接被执行
			noexec --- 共享目录中的执行文件不可以直接执行
			auto --- 可以实现自动挂载（默认）
			noauto --- 不可以实现自动挂载
				mount -a 可以加载/etc/fstab实现自动挂载，即将未挂载的目录挂载上来
			nouser --- 禁止普通用户可以卸载挂载点 （默认）
			users --- 允许普通进行卸载挂载点
			
		- 客户端如何卸载
			- umount
			- umount -lf /mnt 强制卸载挂载点
				-l 不退出挂载点目录进行卸载
				-f 强制进行卸载操作
课程总结：
	1）NFS存储目录服务器概念
		共享存储，减少服务器主机磁盘的开销
	2）NFS存储工作原理图
	3）NFS存储服务部署
	4）NFS服务端详细配置说明
		服务端配置参数 xxx_squash
	5）NFS客户端详细配置说明
		如何实现自动挂载
		客户端挂载参数说明
		如何强制卸载共享目录
				
作业：
	- 实现fstab文件自动挂载的特殊服务是什么
	- mount 的user参数左右
	- NFS服务部署过程
		
				
				
				
			
				
			