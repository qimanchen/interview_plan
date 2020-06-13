# 第七章，linux磁盘与档案系统管理

# 命令

# 内容
	1. 认识linux文件系统
		- 磁盘组成与分割
			- 组成
				a 磁盘主轴 决定磁盘转速 rpm-round per minutes
				 家用 7200 rpm 5400rpm
				 企业 15k rpm 10k rpm
				b 磁盘盘片 用于存储数据
				c 磁盘磁头 用于读取数据
				d 磁盘接口 用于连接主板 用于连接阵列卡
			- 磁盘一些知识
				扇区为最小物理存储单位，有512bytes和4k两种格式
				扇区结合成一个圆柱 - 磁面/磁柱
				磁盘分割表有两种方式，MBR和GPT
				- MBR分割表中，第一个扇区最重要，MBR（Master boot record) 446bytes和分割表partition table 64bytes
				- 磁盘命名
					/dev/sda 第一块磁盘
					/dev/vd[a-p] 虚拟磁盘
					/dev/md[0-128] 磁盘阵列
					LVM /dev/VGNAME/LVNAME
		- 文件系统特性
			- 每种文件系统的文件属性和权限不同
			- 一个可被挂载的数据为一个文件系统，而不是一个分割槽
			- 权限与属性放置在inode中，数据放置在data block中
			- superblock记录着整个文件系统的信息，inode和block总量，使用情况，剩余情况
			- superblock，inode，block一些特性
				superblock记录文件系统的全部信息，inode/block情况，文件系统格式信息
				inode记录文件的属性，一个文件占用一个inode，同时记录指向block指针
				block记录文件内容，大文档会占用多个block
			- 数据存储方法
				- 索引式文件系统
				- FAT 链路
					容易造成磁盘空间碎片化
		- Linux的ext2文件系统(inode)
			文件系统在格式时就将inode和block设置好了，除非重新格式化或使用resize2fs
			- ext2格式化
				Boot Sector | Block Group ...
				Block Group
					superblock | 文件系统描述 | block bitmap | inode对应表 | inode table | data block
				- 文件系统最前面的boot sector 可以安装开机引导程序
			- data block
				ext2 支持block大小有1K 2K 4K
				- ext2文件系统block的限制
					block大小和数量格式化后不可以改变
					- 每个block最多放置一个文件
			- inode table
				- inode存取内容
					ls -l 列出来的（文件名除外）
					文件指向（data block）
				- inode特点
					- 每个inode大小固定为128bytes（ext4和xfs可设定到256bytes）
					- 每个文件占用一个inode
					- 系统读取文件时，先找inode，并分析inode所记录的权限与使用之是否符合
					- inode分为12个直接，一个间接，一个双间接，一个三间接
						利用额外的block来记录block指向
			- superblock
				- 记录的信息
					block/inode容量和使用情况
					block/inode大小
					文件系统挂载时间等相应操作时间
					valid bit 0 已被挂载 1 未被挂载
					1024bytes
				- superblock备份
			- 文件系统描述
				每个block group的开始于结束block号码
			- block bitmap
				记录未使用的block
			- inode bitmap
			- dumpe2fs 查询ext文件系统的superblock信息
				dumpe2fs [-bh] 设备名称
				 -b 列出坏轨部分
				 -h 仅列出superblock信息
			- blkid 列出系统中被格式化的装置
		- 与目录树的关系
			- 目录存储文件名称
			- 目录
				建立目录 -- 文件系统分配一个inode和至少一个block
					block记录在这个目录下的文件名和该文件名称占用的inode号码信息
				- ls -li 查看inode
			- 文件
				inode 仅有12个直接指向
			- 目录树读取
			- 文件读取流程
			- 文件系统大小
				文件系统不能太大
		- ext文件系统存取与日志式记录功能
			- 文件创建
				a 目录权限
				b inode bitmap
				c block bitmap
				d superblock
			- 数据不一致
				e2fsck 检查
			- 日志式文件系统
				- 在一个存储区域记录存储日志
				- dumpe2fs信息中的journal记录着这样的信息
		- linux文件系统的运行
			- 异步处理
				确认文件是否被修改,clear or dirty, 系统定时将dirty数据存入到磁盘中
			- 系统将常用文件数据放置在内存的缓冲区，加速文件系统的读写
			- sync强制将dirty数据写会磁盘
			- 不正常关机，会导致开机长时间磁盘检测
		- 挂载点
			- 挂载点一定目录，该目录为文件系统的入口
			- xfs顶层目录indoe一般为128
			- 同一个文件系统中，相同的inode相当于一个文件多个入口
		- ls -l /lib/modules/$(uname -r)/kernel/fs 查看系统支持的文件系统
		- linux VFS
		- xfs文件系统
			- xfs分为三个部分 
				data section
					block有多种选择 512bytes~64k
					inode 256bytes~2M
					allocation groups -- block groups
				log section
					磁盘操作记录
				realtime section
					extend
			- xfs文件系统信息查看
				xfs_info 挂载点|设备名称
				- df -T /boot 查看挂载点的文件系统类型
			
	2. 文件系统的简单操作
		- 磁盘和目录的容量
			df [-hiT] 目录或文件名
				-h 人类可读
				-i inode
				-T 文件系统
				-a 所有
			- 特别关注根目录的容量
			-/dev/shm/ 内存虚拟
			
			du [-sSkmh] 文件或目录名称
				-s 列出总量，不列出每个目录占用情况
				-S 不包括子目录统计
				-k kbytes
				-m mbytes
				-a 显示所有文件容量和名称，预设只统计目录下的
				du -s /root 列出目录总量
		- 硬链接符号 ln
			- hard link
				多少个文件名连接到这个inode
				- 不能跨文件系统
				- 不能link目录
			- symbolic link
				指向
				会占用inode和block
			- ln [-sf] source destination
				-s symbolic link
				-f 如果目标文件存在，那么移除后再创建
			- 目录link数量
				- 新目录link数为2，上一层目录的link数会加1
			
	3. 磁盘的分割，格式化，检测与挂载
		- 使用一个新的磁盘
			a 磁盘分割
			b 格式化，建立文件系统
			c 检测文件系统
			d 挂载
		- 查看磁盘分割状态
			- lsblk 列出系统上所有的磁盘列表
				lsblk [-dfimpt] device
				 -i 
				 -f 同时列出文件系统
				 -t 列出磁盘详细信息
				 -p 列出装置完整名称
			- blkid 列出装置uuid信息
			- parted 列出磁盘分割表类型和信息
				parted device_name print
				parted /dev/sda print  -- 查看分割类型
				du -s 查看目录大小
				df -T 查看磁盘文件系统类型
			- MBR
				fdisk
					-有限制
			- GPT
				gdisk
				 gdisk device 进入磁盘进行交互操作
				 code：
					linux 8300
					swqp 8200
					0700 windows vfat
					gdisk -L 可以查看这些code
				- gdisk针对的是磁盘，不是分割槽
				- 一定要什么分割类型使用什么命令
				- /proc/parttions 显示分割槽
				- gdisk操作完
					partprobe [-s] 更新linux核心分割表
				
			- 磁盘操作
				a lsblk/blkid 找到磁盘
				b parted /dev/xxx print 找到磁盘分割类型
				c gdisk/fdisk进行操作
		- 磁盘格式化
			mkfs
			mkfs.xfs [-b bsize] [-d parms] [-i parms] [-l parms] [-L label] [-f] [-r parms] device
				-b block
				-d data section设置
				-f 强制格式化
				-i inode
				-L Label name
				-r realtime section
			mkfs.ext4 [-b size] [-L label] device
				-b 1k 2k 4k
		-xfs文件系统对raid优化
			strip 大文件大，小文件64k 4K-1M
		- 文件系统优化
			- xfs_repair 处理xfs
				xfs_repair [-fnd] device
					-f 后面跟一个文件装置
					-n 只检查
					-d 单用户模式检测修复
			- 修复时，文件不能挂载
			- fsck.ext4 处理ext4
				fsck.ext4 [-pf] [-b superblock] device
					-p 自动回复
					-f 强制检查
					-D 目录最佳化配置
					-b superblock位置
						1k 8193
						2k 16384
						4k 32768
						dumpe2fs -h /dev/vda5|grep 'Blocks per group‘ 找到superblock
		- 文件系统挂载与卸载
			- 挂载前注意事项
				a 同一文件系统不能重复挂载在不同目录上
				b 同一目录不能挂载多个文件系统
				c 作为挂载点的目录为空目录
					- 如果原目录为非空目录，那么目录里面的内容会被屏蔽
			- mount
				mount -a
				mount [-l]
				mount [-t 文件系统] LABEL='' 挂载点
				mount [-t 文件系统] UUID='' 挂载点
				mount [-t 文件系统] 装置名 挂载点
					-a 将/etc/fstab中所有未挂载的磁盘都进行挂载
					-l 显示挂载信息时，同时显示label
					-t 指定挂载类型，iso9600(光盘) nfs,cifs,smbfs(网络存储)
					-n 不将挂载情况写入到/etc/mtab中
					-o 额外参数
						async, sync 非同步写入，同步写入，预设为async
						atime, noatime 是否修改读取时间
						ro,rw 只读，可读写
						auto, noauto mount -a 自动挂载
						remount 重新挂载
			- /etc/filesystems 系统指定的测试挂载文件系统类型的优先顺序
			- /proc/filesystems linux系统已经载入的文件系统类型
			- /lib/modules/$(uname -r)/kernel/fs 系统支持的文件系统类型
			- 挂载过程
				blkid /dev/sda
				mount UUID="" 挂载点
				df 挂载点 确认是否挂载成功
			- 挂载光盘
				blkid /dev/sr0
				mkdir /data/cdrom
				mount /dev/sr0 /data/cdrom
				df /data/cdrom
			- 挂载use/vfat
				blkid -- vfat
				mount -o codepage=950,iocharset=utf8 UUID="" /data/usb
		- 重新挂载根目录与挂载非特定目录
			mount -o remount,rw,auto /
		- 目录挂载
			mkdir /data/var
			mount --bind /var /data/var
			ls -lid /data/var
		- umount
			umount [-fn] device/挂载点
			-f 强制卸载，nfs无法读取
			-l 立即卸载文件系统
			-n 不更新/etc/mtab情况下卸载
			- 注意卸载时不要在这个被挂载目录中
		- 磁盘/文件系统参数修改
			- 文件的major和minor数值来代替装置
				磁盘名			major			minor
				/dev/sda		8				0-15
				/dev/sdb		8				16-31
				/dev/loop0		7				0
				/dev/loop1		7				1
				
				mknod 装置名 [bcp] [Major] [Minor]
					b -- 存储设备
					c -- 外设
					p -- FIFO
					Major 主要装置代码
					Minor 次要装置代码
				xfs_admin 修改xfs文件系统的UUID和Label name
					xfs_admin [-lu] [-L label] [-U uuid] device_name
						-l 列出这个装置名称
						-u 列出uuid
						-L 设置label
						-U 设置uuid
					xfs_admin -L vbird_xfs /dev/vda4
				- uuidgen 产生新的UUID
		- 使用UUID指向性更高
		- tune2fs 修改ext4的label name 和UUID
			tune2fs [-l] [-L label] [-U uuid] device_name
	4. 设置开机挂载
		- 系统挂载的一些说明
			根目录必须挂载，而且优先于其他挂载点
			挂载点必须是已经建立的目录
			每个目录和partition只能挂载一次
			进行卸载，必须退出挂载目录
		- /etc/fstab
			[装置/UUID] [挂载点] [文件系统] [文件系统参数] [dump] [fsck]
			01			02		 03			04				05	  06
			01. 装置名 /dev/vda2,UUID=xxx,LABEL=xxx
			02. 挂载点
			03. partition的文件系统
				xfs ext4 ...
			04. 文件系统参数
				mount -o 的参数
			05. 能否被dump备份指令使用
				0
			06. 是否以fsck检测磁盘
				0 - 不检测 
		- 实际文件系统的挂载记录到/etc/mtab 和/proc/mounts中
		- 特殊装置挂载loop挂载（iso档直接挂载使用）
			mount -o loop 设备 挂载点
		- 创建大文件
			a 创建大文件
				dd if=/dev/zero of=/srv/loopdev bs=1M count=512
			b 大文件格式化
				mkfs.xfs -f /srv/loopdev
			c 挂载
				mount -o loop UUID=xxx /mnt
	5. swap空间配置
		- 使用实际分割槽建立swap
			a 分割
				gdisk /dev/sda
				8200
				partprobe
			b 格式化为swap
				mkswap /dev/sda6
			c 查看/载入
				free 查看
				swapon /dev/sda6 载入
				swapon -s 查看swap装置用那些
		- 使用文件建立swap
			a dd if=/dev/zero of=/tmp/swap bs=1M count=128
			b mkswap /tmp/swap
			c swapon /tmp/swap
				swapon -s
			d swapoff /tmp/swap
			swapon -a 会自动识别/etc/fstab中的设置
	5. 文件系统的特殊查看与操作
		- 磁盘空间浪费问题
			ll -sh 查看目录消耗block大小
		- 利用gnu的parted进行分割
			parted [device] [指令[参数]]
				指令：
					新增 mkpart [primary|logical|extended] [ext4|vfat|xfs] 开始 结束
					显示 print
					删除 rm [partition]
			parted /dev/vda unit mb print 指定单位
		- parted 实例
			parted /dev/vda mkpart primary fat32 36.0GB 36.5GB
			parted /dev/vda print
			partprobe
			lsblk /dev/vda7
			mkfs -t vfat /dev/vda7
			blkid /dev/vda7
			vim /etc/fstab
			mount -a
			df /data/win
# 实例

# 练习