#!/usr/bash

if [ $# -lt 1 ]:
then
	echo "Not param"
	exit 1
fi

SERVICES=$1

# 检查服务是否存在

sudo service $SERVICES status

on=$?

case $on in 
	0)
		echo "is Running"
		;;
	1)
		echo "Error: $SERVICES Not Found"
		;;
	3)
		echo "Restarting"
		sudo service $SERVICES start
		;;
	*)
		echo "Error"
		;;
esac
