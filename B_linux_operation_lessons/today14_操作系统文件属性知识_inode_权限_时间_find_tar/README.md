# 自己课程知识回顾
	- tail -f 和tail -F区别
	- tr命令替换信息原理
	- 第四阶段，目录结构知识回顾
		- 如何卸载软件
	- 第五阶段，系统优化回顾
		- 创建多用户
		- 设置密码的方式
	- 文件操作系统，文件系统知识
		inode 文件类型 权限 硬链接数 所属用户 所属组 大小 时间 文件/目录名
	- 拓展命令
		file which whereis locate find
# 视频中课程回顾
	1. 基础课程的前半部分进行了梳理
	2. vim使用原理和常见错误
	3. 文件属性知识
		文件的索引节点 inode
		文件的数据类型
		文件的权限位
		文件的硬链接数
		文件所属用户
		文件所属组
		文件大小
		文件的修改时间
	4. 文件的数据类型 
		- 普通文件 纯文本，二进制文件，压缩文件
		d 目录
		l 软链接
		c/b 设备文件,b 块设备文件，c字符信息设备文件
		s sockets
	5. 和文件相关的命令
		locate(updatedb)
		find path [options]
			find /etc -type f -iname "oldboy" 忽略大小写
		which
		whereis
	
# 课程知识介绍
	1. 文件属性部分内容介绍完
		01. find命令查找信息补充
			查找文件信息
				精确查找
					find path -type f -name "filename"
				模糊查找
					find path -type f -name "*name"
				忽略大小写
					find path -type f -iname "name"
				根据文件大小
					find path -type f -size +1M 大于
					c 字节
					k 
					M 兆
			find 命令查找文件默认是递归的查找
			- find /oldboy -maxdepth 1 type f -name "Oldboy" 根据目录指定层级进行查找数据
				find只在一层
			根据数据的权限进行查找数据
			根据文件的权限进行查找
		02. tree 显示目录的层级信息
			tree /oldboy 显示指定目录层级信息
			tree -L 1 / 指定目录层级
			tree -d / 只显示目录信息
		03. 系统中如何对文件进行压缩处理
			压缩的命令
				tar
					语法 tar zcvf /oldboy/oldboy.tar.gz 要压缩的数据文件
						z 压缩的方式 zip
							j bzip
							x xz
						c 创建压缩包文件
						v 显示压缩的过程详细信息
						f 指定压缩包文件路径信息
					检查是否压缩成功
					- 如何解压数据包
						tar zxvf /oldboy/oldboy.tar.gz 解压
					windows比对文件软件 -- Beyond Compare
					- linux比对文件不同
						diff file1 file2
						vimdiff file1 file2 直接看到两个窗口
					- 确认解压后的文件和源文件是否一致
						1. 文件大小和时间信息
						2. vimdiff or diff 比对文件
					- tar tf /oldboy/oldboy.tar.gz 在不解压情况下，查看压缩包内的数据
					- 压缩过程信息说明
						默认将压缩时，将绝对路径的根删除
						使用相对路径，可以显示一些提示信息
						.. 上一个文件
						. 当前目录
					- 压缩目录中，不压缩某个文件，排除指定数据文件
						exclude
						include
						--exclude 排除单个文件
						-X --exclude-from 排除多个文件
						tar zcvf /tmp/oldboy.tar.gz  ./oldboy --exclude=排除文件 都要使用绝对路径
						总结：排除指定数据信息需要定义好路径信息
							路径信息全部采用绝对路径
					- 压缩文件时，排除多个数据文件
						批量编辑文件 vim  块处理，替换
						1. 编写好排除文件
						2. tar zcvf /tmp/oldboy.tar.gz  /oldboy --exclude-from=存储排除文件的配置文件
		04. 文件属性信息详细说明 -- 文件权限
			1）文件数据权限是什么
				r read		- 4
				w write		- 2
				x execute	- 1
				- 没有权限
			2) 权限赋予到指定到人
				属主信息 文件所有者 权限
				属组信息 文件所有者 权限
				其他用户
		05. 文件属性信息详细说明 -- 用户信息（属主 属组）
			1） 系统中用户信息有什么作用
				a 利用用户登录系统
				b 利用用户管理数据
				c 利用用户管理进程
			2） 如何识别不同的用户
				利用用户的数值编号进行识别：uid
				id username
			3) 用户组的概念
				oldboy -sa(system admin) /sa -- rwx 一个组拥有的权限
				boy - dev(development)	/dev -- rwx
				alex - dba(database admin) /dba -- rwx
				- 用户和用户组的关系
					用户 -- 用户组 1v1
					多个用户 -- 用户组 多v1
					一个用户 -- 多个组 1v多
				系统识别用户组，根据编号识别 gid
					id root
					uid=0(root) gid=0(root) groups=0(root)
					01			02			03
					01. 显示用户名和uid对应关系
					02. 显示属于的用户组，以及组名和gid对应关系
					03. 用户可能所属组
			4）用户进行分类
				a 超级管理员用户	root
					uid信息进行区分 0
					权限：至高无上
				b 虚拟用户			xxx nobody
					uid信息进行区分 1-999 centos7
					权限：管理进程 不能登录系统 没有家目录
				c 普通用户			oldboy
					uid信息进行区分 1000+ centos7
					权限：管理指定数据 指定进程 登录系统/有家目录
				如何保护好root用户
					01. 修改远程连接端口 - 52113 修改/etc/ssh/sshd_config
					02. 禁止root用户远程登录 - 修改/etc/ssh/sshd_config
						登录普通用户，切换为root用户
						- root 密码破解
							1. 系统中有什么普通用户
							2. 普通用户密码
							3. su - root root用户密码
				- 满足什么条件可以以root用户登录
					01. 服务器地址信息 ip
					02. 服务器端口信息 22 改端口
					03. 登录用户信息 root
					04. 登录用户的密码 暴力破解
		06. 文件属性信息详细说明 --- inode
			inode: 索引节点
				文件或数据在磁盘中保存位置
			block: 索引节点指定的位置
				文件或数据的具体内容
			读取数据的原理：
				01. 找到指定数据
				02. 读取数据内容，先获取文件数据inode信息
				03. 根据inode信息在磁盘上找到对应的block
				04. 根据block信息获取文件真正内容
		07. 文件属性信息详细说明 -- 时间信息（mtime）
			文件数据时间类型：
				a 访问时间	Access time -- atime
					cat test.txt
				b 修改时间	Modify time -- mtime
					echo “hello" >> test.txt
				c 改变时间	change time -- ctime -- 数据属性信息发生改变
					chmod +x
					size
				stat /etc/hosts 查看文件时间
				date 显示当前时间
			
	2. 基础命令
