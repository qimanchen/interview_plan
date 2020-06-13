# 课程介绍
	1）利用剧本功能简单完成服务一键化部署
	2）主机清单配置
	3）剧本的扩展配置功能
	4）多个剧本如何进行整合
	5）剧本的角色目录
	
# 课程回顾
	1）将所有模块进行和讲解说明
		command --- 在远程主机上执行命令 默认模块
		shell --- 在远程主机上执行命令 万能模块
			使用shell安装不会保持幂等性
			ps: 有时剧本不能反复执行
		script --- 批量执行本地脚本
		copy --- 用于批量分发传输数据
		fetch --- 用于将远程主机数据进行拉取饿到本地管理主机
		file --- 修改数据属性信息/创建数据信息
		yum --- 用于安装和卸载软件包
		service --- 用于管理服务的运行状态
		user --- 用户批量创建用户并设置密码信息
		mount --- 用于批量挂载操作
		cron --- 批量部署定时任务信息
		ping --- 远程管理测试模块
			ansible 172.16.1.41 -m ping
		synchronize -- 利用rsync进行文件/目录的拉取
			mode -- pull 拉取 push 推送
			dest
			src
				PS：pull 和push实现时，dest和src的位置互换
		unarchive: 将本地压缩文件推送到远程主机，并进行解压
			src -- 本地压缩文件
			dest -- 远程主机目录
	2）ansible的剧本功能
		- hosts: all
		  remote_user: root
		  vars:
		    file_name
	      tasks:
		    -name:
		剧本的语法规范
			1. 空格规范：实现缩进功能
			2. 冒号规范：实现key-value格式定义
			3. -规范：实现列表显示
		
