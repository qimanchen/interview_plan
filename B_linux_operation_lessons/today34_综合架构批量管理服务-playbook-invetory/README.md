# 课程介绍
	1) ansible批量管理服务模块说明
	2）ansible批量管理服务主机清单
	3）ansible批量管理服务playbook
	4）ansible批量管理服务实战应用（rsync nfs）
# 课程回顾
	1. ansible服务概念介绍
		a ansible可以批量管理多台主机
		b 提高运维工作效率
		c 降低运维工作难度
	2. ansible服务特点说明
		管理端不需要服务程序 no server
		管理端不需要配置文件 /etc/ansible/ansible.cfg
		受控端不要安装软件程序 libselinux-python
			被管理端selinux服务没有关闭 -- 影响ansible软件的管理
			libselinux-python让selinux开启的状态也可以使用ansible
		受控端不需要启动服务程序 no agent
		服务程序管理操作模块众多 module
		利用剧本编写来实现自动化 playbook
	3. ansible服务的部署安装
		a 安装服务软件
		b 编写主机测试
		c 进行管理测试
	补充：远程主机无法管理问题分析
		1. 管理端没有分发好主机的公钥
		2. 被管理端远程服务出现问题
		3. 被管理端进程出现僵死情况
			/usr/sbin/sshd -D --- 负责建立远程连接
			sshd: root@pts/0 --- 用于维护远程连接
			sshd: root@notty --- 用户维护远程连接（ansible--被管理端）--- j
	4. ansible服务模块应用
		command
		shell
		script -- 脚本
		copy -- 批量分发文件 管理端 --- 多个被管理
		fetch -- 从远端节点拉取文件到批量管理主机
			dest
			src 
			ansible 172.16.1.31 -m fetch -a "src=/tmp/oldboy.txt dest=/tmp/"
			最终拉取的文件会被放到/tmp/172.16.1.31/tmp/oldboy.txt 目录中
		file
		补充说明：ansible学习帮助手册
			ansible-doc -l  --- 列出模块简介
			ansible-doc -s fetch --- 指定一个模块的详细说明
			ansible-doc fetch --- 给出在playbook中的使用格式，应用方法

