# 课程回顾
	1） find命令使用方法
		a 根据文件名称类型进行查找
		b 根据文件大小进行查找 -size
		c 根据目录层级查找 -maxdepth，-mindepth
		d 根据文件权限进行查找
			find /oldboy -maxdepth 1 -type f -perm 644
		- find 命令删除
			find /oldboy -type f -name '*.txt' -delete
			find /oldboy -type f -name '*.txt' -exec rm -r {} \;
				ps：exec是一行一行处理，针对压缩文件tar不适用
				-exec rm -rf {} \; => rm -f /oldboy/oldboy.txt;...
			find /oldboy -type f -name '*.txt' | xargs rm -f
				xargs 将多行信息换成一行
			rm -rf `find /oldboy -type f -name '*.txt'`
			
	2） tar命令压缩数据
		如何压缩数据
			tar zcvf /tmp/test.tar.gz /etc/ /odlboy/ ...
		如何解压
			tar zxvf /tmp/test.tar.gz -C /oldboy 指定解压目录
		如何查看压缩文件信息
			tar tf /tmp/test.tar.gz
		--exclude
		--exclude-from 后面跟要排除的文件
	3） 文件属性信息 -- 权限信息
	4）	文件属性信息 -- 用户信息
	5） 文件属性信息 -- 时间信息 (atime mtime ctime)
# 课程介绍
	01. 文件属性信息 - inode
		inode：文件属性，大小，权限，时间，拥有者，文件指针信息
			- 文件权限（r/w/e)
			- 文件拥有者与群组
			- 文件容量
			- 文件建立或状态改变的时间 ctime
			- 最近一次读取的时间 atime
			- 最近修改的时间 mtime
			- 定义文件特性的flags
			- 该文件真正内容的指向
		inode -- 索引节点
			概述：
				相当于书的目录
				用于存储文件属性信息
				创建文件系统后
			- 磁盘操作处理过程：
				磁盘
				raid
				分区
				格式化
				创建文件系统	inode和block
				挂载
			特点说明：
				inode用于存放文件属性
				inode用于存放块的指针位置
				创建一个文件至少占用一个indoe和一个block
				在同一分区中，两个文件的inode号码相同，两个文件互为硬链接文件
		block -- 数据块 -- 文件具体内容
			概述：
				目录指向的内容
				用于存储文件具体内容
			特点说明：
				block用于存放的是数据信息
				block默认大小为4k，可以调整
				比较大的文件，会占用多个block
				比较小的文件，剩余空间无法使用，浪费磁盘空间
				创建一个文件至少占用一个indoe和一个block（非空文件）
				磁盘读取数据按照block为单位进行读取
				读取一个block会消耗一次磁盘I/O（input/output 磁盘读写），block越多，消耗I/O就多
					input
					output
			问题：block默认大小可以调整 是大点好 小点好
				- 设置大点，文件大的时候 视频 图片 --- block增大，节省I/O消耗
				- 设置小点，10k，小文件1k ，2k -- 提高磁盘利用率，互联网公司
			企业面试：你都做过哪些系统优化操作
			
		- 查看inode
			df -i
		- 查看block
			df
		- 补充：
			01. 文件属性信息存储到inode中
			02. 文件的名称信息存储在上一级目录的block中
	02. 文件属性信息 - 硬链接数
		硬链接：在一个分区中，inode相同的文件，互为硬链接文件
			- 文件数据的多个门
			- ln 链接源文件 硬链接的文件信息
			- 删除文件了，实质数据仍然存在
			- 只能防止数据误删除
			- cp 才能防止误修改
		- 目录不能创建硬链接
			由于硬链接不能跨分区操作
			/proc/ 和 /sys同inode
		- 目录的硬链接数
			ll /etc/ | grep -c "^d"
			ll /etc/ | grep "^d" | wc -l 统计行
		软连接：创建一个指向文件名的指针
			- 文件的快捷方式
			- ln -s 链接源文件 软链接的文件信息
			- 采用绝对路径创建软连接
		- 找到所有硬链接文件
			find / -type f -inum inode 
		- 软硬链接的区别
			01. 链接后的文件大小不一致
			02. 链接后的文件类型和权限不一致
			03. 链接后的文件和源文件 inode信息有出入
				硬链接inode一致
				软链接inode不一致
			04. 源文件被删除后
				硬链接文件依然有效
				软链接文件失效
			05. 软硬链接创建过程不一致
			06. 硬链接不能跨文件系统，不能link目录
	03. 和时间相关的命令
		时间相关的命令 date
		01. 查看时间信息
			date
		02. 调整时间信息格式
			date +%F-%T
				2020-02-24-11:10:35
			date "+%F %T"
				2020-02-24 11:11:05
			date "+%y-%m-%d %H:%M:%S"
				20-02-24 11:12:26
			cp oldboy.log oldboy.log-$(date "+%F-%T")
			date "+%Y%m%d" -d "+1day"
		03. 如何实际修改系统时间
			date -s "2020-04-17"
			date -s "2020/04/17 14:00"
		04. 修改几天后的时间
			- 显示将来的时间
			date +%F -d "+1day" 后一天
			date +%F -d "2day"
			- 显示历史信息
			date +%F -d "-1day" 前一天
			date +%F -d "1 day ago" 前一天
			- 系统自动的备份数据 00:00
				cp /oldboy/oldboy.log /log/oldboy.log.$(date +%F)
				调整 备份前一天的数据
					cp /oldboy/oldboy.log /log/oldboy.log.$(date +%F -d "-1day")
		05. 系统时间同步
			yum install -y ntpdate
			[root@qiman ~]# ntpdate ntp1.aliyun.com
				24 Feb 17:53:20 ntpdate[17256]: step time server 120.25.115.20 offset 23065.018689 se
