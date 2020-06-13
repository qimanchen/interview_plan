#!/bin/bash
#Function: 设置菜单默认提示符
PS3="please select a num from menu: "

select name in oldboy oldgirl tingting
do 
	echo -e "I guess you selected the menu is:\n $REPLY) $name"
	# $REPLY为菜单项对应数字
	
done
