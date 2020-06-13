#!/bin/bash
#Function: Calculator
menu(){
cat << EOF
			两数运算器菜单
				1. help
				2. 加法运算
				3. 乘法运算
				4. 除法运算
				5. 减法运算
				6. 退出
EOF
}
menu
while true
do
	read -p "请确认要进行的操作: " op
	case $op in 
		1)
			menu
			;;
		2)
			echo "您将要进行加法运算."
			read -p "请输入要运算的两个整数: " ob1 ob2
			echo "ob1+ob2=$(($ob1+$ob2))"
			;;
		3)
			echo "您将要进行乘法运算."
			read -p "请输入要运算的两个整数: " ob1 ob2
			echo "ob1*ob2=$(($ob1*$ob2))"
			;;
		4)
			echo "您将要进行除法运算."
			read -p "请输入要运算的两个整数: " ob1 ob2
			echo "ob1/ob2=$(($ob1/$ob2))"
			;;
		5)
			echo "您将要进行减法运算."
			read -p "请输入要运算的两个整数: " ob1 ob2
			echo "ob1-ob2=$(($ob1-$ob2))"
			;;
		6)
			exit
			;;
		*)
			;;
	esac
done