# 总结
	
# 练习
	- inode中主要存储哪些信息
		stat指令可以查看文件的详细时间信息
		通过 find -inum 可以查找到统一inode的所有文件
		- 文件权限（r/w/e)
		- 文件拥有者与群组
		- 文件容量
		- 文件建立或状态改变的时间
		- 最近一次读取的时间
		- 最近修改的时间
		- 定义文件特性的flags
		- 该文件真正内容的指向
		- 每个inode大小均固定为128bytes -- ext2文件系统
	
	- 总结英文月份信息，周
# 拓展练习
	- 如何修改磁盘中block大小，如何进行查看默认的block大小
		- ext2文件系统
			- 原则上，block的大小与数量在格式化完成后不能够在改变了（除非重新格式化）
			- 如何查看block的大小
				blkid 列出目前系统中被格式化的装置
				dumpe2fs 装置名 --- 查看详细信息 -- 仅针对ext2文件系统
				tune2fs -l /dev/sda1 查看系统块大小
				mke2fs -b 4096 -m 1 /dev/sda1
		- xfs系统
			block容量可以由512bytes~64K可调
			xfs_info 挂载点|装置名
				isize -- inode总容量
				bsize -- block大小
				data     =                       bsize=4096   blocks=9699328, imaxpct=25 总容量
				log      =internal               bsize=4096   blocks=4736, version=2 使用容量
			- 修改block大小
				1. umount /dev/sda1
				2. mkfs -t xfs -b size=2048 -f /dev/sda1
				- mkfs.xfs是mkfs -t xfs的简写
	- 总结数据存储与读取原理
		数据读取：
			- 索引式文件系统
			1. 确定文件的inode信息，权限
			2. 读取inode中存取的block编号信息
		- 文件属性 inode
		- 文件实际内容 block
		- 目录读取
			目录中的文件名存储到目录的block中
		- 普通用户读取/etc/passwd
			1. / inode 权限确认(r,x)
			2. / block 找到 etc/目录的inode
		- 文件存储
			1. 先确定使用者对于新增文件的目录是否具有w和x权限，若有才允许新增
			2. 根据inode bitmap找到没有使用的inode，并将新文件的权限/属性写入
			3. 根据block bitmap找到没有使用中的block号码，并将实际的内容写入到block中，并更新inode的block指针
			4. 将写入的inode与block内容同步更新inode bitmap和block bitmap，并更新superblock的内容
	- 磁盘满无法存储数据的原因，如何解决
		- du 
			-a 列出所有的文件与目录的容量，默认只统计文件
			-h 人类可读容量格式
			-s 仅列出总量，而不列出每个个别目录占用的容量
			-S 不包括子目录下的文件统计的统计
			-k 以kb
			-m 以mkb
		du 查看磁盘中文件或目录所占磁盘空间大小
		- 无法读取的原因
			01. 空间还有，inode使用完了
			02. 空间没了 df -h 查看，du 确认每个文件的大小
		- 解决磁盘空间占用100%的问题
			1. 查看当前磁盘剩余空间
				df -h 超过90%需要清理了
			2. 查找大文件
				find . -type f -size +1024M/100M/10M
			3. 查找大目录
				sudo du -s * | sort -nr | head  占用空间前10的文件
				sudo du -hm --max-depth=2 | sort -nr | head -12 占用空间排序
			4. 删除文件或目录
				rm -rf 目录名称
		- 解决磁盘inode占用100%问题
			1. 查看inode占用情况
				inode table 
				df -i 查看inode占用情况
			2. 查出inode占用大的目录
				for i in /var/*;do echo $i; find $i | wc -l; done 当前各大文件夹占用inode情况
				# 排序
				sudo find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
			3. 删除占用大的文件/目录
		- inode用完的可能原因， 日志文件过多
			可以通过 zabbix进行检测
	- linux系统中读取数据的原理（数据无法读取-权限阻止）
		先读取inode中的权限（文件 r, 目录 r x)
		有相应的权限时，取得相应的block编号，然后获取相应的内容
	- 如何将文件彻底删除
		- shred - 覆盖文件以隐藏内容
			1. $ shred -zvu -n 5 passwords.list
				-z	最后一次覆盖添加0，以隐藏覆盖操作
				-v	显示操作进度
				-u	覆盖后截断并删除文件
				-n	指定覆盖文件内容几次， 默认为3次
		- wipe - 安全查出linux下的文件
			1. sudo yum install wipe(redhat) sudo apt-get install wipe (debian)
			2. wipe -rfi private/*
				-r	wipe递归查询子目录
				-f	强制删除，禁用确认查询
				-i	显示删除过程进度
		- 面向Linux的secure-deletetion工具包
			1. sudo yum install secure-delete
			2. srm -vz private/*
				-v	显示详细信息
				-z	用0而不是用随机数据擦除上一次写入的内容
			- sfill - 安全免费的磁盘/索引节点空间擦除工具
				1. sudo sfill -v /home/..
			- sswap
			- sdmem
			reference: http://www.linuxidc.com/Linux/2017-01/139599.htm
				