# 课程内容
	01. 利用剧本完成一键化部署
		rsync 服务部署
			rsync_service.yaml
			- 准备工作：
				01. 属性软件部署流程
				02. 熟悉ansible软件模块使用
				03. 熟悉ansible剧本编写规范
			ansible:
				ad-hoc 临时实现批量管理功能（模块）
				playbook 永久实现批量管理功能
			/etc/ansible/server_file
				/etc/ansible/server_file/rsync_server
		- 剧本编写常见错误：
			1. 剧本语法格式 空格 冒号 短横线
			2. 剧本模块是否使用正确
			3. 一个name标识下面，只能执行一条命令
			4. 剧本中不要大量使用shell模块
		nfs 服务部署
		sersync 服务部署
		全网备份项目
	02. 如何配置主机清单
		/etc/ansible/hosts
		见hosts文件
		-- 参考官网inventory规范
	03. 剧本的拓展功能
		1. 设置变量
			a 在剧本环境中设置变量
			- hosts: 172.16.1.41
			  vars:
				backupdir: /backup
				passfile: rsync.password
			b 在命令行设置 -- 单次执行 -- 默认针对所有的组测试
				ansible-playbook -e backupdir=/data -e passfile=rsync-password rsync_service-设置变量.yaml
			c 在主机清单中设置变量
				[web:vars]
				backupdir=/backup
				passfile=rsync.password
			三种变量设置方式都配置了，三种方式的优先级：
				最优先：命令变量设置
				次优先：剧本中变量设置
				最后：主机清单变量设置
			如何全局设置变量：roles 剧本整合
		2. 变量注册功能 -- 执行剧本时可以显示输出命令结果信息
			- 测试服务是否启动
			- hosts: oldboy
			  tasks:
			    - name: check server port
				  shell: netstat -tunlp # 端口信息
				  register: get_server_port
				- name: display port info
				  debug: msg={{ get_server_port.stdout_lines }}
				  # stdout_lines 以一行的方式显示
		3. 判断
			如何指定判断条件
				(ansible_hostname == "nfs")
				setup模块中显示的信息中有的变量
				setup模块 -- 显示被管理主机系统的详细信息
					ansible rsync_server -m setup
			获取内置变量方法：
				ansible oldboy -m setup -a "filter=ansible_hostname"
				获取子项的方法
				ansible oldboy -m setup -a "filter=ansible_eth0[ipv4]"
				常见系统变量
		4. 循环：-- 同一个模块合并同类项
			同一个name中，多个相同的模块，那么以后面的那个copy为准
			- name: install
			  yum: name={{ item }} state=present
			  
			  with_items:
			    - wget
				- tree
				- lrzsz
			- name: install new format
			  yum:
			    name: ['rsync', 'tree', 'wget']
				state: present
		5. 在剧本中设置错误忽略
			- name: 02-push conf file & password file			  
			  copy: src=/etc/ansible/server_file/rsync_server/{{ item.src }} dest={{ item.dest }} mode={{ item.mode }}
			  with_items:
				- { src: 'rsyncd.conf', dest: '/etc/', mode: '644' }
				- { src: 'rsyncd.password', dest: '/etc/', mode: '600'}
			  ignore_errors: yes -- 忽略错误
		6. 设置标签功能  -- 仅测试错误的部分
			# 
			- name: 04-create backup file
				file: path=/backup state=directory owner=rsync group=rsync
				tags: t4 # 添加标签
			ansible-playbook --tags=04 *.yaml # 仅执行某个标签
			ansible-playbook --skip-tags=04 *.yaml # 跳过某个标签不执行
				-t --tags
		7. 设置触发功能
			# 如果服务的配置文件被修改了，当设置的是started，这要导致服务无法被
			- name: 02-push conf file
				copy: src=/etc/ansible/server_file/rsync_server/rsyncd.conf dest=/etc/
				notify: restart rsync server  --- 发送通知信息
			  # 发现配置文件改变了，那么需要重启服务
			- name: 06-start rsync server
				service: name=rsyncd state=started enabled=yes
		    tasks:
			handlers: # 处理通知信息
			  - name: restart rsync server # 这个名称与notify名称一致
			    service: name=rsyncd state=restart
			# 接收通知
		剧本错误排查思路：
			1 找到剧本中出现问题的关键点
			2 将剧本中操作装换成模块进行操作
			3 将模块的功能操作装换成linux命令
				本地管理主机上执行测试
				远程主机上执行测试命令
	04. 编写nfs
		1. 创建几个目录
			/etc/ansible/ansible-playbook/nfs_file
				./nfs-server
				./nfs-client
		2. 编写剧本信息
		3. 进行剧本测试
	05. 多个剧本整合
		见 site_server.yaml
		Gathering facts  --- 收集主机的一些信息，这样会导致主句很慢
		- hosts: nfs
			gather_facts: no  # 不收集这些信息
	06. ansible程序roles --- 规范
		剧本编写完问题
			1. 目录结构不够规范
			2. 编写好的任务如何重复调用  -- 比如多个剧本需要安装同样的服务
			3. 服务端配置文件改动，客户端信息自动改变
				rsync 修改服务端口
				验证和配置文件的端口不一致
				- name: 04-check data backup
				   # synchronize模块
				   shell: rsync -avz /tmp/test.txt --port=874 rsync_backup@172.16.1.41::backup --password-file=/etc/rsync.password
			4. 汇总剧本中，没有显示主机角色信息
				汇总剧本无法看到对那些主机进行了操作
			5. 一个剧本内容信息过多，不容易进行阅读，如何进行拆分
		roles编写过程：
			1. 规范目录结构
				/etc/ansible/roles
					mkdir {rsync,nfs} -- 创建相应角色目录
						mkdir {vars,tasks,templates,handlers,files} -- 创建角色目录下面的子目录
							files -- 保存需要分发的文件目录
							handlers -- 保存触发器配置文件信息
							tasks -- 保存要执行的动作信息文件
							templates -- 保存需要分发模板文件，模板文件中可以设置变量信息，调取vars目录中的文件
							vars -- 保存变量信息文件
			2. 在roles目录中创建相关文件
				编写文件流程图
				nfs-server:
					tasks -- main.yaml
					vars
					files
					handlers
					1. 编写tasks目录中的main.yml文件
					2. 编写vars目录中的main.yml文件中
					3. 编写files目录中的文件
						exports文件
					4. 编写handlers目录中的main.yml文件
				同样针对nfs-client
				同样的操作
			3. 在roles目录中编写汇总文件
				site.yml文件
		- templates
			# 每次修改exports中主机
			# rsync vars目录
			Data_dir: /backup
			Port_info: 874
			# templates  -- 模板文件
			rsyncd.conf
				port = {{ Port_info }}
			rsyncd.password
			# file目录需要改变
			# 模板文件中无法调用
			在tasks中使用 templates模板代替copy
		PS：tasks说明
			多个动作需要拆分
			vim copy_info.yml
			vim create_dir.yml
			vim boot_server.yml
			# 整合
			vim main.yml 
			- include_tasks: copy_info.yml
			- include_tasks: create_dir.yml
			or
			- import_tasks 可导入不同的tasks
			
			archive -- 压缩
		ansible-playbook -i 指定主机清单
# 课程总结
	1. rsync服务一键化部署
	2. 主机清单编写方法
	3. 剧本的扩展编写方法
		设置变量
		设置注册信息 debug
		设置判断信息 setup
# 作业
	1. ansible剧本扩展功能进行总结
	2. ansible剧本roles功能
	3. 预习web服务 http协议原理 nginx(安装 配置)
01. 一键化部署全网备份项目
02. 一键化部署实时同步服务
