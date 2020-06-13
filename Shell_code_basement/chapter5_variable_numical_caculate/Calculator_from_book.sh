#!/bin/bash
#Function: Calculator2, add, subtract, multiply and divide 2020-06-03

# 打印输入错误信息
print_usage(){
	printf "Please enter an integer\n"
	exit 1
}

# first number
read -p "Please input first number: " first_num
# determine the number is an integer.
if [ -n "`echo $first_num|sed 's/[0-9]//g'`" ];then
	print_usage
fi

# input operators
read -p "Please input the operators: " operators
# determine operators

# if [ "${operators}" != "+" ] and [ "${operators}" != "-" ] and [ "${operators}" != "*" ] and  [ "${operators}" != "/" ];then
#error
# Please input the operators: *
# calculator2.sh: line 20: [: too many arguments
# solved -- and replace by &&

if [ "${operators}" != "+" -a "${operators}" != "-" -a "${operators}" != "*" -a "${operators}" != "/" ];then
	echo "Please use {+|-|*|/}"
	exit 2
fi

# second number
read -p "Please input second number: " second_num
# determine the number is an integer.
if [ -n "`echo $second_num|sed 's/[0-9]//g'`" ];then
	print_usage
fi

# output results
echo "${first_num}${operators}${second_num}=$((${first_num}${operators}${second_num}))"
