# 课程介绍
	1. ansible批量管理服务概念
	2. ansible批量管理服务特点
	3. ansible批量管理服务部署
	4. ansible批量管理服务应用 -- 模块应用 剧本应用
		ansible模块命令语法
		ansible常用模块
		
# 课程回顾
	1. 远程管理服务
		ssh -- 数据加密 22
		telnet 数据明文 23
	2. ssh远程服务工作原理
		私钥 公钥
		1. 对数据进行加密
		2. 对用户访问进行认证
	3. ssh远程连接方式
		1. 基于口令的方式
		2. 基于密钥对的方式
			基于秘钥量连接的工作原理
	4. 基于密钥连接的部署方式
		ssh-keygen
		ssh-copy-id
		sshpass
		# 批量分发
	5. ssh远程服务防范入侵的案例
	
	6. ssh服务的配置文件编写
	7. ssh服务相关的命令总结
			
# 课程总结
	01. ansible批量管理服务介绍
		# 概述
			基于python开发的
			基于ssh远程管理
		# 意义
			提高工作的效率
			提高工作准确度
			减少维护成本
			减少重复性工作
		# 功能
			可以实现批量系统操作配置
			批量软件服务部署
			批量文件数据分发
			批量系统信息收集
		# 特点
			管理端不需要启动服务程序（no server)
			管理端不需要
	02. ansible批量管理服务部署
		1. 安装部署软件
			yum install -y ansible  --- 需要依赖epel的yum源
		2. 需要编写主机清单文件
			/etc/ansible
			-rw-r--r-- 1 root root 19985 Apr  6 13:10 ansible.cfg -- ansible服务配置文件
			-rw-r--r-- 1 root root  1016 Apr  6 13:10 hosts -- 主机清单文件
				vim /etc/ansible/hosts
				172.16.1.31
				172.15.1.41
			drwxr-xr-x 2 root root     6 Apr  6 13:10 roles -- 角色目录
		3. 测试是否可以管理多个主机
			脚本 hostname
			ansible all -a "hostname"
			[root@m01 ~]# ansible all -a "hostname"
				172.16.1.41 | CHANGED | rc=0 >>
				backup
				172.16.1.31 | CHANGED | rc=0 >>
				nfs01
	03. ansible服务架构信息
		1. 主机清单配置
		2. 软件模块信息
		3. 基于秘钥连接主机
			selinux 连接主机报错 -- 关闭selinux服务
		4. 软件剧本功能 -- ansible
	04. ansible软件模块应用
		关注官方网站 -- https://
			module index
			模块的应用：
				语法格式
				ansible 主机名称/主机组名称/ip/all -m 模块名称 -a "待执行的动作"
					-m 指定应用的模块信息
					-a 指定动作信息
			command 模块 -- 在远程主机上执行一个命令 -- 默认模块
			
			简单应用：
				ansible 172.16.1.31 -m command -a "hostname"
			扩展应用：
				1. chdir 执行命令之前，进行目录的切换
					ansible 172.16.1.31 -m command -a "chdir=/tmp touch oldboy.txt"
				2. creates 如果文件存在了，不执行命令操作
					ansible 172.16.1.31 -m command -a "creates=/tmp/hosts touch oldboy.txt"
				3. removes 如果文件存在了，这个步骤执行
					ansible 172.16.1.31 -m command -a "removes=/tmp/hosts touch oldboy.txt"
				4. free_form 必须要有的模块
					使用command模块时，-a参数后面接一个合法的linux命令信息
			注意事项：
				有些符号信息无法识别：<,> | ; & -- 这些符号使用不了，则使用shell模块
				ansible 172.16.1.31 -m shell -a "grep 6|5 /etc/hosts"
			ansible 模块的总结
		命令类型模块
		shell模块 在节点上执行操作 -- 万能模块
			
			简单应用：
				ansible 172.16.1.31 -m shell -a "hostname"
				ansible 172.16.1.31 -m shell -a "echo 123 > /tmp/hosts"
			扩展应用：
				1. chdir 执行命令之前，进行目录的切换
					ansible 172.16.1.31 -m shell -a "chdir=/tmp touch oldboy.txt"
				2. creates 如果文件存在了，不执行命令操作
					ansible 172.16.1.31 -m shell -a "creates=/tmp/hosts touch oldboy.txt"
				3. removes 如果文件存在了，这个步骤执行
					ansible 172.16.1.31 -m shell -a "removes=/tmp/hosts touch oldboy.txt"
				4. free_form 必须要有的模块
					使用command模块时，-a参数后面接一个合法的linux命令信息
			实践应用
				1. 执行脚本
					a. 编写脚本
						#!/bin/bash
						yum instal -y htop
					b. 将脚本发送到目标主机
						scp -rp yum.sh 172.16.1.31:/server/scripts
					c. 将脚本权限进行修改（添加执行权限）
					d. 运行ansible命令执行脚本
						ansible 172.16.1.31 -m shell -a "sh /server/scripts/yum.sh"
		script 模块 -- 运行一个脚本，将运行结果发送到
			实际应用
				1. 编写脚本
				2. 运行ansible命令执行脚本
					ansible 172.16.1.31 -m script -a "/server/scripts/yum.sh”
			script参数功能和commnd模块参数类似
		文件类型模块
			copy  -- 将数据信息进行批量分发
			基本用法：
				ansible 172.16.1.31 -m copy -a "src=/etc/hosts dest=/etc/"
				[root@m01 ~]# ansible 172.16.1.31 -m copy -a "src=/tmp/test_ansible.txt dest=/tmp/"
				172.16.1.31 | CHANGED => {  --- 对那台主机进行操作
					"ansible_facts": {
						"discovered_interpreter_python": "/usr/bin/python"
					}, 
					"changed": true, 	--- 是否对主机信息进行改变
					"checksum": "d4d55684a3d4d6a3c31c36f788f01f30d0d22d02",  -- 生成一个文件校验码==MD5数值
					"dest": "/tmp/test_ansible.txt", -- 显示目录路径信息
					"gid": 0,  -- 显示复制后文件gid信息
					"group": "root", -- 显示复制后文件属组信息
					"md5sum": "1ae9367e28d7d3173e93a92d09e76708", 	 -- 生成一个文件校验码==MD5数值
					"mode": "0644", -- 显示复制后权限信息
					"owner": "root", -- 显示复制后属主信息
					"size": 25,  -- 显示文件的大小信息
					"src": "/root/.ansible/tmp/ansible-tmp-1588153059.82-249990741420091/source", 
					"state": "file",  -- 显示文件的类型信息
					"uid": 0 -- 显示复制后文件uid信息
				}
			扩展用法：
				1. 在文件传输时，改变文件的属组和属主
					ansible 172.16.1.31 -m copy -a "src=/etc/hosts dest=/etc/ ower=odlboy group=oldboy"
				2. 修改权限
					ansible 172.16.1.31 -m copy -a "src=/etc/hosts dest=/etc/ ower=odlboy mode=1777"
				3. 复制操作前，对源文件进行备份（目标主机）
					ansible 172.16.1.31 -m copy -a "src=/etc/hosts dest=/etc/ ower=odlboy backup=yes"
				4. 传输一个文件并直接编辑文件的信息
					ansible 172.16.1.31 -m copy -a "content='centos' dest=/etc/hosts owner=odlboy"
				复制目录
					ansible 172.16.1.31 -m copy -a "src=/test_dir/ dest=/data"
					src后面目录没有斜线，将目录本身以及目录下面内容都进行远程传输复制
					src后面有斜线， 将目录下面内容都进行远程传输复制
			自行研究：remote_src local_follow directory_mode
				remote_src:
				no -- 从本地查找src的文件
				yes -- 从远程主机上查找 -- 远程主机上的文件移动
				ansible 172.16.1.31 -m copy -a "src=/tmp/test.txt dest=/test_ansible/test.txt remote_src=yes"
		补充说明：ansible软件输出颜色说明
			01. 绿色信息：查看主机信息/对主机未做改动
			02. 黄色信息：对主机数据信息做了修改
			03. 红色信息：命令执行出错
			04. 紫色信息：建议
			05. 蓝色信息：显示ansible命令执行过程
			
			file -- 设置文件属性信息
				基本用法：
					ansible 172.16.1.31 -m file -a "dest=/etc/hosts owner=oldboy group=oldboy mode=666"
				扩展用法：
					1. 可以利用模块创建数据信息 （文件 目录 链接文件）
						state 参数
							=absent --- 删除数据信息
								ansible 172.16.1.31 -m file -a "dest=/test_dict/new_dict/new_file state=absent"
								删除文件new_file
								ansible 172.16.1.31 -m file -a "dest=/test_dict/new_dict/ state=absent"
								删除目录new_dict
							=directory --- 创建一个木信息
								ansible 172.16.1.31 -m file -a "dest=/test_dict/new_dict state=directory"
								同样可以创建多级目录
							=file --- 检测创建的数据信息是否存在， 绿色存在 红色不存在
								
							=hard --- 创建一个硬链接
								ansible 172.16.1.31 -m file -a "src=/test_dict/new_dict/new_file dest=/test_dict/new_dict/new_file_hard_link state=hard"
							=link --- 创建一个软连接
								
							=touch --- 创建一个文件信息
								ansible 172.16.1.31 -m file -a "dest=/test_dict/new_dict/new_file state=touch"
					2. 可以利用模块删除信息
						
				自行研究参数 recurse
					实现 chmod -R 功能 recurse
						"dest=/root/test_ansible/ mode=777 recurse=yes"

# 习题