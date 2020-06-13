#!/bin/bash
#Function: web access status
url_list=(
http://blog.oldboyedu.com
http://blog.etiantian.org
http://oldboy.blog.51cto.com
http://10.0.0.7
)
usage(){
	echo $"USAGE $0 url."
	exit 1
}

main(){
	[ $# -ne 1 ] && {
		echo $"USAGE $0 url."
		exit 1
	}
	while true
	do
		# 
		if [ `curl -o /dev/null --connect-timeout 5 -s -w "%{http_code}" $1|egrep -w "200|301|302"|wc -l` -ne 1 ];then
			action "$1 is error." /bin/false
			# echo "$1 is error." | mails -s "$1 is error." test@qq.com
		else
			action "$1 is ok" /bin/true
		fi
		sleep 10
	done
}
main "$@"