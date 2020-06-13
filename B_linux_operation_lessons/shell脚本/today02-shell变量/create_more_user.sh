#!/bin/bash
read -p "please input prefix: " pre
[ -z $pre ] && echo "prefix not be Null or length is zero" && exit 1
read -p "please input number of users: " num
expr 1 + $num &> /dev/null
[ $? -ne 0 ] && echo "please input a intger." && exit 2
# start create each user
for i in $(seq $num)
do
	id "$pre$i" &> /dev/null && userdel -r "$pre$i" &> /dev/null
	useradd -M "$pre$i" && echo "12345"|passwd --stdin $pre$i &> /dev/null
	id "$pre$i" &> /dev/null && echo "$pre$i create successful" || echo "$pre$i creatre failed"
done
