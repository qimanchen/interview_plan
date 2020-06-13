#!/bin/bash
#Function: mysql monitor
if [ `netstat -tunlp|grep 3306|wc -l` -eq 1 ];then
	echo "MySQL is Running."
else
	echo "MySQL is Stopped."
	systemctl start mysql
fi