# 操作系统知识回顾
# 知识回顾
	1. 第二个阶段的回顾：系统安装和远程连接
		01. 虚拟化环境部署（网络配置）
			NAT 模式， 实现其他宿主机可以远程连接虚拟机
				NAT的端口转发
		02. 进行系统安装
			01. 分区
			92. 系统软件包组安装
			补充：centos7
				网卡的默认命令方式 ensxx-ethernet sockets 以太网槽位
								   eth 以太网 0 1
				- 修改方式：
					a 安装系统时，菜单界面 -- install centos7 - tab -- net.ifnames=0 biosdevname=0
					b 在系统中
						- 编辑网卡配置文件中的网卡名
							vim /etc/sysconfig/network-scripts/ifcfg-ens33
								NAME=eth0
								DEVICE=eth0
						- 修改网卡名规则内核文件
							/etc/default/grub -> net.ifnames=0 biosdevname=0
								GRUB_CMDLINE_LINUX="biosdevname=0 net.ifnames=0 rhgb quiet"
						- 使得系统重新加载grub配置文件
							grub2-mkconfig -o /boot/grub2/grub.cfg
			- 远程连接和连接异常
# 课程介绍
	1. 第三阶段回顾
		1. 目录和文件创建命令
		2. vi/vim详细使用技巧
	- vim 常见错误说明
		a vim命令后面一定要跟文件信息
		b vim 只能编辑存在目录中的文件
			vim 不能创建目录
		c 编辑文件突然非正常状态退出
			- 会出现隐藏文件 .oldgirl.txt.swap
			- 处理方式
				Open 打开只读
					不会删除swap文件
				Edit anyway 继续编辑
					- 不是保存出现异常时的文件内容
					不会删除swap文件
				Recover 恢复
					可以恢复中断前的内容，但不会删除swap文件
				Delete it 删除
					会删除swap文件
				Quit 退出
					不会删除swap文件
				Abort 退出
			- vim 编辑原理
				vim /test.txt -> 判断时候存在swap文件 -> 存在 swap attention
													  -> 不存在 是否正常编辑文件 -> 否 编辑内容时产生swap内容
																				 -> 是 编辑swap文件-> wq! -> \mv /.test.swap /test.txt
				只要编辑文件，就会产生swap文件
			- 解决问题
				- 进行查看文件内容 - O
				- 确认文件内容是否需要恢复
					yes R
					no E 重新编辑
				- 将临时文件删除
					D删除
					rm 删除.swap文件
	- 查看文件信息的方法
		a ls 查看文件信息
			ls - 查看目录中有什么数据信息
			ls -l - 查看文件属性信息
			ls -ld - 查看目录中的信息
			ls -la - 查看文件中所有目录和文件信息
			ls -ltr - 所有文件详细信息按时间排序，最新的到最后一行,逆向排序
			- 企业工作中的一个问题
				多个运维人员维护服务器，下班，交代，将oldboy中最新的数据文件进行编辑
		b 查看文件信息内容
			cat 查看单个文件和多个文件
				cat -n 显示行号
			less/more 分页查看
			less
				回车 下一行
				空格 下一页
				方向键上 上一行
				b	上一页
				搜索 /search_string
				less -N 显示行号
				gg 首行
				q 退出查看
			more
				回车 下一行
				空格 下一页
				f 往上一行
				b 往上一页
				读到最后一行，自动退出
			head/tail 前几行，后几行
	- 直接编辑文件命令方法
		echo "oldboy" >> /oldboy/oldboy.txt
		补充：echo 命令用法说明
			输出连续的序列信息
			1. echo {1..100} 1 2 3 ...
			2. echo {01..100} 001 002 ...
			3. echo {a..z} a b c
			输出不连续序列
				echo {01..10..2} 01 02 03 04
			输出无规律的序列
				echo {1,3,5,7}
				mkdir -p /oldboy/oldboy01/oldboy02/{www,bbs,blog}
		- 如何直接在文件中添加多行内容
			cat >> test.txt <<EOF
			cat >> test.txt <<(标准输入)
	- 过滤筛选文件内容
		三剑客命令
		老三：grep	过滤筛选信息
		老二：sed	修改替换文件内容，擅长对文件中的行进行操作
		老大：awk	擅长统计分析文件内容 擅长对文件中列进行操作
		- grep 命令如何进行过滤
			1. 筛选指定信息
				grep "oldboy" test.txt
			2. 将过滤出的行的上几行的信息显示出来
				grep -B 1 "oldboy" test.txt
			3. 将过滤出的行的下几行的信息显示出来
				grep -A 1 "oldboy" test.txt
			4. 将过滤出的行的上下几行的信息显示出来
				grep -A 1 -B 1 "oldboy" test.txt
				grep -C 1 "oldboy" test.txt 上下一行
			5. 统计oldgirl在其中出现了多少次
				grep -c "oldgirl" test.txt 统计出现了多少行
		- sed
			sed "/oldboy/p" test.txt 把原有的内容也显示
			sed -n "/oldboy/p" test.txt 只显示过滤内容
				p print 将过滤信息输出
				-n 取消默认输出（源文件）
		- awk
			awk "/oldboy/" test.txt
	- 修改文件部分内容信息
		1. sed命令 -- 真正修改文件内容
			将test.txt文件内容替换
			sed "s#oldboy#python#g" /oldboy/test.txt
			任何文件修改时，做文件备份
			sed -i "s#oldboy#python#g" /oldboy/test.txt 修改文件内容
		2. tr命令 -- 不会真正修改文件内容
			- tr的替换，一对一替换
			文件内容替换
			tr	"要改的内容"	"要改成的内容" < test.txt 只是显示，不会修改文件
