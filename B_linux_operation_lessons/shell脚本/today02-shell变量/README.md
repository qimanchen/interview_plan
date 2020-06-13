# 脚本变量
	1. shell脚本一些特殊位置变量
		$0 -- 脚本的名称 -- 给用户提示
			basename -- 仅获取文件的名称
		$n -- 脚本执行时第n个参数
			cat test.sh {a..z}
			$9以后要使用${10}表示
		$# -- 传输参数的个数 -- 控制脚本的传参个数
			[ $# -ne 2 ] && echo "请输入两个参数" && exit 1
		$* -- 获取脚本所有的参数 不加引号和$@相同，加上引号，则把参数视为一个参数$1$2$3
		$@ -- 获取脚本的所有的参数，不加双引号与$*相同，加上引号，则把参数视为一个$1 $2 $3
			$*和$@在脚本中一样，但是for循环中一样
				-- 加上双引号，"$*" 看成一个字符串
					"$@" 看成每个参数
			set -- "I am" lizhenya teacher -- 测试传参
		$? -- 获取上一条命令的返回结果，0 -- 成功 非0 -- 失败
			exit 设置错误的返回值
		$$ -- 获取脚本的PID
			-- 用于杀死pid
			kill -9 'cat tmp.pid'
		$! -- 获取上一个在后台运行脚本的PID，调试使用
		$_ 获取命令行后的最后一个参数 - 相当于esc .
	2. 变量中字符串的删除和替换
		url=www.sina.com.cn
		echo ${url#*.} -- 从前往后删除sina.com.cn -- 双#表示贪婪匹配
		echo ${url%.*} -- 从后往前删除www.sina.com
		echo ${url/sina/oldboy} 只替换第一个www.oldboy.com.cn
			echo ${url//sina/oldboy} 全部替换
		read -p "注释" argu
	3. 数值运算
		1） expr -- 只支持整数运算
			expr 1 + 1 注意要用空格空开
			expr 1 \* 10 
		2） echo $((10+-*/10)) -- 只支持整数运算，运算效率是最高的
		3） $[] 只支持整数运算
			echo $[10+10]
		4) bc 整数运算 小数运算
			echo 10.5+10 | bc
		5) awk python 整数小数
			awk 'BEGIN{print 1+1}'
			python -c 
		判断输入的是否是整数
			read -p "请输入一个数字" num
			expr 1 + $num &> /dev/null -- 判断是否是整数
			[ $? -ne 0 ] && echo "请输入整数" && exit 1
		做一个计算器：加减乘除 用三种传参的方式
		- 遇到传入*参数出现错误
			[root@m01 shell]# bash caculator.sh 12 33 *
			caculator.sh: line 4: 12 caculator.sh 33: syntax error: invalid arithmetic operator (error token is ".sh 33")
		tr 
			- 原因：由于*为通配符的一种，传入运算符号时，应该使用 \*
	4. 条件表达式
		1）文件测试
			test -e 等效于 [ -e ]
			-e 存起是否为真
			-f 是否为文件
			-d 是否问目录 是否存在
			-x 是否可执行
			-r 可读
			-w 可写
		案例
			-d
				[ -d /backup ] && echo ok || /backup
			-f
				[ -f /etc/test.txt ] && echo ok || echo error
			/etc/init.d/functions
				[ -f /etc/init.d/functions ] && . /etc/init.d/functions
				action "Nginx start is " /bin/true
		2）数值比较
			语法格式 [ 数值1 比较符 数值2]
			- 比较符号
				-eq 等于
				-ne 不等于
				-gt 大于
				-ge 大于等于
				-lt 小于
				-le 小于等于
			[[]] -- 双中括号使用>等数学符号
		- 统计磁盘使用率，如果磁盘大于80%则发邮件
			NF -- 总列数
			disk_using=$(df -h | awk 'NR==2{print $4}')
			[ ${disk_using%\%} -gt 5 ] && echo error || echo ok
		- 统计内存，超过5%告警
		- 负载，超过警告
			uptime | awk '{print $(NF-2)}'
			ab -n 20000 -c 20000 http://127.0.0.1/index.html
		3）多整数比较
			-a and
			-o or
			在双重中括号中使用&& ||
		4）字符串比较
			字符串比较需加双引号
			/etc/profile -- ~/.bashrc_profile -- ~/.bashrc -- /etc/bashrc
			-z 字符长度为0，则为正，判断是否为空
			-n 字符长度不为0，则为正
			
			- 判断是否为整数， expr 1 + 变量
		5）正则比较 -- 必须使用两个中括号
			[[ $USER =~ ^r ]]
			[[ ! $USER =~ ^r ]] -- 取反
			[[ $test =~ ^[0-9]+$ ]] -- 判断是否是整数
		-- 添加默认路由
			route add default gw 192.168.90.1
			ip route add default via 10.0.0.254
			route del default gw 192.168.90.1
		-- 网卡添加多个IP
			ip addr add 10.0.0.2/24 dev eth1
		-- 查看策略 -- vpn -- 连不上路由
			/etc/iproute2/rt_tables
				200 test 
				- 添加策略
				ip route add 0/0 via 10.0.0.254 table test
		- 添加一个表 给这个表添加东西
			ip rule add from  10.0.0.1 table test -- 走test表
				10.0.0.1 公司的公网IP
	# 如何统计服务器昨天，一整天的数据 发送给领导
		curl 127.0.0.1
		awk '{print $1}' /var/log/nginx/access.log|uniq -c > /html/www/$(date +%F -d "-1days")
		curl 127.0.0.1/$(date +%F "-1days")
		cat /tmp/test_data.txt | awk '{print $1}'|xargs|tr " " "+"|bc -- 多个统计数据相加
	# 查看对应的系统信息
		# 显示系统信息，hostnamectl
		开机查看相应的信息
		
	5. for循环
		for i in [取值列表] 数字 字符串 命令结果（$()）序列
		do
			循环体
		done
		# 批量ping测试
		# 批量创建10个用户
			1. 前缀
	6. if判断
		if [ ];then
		
		elif []; then
		
		fi
		# 判断数据
		# 判断大了，小了
			随机数	$((RANDOM%100+1)) -- 1-99随机
			let i++ -- 循环一次自增1
		# 按照不同centos版本，安装不同的yum源
			os=cat /etc/redhat-release|awk '{print $(NF-1)}' # 注意7和6的版本不一样
			if [ ${os%%.} -eq 7 ];then
				which wget &> /dev/null
				[ $? -ne 0 ]&& yum -y install wget
				mv .. #备份
				wget .. #拉取源
			elif [ $os -eq 6 ];then
				..
			fi
	7. 菜单的使用方法
		1）echo方式
			echo "1"
			echo "2"
			echo "3"
		2)
			cat <<EOF -- 这个要贴着开头 cat<<-EOF
				1. ..
				2. ..
				3. ..
			EOF  -- 这个要贴着开头
			
		# 安装不同版本的PHP
	8. case语句
		结构
			变量 == 名称
			case 变量 in
				模式1)
					;;
				*)
					;;
			esac
		# 批量删除用户 if判断
			1. 删除用户的前缀 read
			2. 删除用户的数量 read
				read -p ”你是否要删除该用户？[y|N..]" te
				case $te in
					*)
						....
						;;
				esac
		# case 要求使用菜单 显示
			1.help帮助 打印菜单
			2. 显示内存使用
			3. 显示磁盘使用
			4. 显示系统负载
			5. 显示登陆用户
			6. 查看IP
			7. 查看Linux-version
		# nginx 脚本启动案例
			which nginx