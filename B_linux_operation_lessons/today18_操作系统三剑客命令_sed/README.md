# 课程回顾
	1） 正则符号
		基础正则
			^	开头
			$	结尾
			^$	匹配空行
			.	匹配任意一个字符，空行除外
			*	匹配前一个字符0次或任意次数
			.*	匹配所有任意字符
			\	转义字符
			[]	匹配多个字符信息，多个字符匹配时是或者的关系
			[^]	对匹配信息进行排除
		扩展正则
			grep -E,egrep
			sed -r
			+	匹配前一个字符1次或任意次数
			|	与
			()	将多个信息进行一个整体进行过滤
				进行后项引用前项
			{}	指定匹配前一个字符连续出现了多少次
				{n,m} 
			?	匹配前一个字符0次或1次
			
# 课程介绍
	01. sed命令概述说明
		stream editor for filtering and transforming text
		字符流编辑工具 == 按照每一行中的字符进行处理操作
		ps:全屏编辑工具 vim
		- sed操作对象
			- sed处理是文本文件（小文件）
			- 日志文件和配置文件
		- sed命令作用说明：
			1） 擅长对行进行操作处理
			2）擅长将文件的内容信息进行修改调整/删除
			编写脚本：修改文件内容信息时
			- 网络服务中的IP地址进行修改
				- 自动修改网卡地址脚本
					1. 修改地址
						sed -i 's/IPADDR.*/IPADDR=$ip/g' /etc/sysconfig/network-script/ifcfg-eth0 &&\ 
					2. 重启网络服务
						systemctl restart network &&\ 执行完这个命令，才执行下一个命令
					3. 过滤ip，网卡地址信息存储到一个文件中，共享存储
					- 幂等性，多次执行的结果是一致的
				- 重复性的工作
		- 具体功能
			1） a 增
			2） d 删
			3） c，s 改
			4） p 查
	02. sed命令的语法信息
		sed [options] ’条件-处理（指令）' 处理文件信息
			sed -n '/oldboy/p' oldboy.txt	仅显示查询到的内容
			sed -n '/oldboy/!p' oldboy.txt	打印除找到内容之外的内容
	04. sed命令执行原理
		- sed 命令，默认会将内容输出到屏幕上，可以通过-n参数取消输出
		- 处理过程
			- sed有个默认输出
			1. 先找到文件
			2. 先把第一行放到内存中，判断是否满足需要的信息，是否满足条件 （模式空间中）
				若不满足条件，执行下一行
			3. 处理完，接着处理下一行
			4. 直到文件所有的行处理完
	05. sed命令实践操作
		a sed命令查询信息方法
			- 测试文件
				101,oldboy,CEO
				102,zhaoyao,CTO
				103,Alex,COO
				104,yy,CFO
				105,feixue,CIO
			- 根据文件内容的行号进行查询
				- 测试练习
					- 单行显示
						sed -n '3p' person.txt
					- 多行显示
						sed -n '1,3p' person.txt
					- 多行显示，不连续
						sed -n '1p;3p' person.txt
			- 根据文件内容的信息进行查询
				- 测试练习
					- 将有oldboy内容的信息找出来
						sed -n '/oldboy/p' person.txt
					- 将有oldboy到alex行的信息找出来 - 根据内容信息输出多行内容 - 连续
						sed -n '/oldboy/,/Alex/p' person.txt "," 范围
					- 将有oldboy，alex行的信息找出来 - 根据内容信息输出多行 - 不连续
						sed -n '/oldboy/p;/Alex/p' person.txt 多个命令，多个操作
		b 添加信息方法
			- 在文件的第一行添加信息，这个信息读取的是内存中的信息
				sed '1i 100,oldgirl,UFO' person.txt 当前行上面
				sed '1a 100,oldgirl,UFO' person.txt 当前行下面
			- 在文件的最后一行添加信息
				sed '$a 107,oldbbb,ooo' person.txt
			- 添加多行信息
				sed '$a 100\n101' person.txt
				企业中添加配置文件
			- 测试：
				01. 在第三行后面添加oldboy.txt信息
					sed '3a oldboy.txt' person.txt
				02. 在第二行前面添加oldboy.txt信息
					sed '2i oldboy.txt' person.txt
				03. 在有oldboy行的前面添加oldgirl 后面添加olddog信息
					sed -e '/oldboy/iodlgirl' -e '/oldboy/aolddog' person.txt 一条sed命令执行多件事
					ps: 这里 '/oldboy/i oldgirl' 可以用空格隔开
		c sed 删除信息
			
			- 测试练习
				- 删除单行信息
					sed '3d' person.txt
				- 删除多行信息
					sed '3,6d' person.txt
				- 删除有oldboy的行
					sed '/oldboy/d' person.txt 
				- 删除第三行和第六行
					sed -e '3d' -e '6d' person.txt
					sed '3d;6d' person.txt
		d sed 修改信息
			sed 's#原有内容#修改后的内容#g' filename
			PS：当有要匹配的内容中有相应的分割符时，注意/和#切换
			sed 's#()#\n#g' 文件信息 后项引用前项
				- & 表示要匹配的一整行的内容
			
		- 利用sed命令取出ip地址
			1. 提取有ip地址的行
				ip a s eth0 | sed -n '3p'
			2. 取出ip地址
				ip a s eth0 | sed -n '3p'|sed -e 's/.*inet //g' -e 's#/24.*##g'
				
				ip a s eth0 | sed -n '3p'|sed -r 's#^.*net (.*)/24.*#\1#g'
				ip a s eth0 | sed -rn '3s#^.*net (.*)/24.*#\1#gp' 后项引用前项
				ip a s eth0|sed -rn 's#.*inet (.*)/24.*#\1#gp'
				
		- 如何用sed取消空行显示
			sed '/^$/d' person.txt
			sed -n '/^$/!p' person.txt 取反显示，空行不显示
		- sed，awk 都是使用单引号
		- 总结：sed命令的指令信息
			p print
			i insert 		当前行上一行
			a append 		当前行后面一行
			d delete		删除信息
			s substitute	替换信息	s###g(全局替换)
			c 				整行替换
		- 总结：sed命令的参数信息
			-n 取消默认输出
			-r 识别扩展正则
			-i 真实修改内容
			-e sed同时执行多个操作
		- 补充
			- 修改内容直接进行备份
				sed -i.bak 'xx' person.txt 该之前进行备份文件，在对源文件进行修改
			- 企业过程中的一个坑，避免n和i同时使用
				sed -ni 's#Alex#aaa#gp' person.txt
				- n和i参数同时使用，会将文件内容进行清空
				- 所有参数都要放在i前面
	- sed显示行号：
		sed '=' person.txt | xargs -n2
			xargs 组织多行
	- 文件中添加内容的方法
		01. vim/vi
		02. cat >> xxx <EOF
		03. echo -e "xxx\nxxx"
		04. sed 'a/i xxx\nxxx\nxxx' filename
	- 批量重命名的专业命令：rename
		rename	.txt							 .jpg 					odlboy*.txt
		命令	文件名称需要修改的部分的信息	文件修改成的部分的信息	针对的文件信息
	- cat | sed -i 针对的文件是标准输出，而不是源文件
	- 使用后项引用前项时可以使用&符号表示前面匹配的内容
		& --- 表示前面整行的内容
		
# 课程内容
	
# 练习
	- 批量修改文件的拓展名称，oldboy.txt -> oldboyxx.jpg
	find oldboy/ -type f -name "oldboy*.txt"| sed -r 's#(.*)\.txt#mv \1\.txt \1\.gpg#'
	
	ls oldboy*.txt | sed -r 's#(.*)txt#mv & \1jpg#g'|bash
		& 将前面匹配信息信息表示
	- 总结正则
	- 总结sed
	- 总结 find tar date
	
# 拓展