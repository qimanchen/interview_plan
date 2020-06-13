# 课程回顾
	1. rsync守护进程的部署
		服务端部署
			1. 安装服务
			2. 编写配置文件
			3. 配置环境
				创建虚拟用户
					用来管理备份存储目录
				创建保存目录
				创建认证密码文件
			4. 启动服务
		客户端部署
			创建认证密码文件，并修改权限，只有密码信息即可
			进行免交互测试
	2. rsync备份传输数据的原理
		a 有用户的身份装换 其他所有用户 -- rsync
		b 用户存储数据的权限 （目录本身权限755 目录的属主信息rsync）
	3. rsync服务的常见错误
	4. rsync命令的参数信息 -av z（压缩数据）
	5. rsync服务的企业应用
		多模块
		服务排除功能 --exclude
		服务的备份目录的创建
		服务的列表功能
		服务的策略控制功能
		服务的无差异同步备份
# 课程介绍
	1. 根据需求搭建环境
	2. 按照需求编写脚本
	3. 进行功能测试
	4. NFS存储服务
# 课程内容
	1. 全网备份项目环境配置
		nginx web服务器			10.0.2.17/24		172.16.1.17/24		web01
		nfs						10.0.2.31/24		172.16.1.31/24		nfs01
		rsync					10.0.2.41/24		172.16.1.41/24		backup
		
		要求：
			每天晚上00点整在web服务器上打包备份系统配置文件、网站程序目录以及访问日志并通过rsync命令
			推送备份服务器backup上备份保留（备份思路可以先按本地日期打包，然后再推送到备份服务器backup上）
			nfs服务器同web服务器，实际工作中就是全部服务器
		具体要求：
			1. 所有服务器的备份目录必须都为/backup
				web01 nfs01 backup
			2. 要备份的系统配置文件包括但不限于
				/var/spool/cron/root
				/etc/rc.local
				/server/scripts
				/etc/sysconfig/iptables
				
				web01 nfs01
			3. web服务器站点目录 /var/html/www
			4. web服务器A访问日志路径/app/logs
			
			5. web服务器保留打包后的七天的备份数据即可（本地保留不能多于7天）
			6. 备份服务器上，保留每周一的所有数据副本，其它要保留6个月的数据副本
				backup
				部署好服务
				
				
			7. 备份服务器上要按照备份数据服务的内网ip为目录保存备份，备份的文件要按照时间名称保存
			
			8. 需要确保备份数据的完整性，完整性检查，把备份的成果与失败的结果发送给系统管理员（发送邮件）
				backup
			
			备份客户端要完成的工作
			mkdir -p /backup
			mkdir -p /server/scripts
			touch /etc/sysconfig/iptables
			
			# backupfile.txt
			/var/spool/cron/root
			/etc/rc.local
			/server/scripts
			/etc/sysconfig/iptables
			
			cat /backup/backupfile.txt | xargs tar zcvhf /backup/system_backup.tar.gz
			# 参数h 把链接文件的源文件进行压缩
			# 压缩完要检查
				备份后有软链接文件
			# 进入根目录下，采用相对路径的目录进行备份
			cd /
			tar zchf /backup/system_backup_$(date +%F_week%w -d -1day).tar.gz ./var/spool/cron/root ./etc/rc.local ./server/scripts ./etc/sysconfig/iptables
			
			# 两个web站点目录和日志目录要分开存储
				tar zchf /backup/www_backup_$(date +%F_week%w -d -1day).tar.gz ./var/html/www
				tar zchf /backup/www_log_backup_$(date +%F_week%w -d -1day).tar.gz ./app/logs
			find /backup -type f -mtime +7 | xargs rm
			
			# 指定客户端的目录 -- 目录结构一致
			
			rsync -avz /backup/ rsync_backup@172.16.1.41::backup/172.16.1.31/ --password-file=/etc/rsync.password
			mkdir -p /backup/172.16.1.31
			rsync -avz /backup/ rsync_backup@172.16.1.41::backup --password-file=/etc/rsync.password
			# md5sum
				find /backup/ -type f -mtime -1 ! -name "finger"| xargs md5sum > /backup/finger.txt
				md5sum -c 指纹文件命令执行原理
					# 打开一个指纹文件，将信息记录到缓存中
					# 根据指纹文件的路径信息，生成MD5数值信息
					# 将新生成md5数值和原有指纹文件中的数值进行比较
					# 如果相同 ok 否则 false
					
				
			
			服务端要完成的工作
			mkdir -p /backup
			
			find /backup -type f -mtime +180|xargs rm
			find /backup -type f -mtime +180 ! -name "*week1.tar.gz" | rm# 保留周一的数据
			# 单台主机备份验证
			md5sum -c /backup/172.16.1.31/finger.txt
			
			find /backup/ -type f -name "finger.txt" | xargs md5sum -c
			find /backup/ -type f -name "finger.txt" | xargs md5sum -c &> /tmp/check.txt
			mail -s "发送测试" 1033178199@qq.com < /tmp/check.txt
	4. 编写全网备份脚本
		客户端脚本
			#/bin/bash
			
			# create backup dir
			mkdir /backup/172.16.1.31 -p
			# tar backup data
			cd /
			tar zchf /backup/172.16.1.31/system_backup_$(date +%F_week%w -d "-1day").tar.gz ./var/spool/cron/root ./etc/rc.local ./server/scripts ./etc/sysconfig/iptables
			# del 7 day ago data
			find /backup -type f -mtime +7 | xargs rm
			# create finger file
			find /backup/ -type f -mtime -1 ! -name "finger"| xargs md5sum > /backup/172.16.1.31/finger.txt
			# backup push data info
			rsync -avz /backup/ rsync_backup@172.16.1.41::backup --password-file=/etc/rsync.password
			
			# 脚本目录
			/server/scripts
			# 执行脚本
				sh client_backup.sh
		服务端脚本
	5. 实现自动完成全网数据备份（定时任务）
		crontab -e
		0 0 * * * /bin/bash /server/scripts/backup.sh &>/dev/null
		
		服务端的时间一定要晚
		测试检验脚本 sh -x 脚本信息
	6. 还有什么完善余地
			补充：
				保留周一数据的方法
					a 在数据名称信息后加上周的信息
						%A Monday
						tar zchf /backup/www_backup_$(date +%F_week%w -d "-1days").tar.gz ./var/html/www
					b 在服务端进行检查，将每周一传输的数据进行单独保存
						
				如何验证数据完整性
					md5sum /etc/hosts # 生成MD5验证码
				如何实现发送邮件
					让linux连接网易邮箱
					让163邮箱进行发 -- 用qq邮箱进行收
						163邮箱配置
						POP3/SMTP/IMAP
							IMAP/SMTP -- 近30天
							开启客户端删除邮件提醒
							smtp.163.com
						客户端的授权密码
							DZGQZOMSURHTOUOZ
					a 配置163企业邮箱
					b 编写linux服务端邮箱服务配置文件
						vim /etc/mail.rc
						set from=18770917247@163.com smtp=smtp.163.com
						set smtp-auth-user=18770917247@163.com smtp-auth-password=DZGQZOMSURHTOUOZ smtp-auth=login
					systemctl restart postfix.service
					测试
						echo "testing" | mail -s "发送测试" 1033178199@qq.com
						# 多行内容
							mail -s "发送测试" 1033178199@qq.com < /etc/hosts
						
							
			