# 课程总结
	1) find命令使用方法
	2）tar命令详解
	3）文件属性权限信息
	4）文件属性中用户信息 用户分类 useradd userdel usermod
	5) 文件属性中的inode
	6）文件属性中时间信息（stat）
	
# 练习
	- 如何将一个目录中以.txt结尾的文件，统一压缩处理
		 tar zcvf /root/oldboy.tar.gz `find /root/oldboy -type f -name "*.txt"`
		 find /root/oldboy -type f -name "*.txt" -exec tar zcvf /root/oldboy.tar.gz {} \;
			- 这个不能实现，由于exec是一行一行执行的
		 find /root/oldboy -type f -name "*.txt" | xargs tar zcvf /oldboy/oldboy.tar.gz
		 -exec是一行一行处理
	rwx 对应的数值 7
	rw--w---x 6 2 1
	r---wx-w-
	- centos6如何用uid区分不用用户
	- 如何找出oldboy目录中.txt结尾的文件，将找出的文件统一删除
		find ./oldboy/ -type f -name "*.txt" -exec rm -f {} \;
		rm -f `find /root/oldboy/ -type f -name "*.txt"`
	- 如何找出oldboy目录中.txt结尾的文件，将找出的文件统一移动到/temp目录中
		mv `find /root/oldboy -type f -name "*.txt"` /tmp
		find /root/oldboy -type f -name "*.jpg" -exec mv {} /tmp \;
	- 总结linux中常用的压缩和解压命令 tar zip rar
# 拓展练习