#!/bin/bash
#Function: monitor memory of the server
WARN_VALUE=100
FREE=$( free -h | awk -F"[ ]+" 'NR==2{print $4}')
CHARS="Current memory is $FREE."

if [ ${FREE%M} -lt $WARN_VALUE ];then
	echo $CHARS|tee /tmp/message.txt
	mail -s "`date +%F-%T`$CHARS" test@qq.com < /tmp/message.txt
fi

# /3 * * * * /bin/bash /server/scripts/shell/memory_monitor.sh &> /dev/null