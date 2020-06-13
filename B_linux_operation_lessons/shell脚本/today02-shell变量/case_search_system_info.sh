#!/bin/bash
#显示系统信息
menu(){
cat << EOF
				1. help帮助
				2. 显示内存使用
				3. 显示磁盘使用
				4. 显示系统负载
				5. 显示登陆用户
				6. 查看IP地址
				7. 查看Linux-version
				8. 退出系统
EOF
}
menu
while true
do
	read -p "请输入要查看的系统信息编号: " num
	case $num in
		1)
			menu
			;;
		2)
			free -h
			;;
		3)
			df -h
			;;
		4)
			uptime
			;;
		5)
			w
			;;
		6)
			ip a
			;;
		7)
			cat /etc/redhat-release
			;;
		8)
			exit
	esac
done