# 课程内容
	01. ansible模块说明
		yum模块
			name -- 指定安装软件名称
			state -- 是否安装软件
				absent -- 卸载软件
				removed
				
				latest
				installed -- 安装软件
				present
				
			ansible 172.16.1.31 -m yum -a "name=iotop state=installed"
		service模块 -- 管理服务的运行状态 停止 开启 重启
			name --- 指定管理服务的服务名称 -- 完整的名称
			state --- 指定服务的状态
				started 启动
				restarted 重启
				stopped 停止
			enabled --- 指定服务是否开机自启
			ansible 172.16.1.31 -m service -a "name=nfs state=started enabled=yes"
		cron模块 --- 批量设置多个主机的定时任务信息
			minute -- 设置分钟信息 0-59, * */2 etc
			hour -- 小时
			day -- 设置天
			month -- 月
			weekday -- 
			
			job --- 定义定时任务需要干的事
			
			- 基本用法
			ansible 172.16.1.31 -m cron -a "minute=0 hour=2 job='/usr/sbin/ntpdate ntp1.aliyun.com >/dev/null 2>&1"
			- 扩展用法
				1. 给定时任务设置描述信息
				ansible 172.16.1.31 -m cron -a "name='test ansible cron' minute=0 hour=2 job='/usr/sbin/ntpdate ntp1.aliyun.com >/dev/null 2>&1"
					有相同名称的定时任务不会在重新创建
				2. 如何删除指定定时任务
					persent
					ansible 172.16.1.31 -m cron -a "name='test ansible cron' state=absent"
					ps: ansible可以删除的定时任务，只能是ansible设置好的定时任务
				3. 如何批量注释定时任务
					ansible 172.16.1.31 -m cron -a "name='test ansible cron' job='/usr/sbin/ntpdate ntp1.aliyun.com >/dev/null 2>&1 disabled=yes"
					必须指定job信息
					disabled=no
					
		mount模块 -- 批量进行挂载
			src --- 需要挂载的存储设备或文件信息
			path --- 挂载点
			fstype --- 挂载文件系统类型
			opts -- 指定挂载参数 如 rw noauto 等
			state --- 
				persent/mounted --- 挂载
					persent -- 不会实现立即挂载 --修改/etc/fstab
					mounted -- 实现立即挂载，并且修改fstab文件，实际开机自动挂载
				absent/unmounted --- 卸载
					absent -- 会实现立即卸载，并会删除fstab文件信息
					unmonted -- 只卸载，但不会删除/etc/fstab 中的自动挂载信息
			ansible 172.16.1.31 -m mount -a "src=172.16.1.31:/data path=/mnt state=persent"
		user模块 -- 实现批量创建用户
			- 基本用法
				ansible 172.16.1.31 -m user -a "name=oldboy01"
			- 扩展用法	
				1. 指定uid
					ansible 172.16.1.31 -m user -a "name=oldboy01 uid=666"
				2. 指定用户组
					ansible 172.16.1.31 -m user -a "name=oldboy03 group=oldboy02"
						groups=oldboy02  -- 添加额外的组
						group --- 主要组
				3. 批量创建虚拟用户
					ansible 172.16.1.31 -m user -a "name=oldboy03 create_home=no shell=/sbin/nologin"
				4. 给指定用户创建密码
					ansible 172.16.1.31 -m user -a "name=oldboy03 password="
					ps：利用ansible程序设置密码，密码钥匙密文信息
					生成密文信息密码信息
						ansible all -i localhost -m debug -a "msg={{ ‘密码信息’ | password_hash('sha512', '加密校验信息') }}"
						ansible all -i localhost -m debug -a "msg={{ ‘123456’ | password_hash('sha512', 'oldboy') }}"
						- 校验信息 --- 
					方法二
						mkpasswd --method-sha-512
					方法三
						yum install -y python-pip
						pip install passlib
						python -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))
						--- 交互方式生成密文信息
					ansible 172.16.1.31 -m user -a 'name=oldboy03 password=生成的密文信息'
					为使得密文信息生效，参数部分必须使用单引导
	03. 编写剧本的编写方法
		剧本作用 -- 可以一键化完成任务
			自动化部署rsync服务
				1. ansible 172.16.1.41 -m yum -a "name=rsync state=installed"
				2. 编写文件
					ansible 172.16.1.41 -m copy -a "src=/xxx/rsyncd.conf dest=/etc/"
				3. 创建用户
					ansible 172.16.1.41 -m user -a "name=rsync create_home=no shell=/sbin/nologin"
				4. 创建目录
					ansible 172.16.1.41 -m file -a "dest=/backup state=directory owner=rsync group=rsync"
				5. 创建密码文件
					ansible 172.16.1.41 -m copy -a "content='rsync_backup:oldboy123' dest=/etc/rsync.password mode=600"
				6. 启动服务
					ansible 172.16.1.41 -m service -a "name=rsyncd state=started enabled=yes"
				客户端
					ansible 客户端操作 -m copy -a "content='rsync_backup:oldboy123' dest=/etc/rsync.password mode=600"
		剧本组成
			hosts
			tasks
		剧本的编写规范：
			pyyaml格式 -- 三点要求
				1. 合理的信息缩进 两个空格表示一个缩进关系
					ps: 在ansible中一定不能用tab进行缩进
				2. 冒号的使用
					hosts: 172.16.1.41
					yum: name=xx
					ps: 使用冒号时，后面要有空格信息
						以冒号结尾，冒号信息出现在注释说明中，后面不需要加上空格
				3. 短横线应用 -(列表功能)
			ps:使用短横线构成列表信息，后面需要有空格
			YAML 格式说明
				1. 文件均以 --- 作为开始，以 ... 结束。
				2. 列表中同级别的项使用相同缩进以及短横线加空格（-）开始。

				3. 字典（dictionary）用 key: value 的简单形式表示，其中冒号后面必须有个空格。value 部分可以用几种形式（yes/no/true/false）来指定布尔值。

				4. 换行符：value 部分还可以使用 | 或 >，使用 | 可以将内容进行分行处理，而使用 > 将忽略换行符，任何情况下缩进都会被忽略。

				5. 语句过长可以使用 "" 括起来，例如：foo: "somebody said I should put a colon here: so I did"。
		开始编写剧本
			
			mkdir /etc/ansible/ansible-playbook
			vim rsync_server.yaml -- 剧本文件扩展名尽量写为yaml，文件编写时会有颜色说明
			如何执行剧本
				1. 检查剧本的语法格式
					ansible-playbook --syntax-check rsync_server.yaml
				2. 模拟执行剧本
					ansible-playbook -C rsync_server.yaml -- 模拟执行剧本
				3. 直接执行剧本
					ansible-playbook rsync_server.yaml
# 课程总结
	1. 常用模块的补充说明
		fetch yum service user mount cron
	2. 剧本的编写规范
		剧本组成 
		- hosts: 
		  tasks: 
		    - name: 
			  yum: 
	3. 剧本的执行方式
		检查语法
		模拟执行
		真正执行
作业：
	1. 如何利用剧本部署rsync服务
	2. 如何利用剧本部署nfs服务