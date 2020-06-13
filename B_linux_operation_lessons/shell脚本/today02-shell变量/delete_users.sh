#!bin/bash
#Function:批量删除用户
read -p "please input username prefix: " pre
read -p "please input user number: " num
for i in `seq $num`
do
	echo $pre$i
done
read -p "确定是否删除以上用户吗?[y|Y|yes|n|N|no] " re
for i in `seq $num`
do
	user=$pre$i
case $re in 
	y|Y|yes)
		id $user &>/dev/null 
		if [ $? -eq 0 ]; then
			userdel -r $user
			[ $? -eq 0 ] && echo "$user del is ok"
		else
			echo "id: $user: no such user"
		fi
		;;
	n|N|no)
		echo "不删除"
		exit
esac
done
