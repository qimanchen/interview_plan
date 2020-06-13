# 第十五章
# 命令
	
# 内容
	1. 什么是定时工作
		01. Linux定时工作的种类 at cron
			- 每隔一个时间
			- 突发性，单次
			- at atd服务支持 单次
			- crontab crond服务支持 循环
				crontab -e
				vim /etc/crontab
		02. centos 系统常见的定时任务
			- 登录档备份(log rotate)
			- 登录档分析logwatch任务
			- 建立locate数据库
				/var/lib/mlocate
				updatedb
			- man page查询数据库建立
				mandb
			- rpm软件目录
			- 删除临时文件
	2. 仅执行一次的定时工作
		01. atd启动与at运行方式
			systemctl restart atd 重启服务
			systemctl enable atd 设置开机自启
			- 运作方式
				实际内容写入到/var/spool/at目录中
				a 先确认/etc/at.allow中是否有该用户
				b 如果/etc/at.allow不存在，找at.deny 不存在该用户
					- 只存在/etc/at.deny 表示主机上所有的人都可以使用
				c 如果两个文件都不存在，那么只用root可以使用at这个指令
		02. 实际执行单一定时任务
			at -[mldv] Time
				-m at任务完成后，发邮件通知
				-l at -l == atq 显示系统上的at任务
				-d at -d == atrm 取消一个at任务
				-v 
				Time:
					HH:MM 04:00
					HH:MM YYYY-MM-DD 04:00 2015-07-30
					HH:MM[am|pm] [Month] [Date] 04pm July 30
					HH:MM[am|pm] + number[minutes|hours|weeks] now + 5 minutes, 04pm + 3days
			at -c 工作号码， 列出具体工作指令内容
			- 实例
				# at now + 5 minutes
				at> /bin/mail -s "testing at job" root < /root/.bashrc
				at> <EOF> ctrl + d
			- at 可以在一个工作中输入多个指令
			- at中命令使用绝对路径
			- at执行的输出信息都会发送到mailbox中去
			- at可以背景中执行
			- at工作管理
				atq 查看
				atrm jobnumber 删除 
			- batch 系统空闲时才执行背景任务
				- 当cpu的负载小于0.8时，才执行
				- uptime查看负载
				- batch设置任务，atq查看
			- 执行单位是分钟
	3. 循环执行的定时工作
		- cron(crond)
		01. 使用者设置
			/etc/cron.allow
			/etc/cron.deny
			- 指令内容记录到 /var/spool/cron中
			crontab [-u username] [-l|-e|-r]
				-u 只用root可以执行，帮其他用户建立或删除crontab任务
				-e 编辑
				-l 查看
				-r 移除所有crontab任务，如果只移除单个，则使用crontab -e
			- 格式
				分 时 日 月 周 command
				* 任何时刻
				, 分隔时间段
				- 时间范围
				/n 每隔n
		02. 系统设置定时任务 /etc/crontab, /etc/cron.d/*
			系统，只需要编辑/etc/crontab
			cron会每分钟读取一次/etc/crontab和/var/spool/cron中的内容
			- 当修改完/etc/crontab时，不会执行任务，那么systemctl restart crond
			- /etc/crontab文件说明
				MAILTO=root 任务资讯发送给那个用户
				PATH=
			- crond的设置文件
				/etc/crontab
				/etc/cron.d/* -- 系统定时清除一些任务
					类似于/etc/crontab
				/var/spool/cron/* -- 用户相关的
			- 在 /etc/cron.hourly/中的必须是可以被直接执行的指令脚本
			- crontab -e 个人执行
			- vim /etc/crontab 系统管理员
				run-part轮询执行脚本
			- vim /etc/cron.d/newfile 自己开发的软件
		03. 一些注意
			- 资源分配不均问题
				1,6,11,16,21,26,31,36,41,46,51,56 * * * * root  CMD1
				2,7,12,17,22,27,32,37,42,47,52,57 * * * * root  CMD2
			- 取消不要输出的项目 &> /dev/null
			- 安全检查 /var/log/cron
			- 日期与周不要同时出现
				
	4. 可唤醒停机期间的定时任务
		01. 什么是anacron
			anacron每小时被crontab执行一次，查看是否有超期的任务
			anacron会分析时间，比较上次执行anacron和当前时间
		02. anacron与/etc/anacrontab
			anacron 放在/etc/cron.hourly
			anacron [-sfn] [job]
				-s 开始一连续的执行工作
				-f 强制执行
				-n 立即执行未执行的任务
			anacron -u [job]
				-u 更新时间戳
				job /etc/anacrontab中定义的各项工作名称
				0anacron 优先执行
			- /etc/anacrontab
				#period in days   delay in minutes   job-identifier工作定义名称   command
				1	5	cron.daily		nice run-parts /etc/cron.daily
					时间戳相差的天数，如果超过了这个天数，则开始执行，没超过则不执行
					延迟时间：如果超过了时间，则延迟执行，避免资源冲突
					工作名称：/var/log/cron中记录
				7	25	cron.weekly		nice run-parts /etc/cron.weekly
				@monthly 45	cron.monthly		nice run-parts /etc/cron.monthly
				RANDOM_DELEY=45 随机给与最大延迟时间，单位为分钟
				START_HOURS_RANGE = 3-22 延迟多少个小时内要执行任务
			- /var/spool/anacron/cron.daily 存储的是时间
			- 执行过程
				1 由 /etc/anacrontab 分析到 cron.daily 這項工作名稱的天數為 1 天；
				2 由 /var/spool/anacron/cron.daily 取出最近一次執行 anacron 的時間戳記；
				3 由上個步驟與目前的時間比較，若差異天數為 1 天以上 (含 1 天)，就準備進行指令；
				4 若準備進行指令，根據 /etc/anacrontab 的設定，將延遲 5 分鐘 + 3 小時 (看 START_HOURS_RANGE 的設定)；
				5 延遲時間過後，開始執行後續指令，亦即『 run-parts /etc/cron.daily 』這串指令；
				6 執行完畢後， anacron 程式結束
			- 放在 /etc/crontab中的工作过期了就过期了，而在/etc/cron.daily中的不会
	- /etc/crontab 分 时 日 月 周 root command
	- crontab -e 分 时 日 月 周 command
	- /etc/cron.hourly/中的文件必须是能直接执行的脚本
# 实例
	
# 练习