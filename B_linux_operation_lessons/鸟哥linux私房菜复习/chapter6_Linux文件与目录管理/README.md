# Linux文件与目录管理
# 本章所讲解到的命令
	cd
	pwd
	mkdir
	rmdir
	ls
	cp
	rm
	mv
	basename
	dirname
	cat
	tac
	nl
	more
	less
	head
	tail
	od
	touch
	umask
	chattr
	lsattr
	file
	which
	whereis
	locate/updatedb
	find
	
# 本章主要内容
	1. 目录与路径
		- 相对路径与绝对路径
			绝对路径：一定是由根目录开始的
				绝对路径的精确度高
				shell中必须使用绝对路径
			相对路径：不是由根目录开始的
				.. 上一层目录
		- 目录的相关操作
			- 一些关于目录的特殊符号
				.	代表当前目录
				..	代表上一层目录
				-	代表前一个工作目录
				~	代表目录使用者（登录用户）所在的家目录
				~account	代表account这个用户的家目录（account是账号名称）
			- cd	change directory	切换目录
				- 利用相对路径时，必须确认你当前所在路径
			- pwd	显示当前所在目录
				- options
					-P	显示出真实文件所在路径，而非使用链接路径
			- mkdir	建立一个新的空目录
				- options
					-m	建立文件时指定文件权限
						mkdir -m 711 testfile
					-p	层级目录建立
			- rmdir	删除一个空目录
				- options
					-p	层级删除目录
				- 被删除的目录中一定不能包含其他目录或文件
		- 关于执行路径的变量	$PATH
			- 增加新的执行路径
				PATH="${PATH}:/root"
			- 当多个执行路径中具有相同的命令时
				被先查询到的命令，优先被执行
			- 不同身份用户预设的PATH不同，能够随之执行的命令也不同
			- 本目录(.)最好不要放到PATH中
			
	2. 文件与目录管理
		- 文件与目录的查看	ls
			ls [-adlhn] filename/dirname
				-a	显示全部文件，包括隐藏文件
				-d	仅显示目录本身，而不列出目录内的内容
				-l	显示文件属性和文件名称详细信息
				-n 	显示UID/GID,而不显示名称
				-h	以人类易读的方式显示容量
			ls [--color={never,auto,always}] filename/dirname
				不显示，系统自动判断，总显示
			ls [--full-time] filename/dirname
				完整的时间显示
				--time={atime 文件访问时间,ctime 状态改变} 指定显示的时间，默认为修改时间 mtime
			ls -i 	显示文件的inode号码
		- 复制，删除和移动	cp，rm，mv
			- cp	复制文件与目录
				cp [-aipr] source destination
					-a 	-dr --preserve=all
					-d	若源文件链接文件，则复制链接文件属性，而非文件本身
					-i	当destination存在时，在覆盖是询问
					-p	连同文件属性一起复制，而非预设属性
					-r	目录层级复制
					-s	符号链接
					-l	硬链接
					-u	destination比source旧才更新destination，或destination不存在
					--preserve=all	处理-p权限外，还加入SELinux，links，xattr等权限也复制了
				cp [options] source1 source2 ... directory
				- 预设中，cp的目标位置的权限位目标位置用户的权限
				- cp默认复制的原始文档，而非链接文件
				- 当在普通用户，使用-a参数，对应的用户可能因为权限问题无法完全复制过来（权限）
			- rm	移除文件或目录
				rm [-fir] 文件或目录
					-f	强制删除
					-i	删除前询问
					-r	递归删除
				\rm 可以忽略掉alias的设置
				- rm删除特殊文件名称的文件 -aaa-文件
					1. rm ./-aaa-
					2. rm -- -aaa-
			- mv 移动文件与目录，或改名
				mv [-fiu] source destination
				mv [options] source1 source2 ... directory
					-f	强制，如果destination已经存在，不会询问，直接覆盖
					-i	交互询问是否覆盖
					-u	如果destination已经存在，且source比较新，才会更新
				- 同一目录下操作mv，--重命令
				- rename .jpg .txt filelist
				- 如果source为多个文件，则destination一定是个目录
		- 获取路径的文件名称和目录名称
			- basename /etc/sysconfig/network 获取最后的文件名称
			- dirname /etc/sysconfig/network 获取目录名称
	3. 文件内容查看
		cat	Concatenate		从第一行开始显示文件内容
			-n	显示行号，连同空白行也显示
			-b	显示行号，空白行不标记
			-A	 -vET的组合，列出一些特殊符号
		tac	从文件最后一行开始显示
		nl	显示时带行号
			-b	指定行号指定方式
				-b a	空白行也包括
				-b t	空行不列出行号
			-n	列出行号显示位置
				-n ln 最左
				-n rn 最右 且不加0
				-n rz 最右 且加0
			-w	行号显示所占位数
		more	一页一页显示
			space	下一页
			enter	下一行
			/string	向下查找string
			:f		显示文件名称及当前所在行数
			q		离开文档
		less	比more更好，可以前翻页
			space	下一页
			enter	下一行
			/string	向下查找string
			:f		显示文件名称及当前所在行数
			q		离开文档
			b		上一页
			g	第一行
			G	最后一行
		head	只看头几行
			head [-n number] 文件
				-n	显示几行
				负数，不包括后面几行，其余全部显示
				head -n -100 仅列出最后100行之前的内容
		tail	只看尾几行
			tail [-n number] 文件
			tail -n +100 仅列出最前面100行以后的信息
			tail -f filane 	持续监测
		od		以二进制方式读取文件内容
			od [-t TYPE] 文件
				a 利用预设字符输出
				c 利用ASCII输出
				d[size] 十进制，每个整数占用size bytes
				f[size] 浮点
				o[size] 八
				x[size] 十六
			- od -t oCc /etc/issue 显示ascii对照表
		touch	修改文件时间或创建新文件
			mtime
			ctime
			atime
			touch [-acdmt] 文件
				-a 仅修改atime
				-c 仅修改ctime，如果文件不存在则不建立新文件
				-d --date="日期或时间"
					touch -d "2 days ago" bashrc
				-m 仅修改mtime
				-t 指定时间[YYYYMMDDhhmm]
					touch -t 201406150202 bashrc
			- 复制时，ctime不能够被复制的
	4. 文件与目录的预设权限与隐藏权限
		- 文件预设权限，umask
			umask -S	以符号显示权限
			文件 666
			目录 777
			- umask为预设值，拿掉的权限
			- 作用
				项目使用，使得同一组的人员可以编辑文档
		- 文件隐藏属性
			chattr [+-=][options] 文件或目录 设置文件隐藏属性
				- 在ext文件系统值才完全支持
				- options
					a 设置后，文件只能增加内容，不能删除也不能修改，只用root可以设置这一属性
					i 不能删除，改名，设置链接，不能写入
					s 删除了就彻底删除了
					d dump执行时，不被备份
					u 被删除了，有备份
					S 同步写入
					A atime不变
					- xfs仅支持AadiS
			lsattr [-adR] 文件或目录 显示隐藏属性
				- options
					-a 将隐藏文件属性也列出来
					-d 仅列出目录本身信息
					-R 连同子目录也列出来
		- 文件特殊权限：SUID，SGID，SBIT
			- Set UID
				s -- 在文件属主的x权限位上
				- suid仅对二进制程序有效
				- 执行者对于该程序具有x的可执行权限
				- 本权限仅在执行该程序过程中有效
				- 执行者将拥有该程序属主的权限（owner）
				- passwd修改用户密码
					1. qiman用户对于/usr/bin/passwd拥有可执行权限
					2. passwd的拥有者为root
					3. 当qiman执行passwd时，会展示拥有root权限
					4. 那么/etc/shadow 可以被修改
				- suid对目录无效
			- Set GID
				s -- 在文件属组的x权限位
				- suid对二进制程序有效
				- 程序执行者对该程序来说具有x权限
				- 执行者在执行过程中获得该程序群组的权限
					命令的属组
				locate命令
				- 可以对一个目录设置
					- 使用者对此目录具有rx，则能进入此目录
					- 使用者在此目录下的有效群组，变为该目录的群组
					- 用途，若使用者在此目录下有w，则使用者所建立的新档案，该新档案的群组与此目录的群组相同
						锁定目录下文件的属组
					- 使用者在此目录下的有效群组变为该目录的拥有者的有效群组
			- Sticky Bit
				- 只对目录有效
				- 当使用者对此目录具有wx时，具有写入权限
				- 当使用者在该目录下建立文件或目录时，只有自己与root才能删除并修改该文件，删除/重命名/移动
			- SUID/SGID/SBIT权限设置
				4	SUID
				2	SGID
				1	SBIT
				u+s
				g+s
				o+t
			- 出现大S大T
				表示空，user，other group自身没有可执行权限
		- 查看文件类型 file
			file filename
	5. 命令与文件的查找
		- 命令所在文件查找
			- which 寻找执行档
				- 根据PATH查找
				- 内置命令找不到
				which -a command
					-a 将PATH所有路径中找到的指令都列出来，默认只列出找到的第一个
		- 文件名查找
			- whereis 通过一些特定的目录来寻找文件，命令所在文件和帮助文件
				whereis [-bmsu] 文件或目录名
					-b 只找binary格式文件
					-m 只找manul路径下的文件
					-s 只找source来源的文件
					-u 找不在上面三种中文件
				whereis -l 列出whereis回去查询的主要目录
			- locate/updatedb
				[root@qiman ~]# locate ifconfig
				/usr/sbin/ifconfig
				/usr/share/man/de/man8/ifconfig.8.gz
				/usr/share/man/fr/man8/ifconfig.8.gz
				/usr/share/man/man8/ifconfig.8.gz
				/usr/share/man/pt/man8/ifconfig.8.gz

				locate [-ir] keyword
					-i	忽略大小写
					-c	仅统计找到文件数量
					-l	仅输出几行，-l 5
					-S	输出locate所使用的资料库，和资料库包含文件数量
						[root@qiman ~]# locate -S
						Database /var/lib/mlocate/mlocate.db:
							8,993 directories
							60,997 files
							3,003,110 bytes in file names
							1,375,372 bytes used to store database
					-r	后面接正则表达式
				- 实际上是在/var/lib/mlocate中查找
				updatedb	读取/etc/updatedb.conf设置文件，更新/var/lib/mlocate文件库
			- find
				find [PATH] [option] [action]
				- option
					1. 时间相关参数
						-mtime n：n天之前的一天内被更改过的文件
						-mtime +n: 列出n天之前（不含n天）
						-mtime -n：列出n天之内（含n天）
							find / -mtime 0 24小时内有变动过的文件
						-newer file: file为一个存在的档案，列出比file还要新的文件
								|4	|
									-4 ->
							<-	+4
						|7	|6	|5	|4	|3	|2	|1	|now
						find /old -type f -mtime +10 -delete 删除历史数据信息
					2. 与使用者或群组相关参数
						-uid n: n为数字uid
						-gid n
						-user username
						-group groupname
						-nouser：	在/etc/passwd中找不到用户的文件
						-nogroup：在/etc/group中找不到组的文件
					3. 与文件权限以及名称有关的参数
						-name filename: 查找文件名称为filename的文件
						-size[+-]SIZE：查找比SIZE大（+）或小（-）的文件
							SIZE：c byte,k 1024bytes,
							-size +50k
						-type TYPE 查找文件类型
							f 一般文件
							b,c 装置文件
							d 目录
							l 链接文件
							s socket 
							p FIFO
						-perm mode 查找权限恰好为mode1的文件
							-rwsr-xr-x 4755
						-perm -mode 查找权限必须包括mode的文件
							-rwxr--r--,-perm -0744
						-perm /mode 查找包含任意mode权限文件也会被找到
							- 找到具有SUID或SGID的文件
								find /usr/bin /usr/sbin/ -perm /6000
					4. 额外可进行的动作
						-exec command command为其他指令，接额外的指令来处理查找到的结果
							find /usr/bin /usr/sbin -perm /7000 -exec ls -l {} \;
							{} find找到的内容
							-exec 开启 \;结束
						-print 将结果打印到屏幕上，预设
					-maxdepth 层级深度
					-inum 根据inode查找
				- 几个find实例
					- 找到/etc目录下大小为50k到60k之间的文件
						find /etc -size +50k -a -size -60k -exec ls -l {} \;
							-a and
					- 找到/etc目录下大小为50k且非root用户的文件
						find /etc -size +50k -a ! -user root -exec ls -ld {} \;
							! 反向选择
						find /etc -size +50k -a ! -user root -type f -exec ls -l {} \;
					- 找到/etc目录下大于1500k以及容量等于0的文件
						find /etc -size +1500k -o -size 0
							-o or
	6. 权限与命令之间的关系
		- 让使用者能够进入某个目录，并成为工作目录
			- 可使用指令 cd等
			- 目录所需权限 至少拥有x
			- 额外需求 如果想查询文件ls，需要r权限
		- 使用者在某个目录中读取一个文件的基本权限
			- 可使用指令
				cat，more less 等
			- 目录所需权限
				至少x
			- 文件所需权限
				至少具有r
		- 让使用者可以修改一个文件基本权限
			- 可使用指令
				vi，cat 等
			- 目录所需权限
				至少x
			- 文件所需权限
				至少具有rw
		- 让使用者可以建立一个文件基本权限
			- 目录所需权限
				使用者在该目录下具有wx，重点在w
		- 让使用者进入某目录并执行该目录下的摸个指令基本权限
			- 目录所需权限
				至少x
			- 文件所需权限
				至少x
# 本章实例
	- 将某个root用户文件复制个一个普通用户
		cp
		chown newuser:newuser
# 本章总结

# 本章练习