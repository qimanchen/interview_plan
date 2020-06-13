#!/bin/bash
#Function: show select function
# 采用列表
# select name in oldboy oldgirl tingting

# 采用数组
array=(oldboy oldgirl tingting)
select name in "${array[@]}"
do
	echo $name
done