- 练习题
	在指定目录下创建20个文件，20个文件的名称为oldboy01,oldbocy02,.. oldboy20
	touch
	mkdir
	echo
	序列符号不是所有的命令都识别
- 拓展作业
	tail 命令查看
		tail -F/-f 有什么区别
		- tail -f	等同于--follow=descriptor, 根据文件描述符进行追踪，当文件改名或被删除，追踪停止
		- tail -F	等同于--follow=name --retry，根据文件名进行追踪，并保持重试，即该文件被删除或改名后，如果再次创建相同的文件名，继续追
		- tailf		等同于tail -f -n 10 如果文件不增长，它不会去访问磁盘，可以减少磁盘访问
	tr 替换时，为何会替换的如此的乱
		tr "123321" "abc" -> ccc
- 课程知识总结
	1. vim编辑命令常见异常情况
	2. vim编辑命令的执行原理
	3. 如何查看文件内容命令 cat less more head tail 
	4. 如何直接编辑文件内容
		单行编辑 echo {} 序列符号
		多行编辑 cat >> file <<EOF
	5. 如何过滤文件内容
		三剑客
			grep
			sed
			awk
	6. 如何修改
		1. 真正修改替换 sed
		2. 假装替换 tr
- 拓展作业
	tr命令替换信息的原理
- sed命令 -- 鸟哥的linux私房菜
	sed [-nefr] [actions]
	参数说明
		-n 只显示文件中被处理的行
		-e 
		-f 后面跟sed动作配置文件
		-r 使用延伸正则
		-i 直接修改原文件内容
	动作说明
		[n1,[n2]]function
		n1,n2, 选择进行操作行数指定
	function说明
		a 新增，在a的后面加字符串，目前的下一行新增
			nl /etc/passwd | sed '2a drink tea' 插入单行
			nl /etc/passwd | sed '2a drink tea..\
								> drink beer ?' 插入多行
		c 取代，替换行
			nl /etc/passwd | sed '2.5c No 2-5 number'
		d 删除，删除行
			nl /etc/passwd | sed '2,5d'
			
		i 插入，上一行
		p 打印
			nl /etc/passwd | sed -n '5,7p'
		s 取代 1,20s/old/new/g
			sed 's/^.*inet//g'
- awk
	awk '条件类型1{动作1}条件2{动作2}...' filename
		$0 - 一整列,$1 - 一整行,$2
		NF -- 每行列数
		NR -- 当前处理第几行
		FS -- 分割符，默认空白键
		awk 'BEGIN {FS=":"}$3<10{print $1 "\t" $3}'
- tr 从标准输入中替换，缩减和删除字符，并将结果写到标准输出中
	- 子串1用于查询，子串2用于转换，tr执行时，子串1中的字符被映射到子串2中的字符，然后开始转换
	- 大小写转换
	- 去除控制字符
	- 删除空行
	参数：
		-c 用字符串1中的字符集的补集替换此字符集，要求字符集为ASCII
		-d 删除字符串1中所有输入字符
		-s 删除所有重复出现字符序列，只保留第一个，即将重复出现字符串压缩为一个字符串
	tr 字符串1 字符串2
		- 当str1 比str2短，abc/1234 那么abc 替换为123，而4被忽略
		- 当str1 长于str2， abcd/123 它会使用str2中的字符去替换没有替换到的字符
			tr abc 空格，那么转换成空格
		- 所以要保持str1和str2保持一致
	指定字符串内容时，只能使用单字符或字符串列表范围
	- tr -s "[a-z]" 删除重复字符，只保留第一个
	- tr -s "[\012]" < test.txt 删除空行
	- tr "[a-z] "[A-Z]" 大小写转换
	
	