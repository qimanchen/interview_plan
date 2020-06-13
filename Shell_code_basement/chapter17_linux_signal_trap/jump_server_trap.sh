#!/bin/bash
#用户登录到跳板机上，只允许执行管理员给定的动作，不允许以任何形式终端脚本

#1. ssh秘钥验证（跳板机地址为192.168.33.128)
	# 所有服务器上操作
	# useradd jump
	# echo 123456|passwd --stdin jump
	
	# 跳板机上操作
	# su - jump
	# 生成秘钥
	# ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa &> /dev/null
	# 分发公钥
	# ssh-copy-id -i ~/.ssh/id_dsa.pub 192.168.33.130
	
menu(){
	cat <<EOF
	1)oldboy-192.168.33.129
	2)oldgirl-192.168.33.100
	3)exit
EOF
}

# 利用linux信号，防止用户终端信号在跳板机上操作
trapper(){
	trap ':' INT EXIT TSTP TERM HUP # 屏蔽这些信号
}

# 指定用户在跳板机中可以执行的命令 -- 指定到jump服务中
# echo '[ $UID -ne 0 ] && . /server/scripts/jump.sh' > /etc/profile.d/jump.sh
main(){
	while :
	do
		trapper
		clear
		menu
		read -p "Please input a num: " num
		case "$num" in
			1)
				echo "login in 192.168.33.129."
				ssh 192.168.33.129
				;;
			2)
				echo "login in 192.168.33.130."
				ssh 192.168.33.130
				;;
			110)
				read -p "your birthday: " char
				if [ "$char" == "0926" ];then
					exit
					sleep 3
				fi
				;;
			*)
				echo "select error."
		esac
	done
}