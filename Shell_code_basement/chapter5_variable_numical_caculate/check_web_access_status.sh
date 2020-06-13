#!/bin/bash
#Function: copy from oldboy book
# check access web stations status
# qiman 2020-06-03

# define check function
check_url(){
	# define some variables for access status
	timeout=5
	fails=0
	success=0
	
	# Continuous monitoring
	while true
	do
		wget --timeout=$timeout --tries=1 http://www.baidu.com -q -o /dev/null
		
		# update access status info
		if [ $? -ne 0 ];then
			let fails+=1
		else
			let success+=1
		fi
		
		if [ $success -ge 1 ];then
			echo "success"
			exit 0
		fi
		
		if [ $fails -ge 2 ];then
			Critical="sys is down."
			echo $Critical|tee|mail -s "$Critical" 1033178199@qq.com
			exit 2
		fi
	done
}
# exec function
check_url