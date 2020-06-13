# 课程回顾
	1）磁盘的层次结构
		1. 物理
		2. 阵列 lvm 将多块磁盘整合成一块，lvm弹性磁盘
		3. 磁盘分区方法
		4. 磁盘格式化操作：创建文件系统
		5. 磁盘挂载使用
# 课程介绍
	1) 磁盘分区方法 （备份服务器 存储服务器 数据库服务器）
	2）实现挂载使用 （实现开机自动挂载 /etc/fstab /etc/rc.local)
	3）swap分区如何调整大小（案例 java 比较耗费内存 临时增加swap空间）
	4）企业常见问题：磁盘空间满了如何处理
	01. 磁盘分区方法
		- 情况一， 磁盘分区实践 -- 磁盘小于2T
			a 准备磁盘环境
				添加一块新的硬盘
			b 在系统中检查是否有新的磁盘加入
				lsblk 查看磁盘情况
			c 对磁盘进行分区处理 （fdisk -- 进行分区处理 查看分区信息）
				fdisk -l  --- 查看分区信息
				fdisk /dev/sdb
				   d   delete a partition
					删除分区
				   g   create a new empty GPT partition table
					创建一个新的空的gpt分区表（可以对于大于2T磁盘进行分区）
				   l   list known partition types
					列出可以分区的类型
				   m   print this menu
					输出帮助信息
				   n   add a new partition
					新建一个分区
				   p   print the partition table
					输出分区的结果信息
				   q   quit without saving changes
					不保存退出
				   t   change a partition's system id
					改变分区的系统id==改变分区类型（LVM 增加swap分区大小)
				   u   change display/entry units
					改变分区的方式 是否按照扇区进行划分e
				   w   write table to disk and exit
					将分区的信息写入分区表并保存退出
			开始分区：
				a 规划4个主分区，每个分区1G
					分区操作过程
						n -- 选择分区的位置 -- 大小
						t -- 改变分区的类型
					分区操作检查
						p
				b 规划3个主分区，一个拓展分区，每个主分区1G，剩余的为扩展分区
					有了扩展分区，才能划分逻辑分区
			d 保存退出，让系统可以加载识别分区信息
				让系统可以加载识别分区文件
					partprobe /dev/sdb
		- 磁盘分区，大于2T的磁盘
			使用fdisk，每个分区最大52G
			1. 虚拟化一块磁盘
			2. 使用parted命令进行分区
				parted /dev/sdb
				mklabel，mktable LABEL-TYPE 创建一个分区表（默认mbr）
					mklabel gpt 修改磁盘分区类型
				print 显示分区信息
				mkpart PARY-Type fs-type 
					mkpart [primary|logical|extended] [ext4|vfat|xfs] 开始 结束
					parted /dev/vda mkpart primary fat32 36.0GB 36.5GB
					分区方法
						mkpart primary 0 2000G
					parted分区了就会生效
				quit 退出分区转态
				rm NUmber 删除分区
			3. 加载分区
				partprobe /dev/sdb
			4. 挂载
					
			
	02. 磁盘格式化操作 （创建文件系统）
		mkfs.xfs /dev/sdb1
		mkfs -t xfs /dev/sdb2
		
		创建文件系统：磁盘分区存储数据的方式
		
		ext3/4 centos6
		xfs		centos7 格式化效率更高 数据存储效率提升（数据库服务器）
			[root@qiman ~]# mkfs.xfs /dev/sdb1
			meta-data=/dev/sdb1              isize=512    agcount=4, agsize=65536 blks
					 =                       sectsz=512   attr=2, projid32bit=1
					 =                       crc=1        finobt=0, sparse=0
			data     =                       bsize=4096   blocks=262144, imaxpct=25
					 =                       sunit=0      swidth=0 blks
			naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
			log      =internal log           bsize=4096   blocks=2560, version=2
					 =                       sectsz=512   sunit=0 blks, lazy-count=1
			realtime =none                   extsz=4096   blocks=0, rtextents=0
	03. 磁盘挂载应用
		mount /dev/sdb1 /mnt
		检查确认
			df -h
		如何实现开机自动挂载
			1. 使用/etc/rc.local 文件
				mount /dev/sdb1 /mnt
				如果设置未生效，则文件没有执行权限
				chmod +x /etc/rc.d/rc.local
			2. 使用/etc/fstab文件中进行设置
				UUID=2653fb0a-af55-432d-a5c0-771b16dcc70a /                       xfs          defaults        0 0
				挂载设备								  挂载点                  指定文件类型  挂载参数       是否备份 是否检查
				
	04. 企业磁盘常见问题
		1）磁盘满的情况
			模拟磁盘空间不足
			dd if=/dev/zero of=/mount01 bs=10M count=10
			磁盘满了的提示 No space left on device
			a 存储数据过多了
				block存储空间不足
				- 解决方法
					a 删除大空间文件
					b 找到大的空间目录
						du -sh /* | sort -nr
					补充：按照数值排序 sort
						sort -n
							-n 按照数值排序
						sort -h 人类可读的方式
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
			b inode不足了：出现了大量的小文件
				删除小文件过多
					Argument list too long
				- 解决磁盘inode占用100%问题
					1. 查看inode占用情况
						inode table 
						df -i 查看inode占用情况
					2. 查出inode占用大的目录
						for i in /var/*;do echo $i; find $i | wc -l; done 当前各大文件夹占用inode情况
						# 排序
						sudo find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
					3. 删除占用大的文件/目录
	05. 如何调整swap空间
		查看swap空间 free -h /swapon -s
		a 从磁盘分出一部分空间个swap分区使用
			dd if=/dev/zero of=/tmp/1G bs=100M count=10
		b 将指定磁盘空间作为swap空间使用
			mkswap /tmp/1G
		c swap空间挂载
			swapon /tmp/1G
		d swap空间卸载
			swapoff /tmp/1G
# 课程总结
	1）掌握磁盘体系结构
	2）磁盘的内部和外部结构（磁头 磁道 扇区 柱面）-- 存储服务
	3）磁盘分区的方法
		fdisk 小于2T
		parted 大于2T
		fdisk -l 查看磁盘大小
	4）如何实现格式化和自动挂载  存储服务 nfs
		/etc/rc.local
		/etc/fstab
	5）磁盘分区满的原因
		block占用过多
			df -h
			删除大文件
			如何找到大文件
				find / -type f -size +500M
				du -sh /etc 针对目录
		inode占用过多
			df -hi
			删除大量的没用的小文件
	6）如何调整swap空间大小 ---- tomcat（java）
		dd
		mkswap
		swapon
		swapoff
		sync 刷新文件缓冲区
# 练习
	
# 拓展