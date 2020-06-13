#!/bin/bash
#Function: deal apache access logs for all data size
# awk
# awk '{sum+=$10}END{print sum/1024}' access_log
sum=0
exec < $1 # parameters $1 redirect to exec

while read line
do
	size=`echo $line |awk '{print $10}'`
	expr $size + 1 &> /dev/null
	if [ $? -ne 0 ]; then
		continue
	fi
	((sum=sum+$size))
done

echo "${1}:total:${sum}bytes=`echo $((${sum}/1024))`KB"