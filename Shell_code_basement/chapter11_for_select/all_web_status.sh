#!/bin/bash
#Function: check web service
path=/server/scripts
MAIL_GROUP="1111@qq.com 2222@qq.com"
PAGER_GROUP="1877091.... 1891171...."
LOG_FILE="/tmp/web_check.log"

[ ! -d "$path" ] && mkdir -p $path

function url_list(){
	cat > $path/domain.list<<EOF
	http://blog.oldboyedu.com
	http://oldboy.blog.51.ctl.com
	http://10.0.0.7
	http://www.baidu.com
EOF
}

function check_url(){
	FAILCOUNT=0
	for ((i=1;i<=3;i++))
	do
		wget -T 5 --tires=1 --spider $1 &> /dev/null
		if [ $? -ne 0 ];then
			let FAILCOUNT+=1
		else
			break
		fi
	done
	return $FAILCOUNT
}

function Mail(){
	local SUBJECT_CONTENT=$1
	for MAIL_USERT in `echo $MAIL_GROUP`
	do
		mail -s "$SUBJECT_CONTENT" $MAIL_USERT < $LOG_FILE
	done
}

function pager(){
	for PAGER_USER in `echo $PAGER_GROUP`
	do
		TITLE=$1
		CONTACT=$PAGER_USER
		HTTPGW=http://oldboy.sms.cn/smsproxy/sendsms.action
		
		# send_message method
		curl -d cdkey=5ADF-EFA -d password=OLDBOY -d phone=$CONTACT -d message="$TITLE[$2]" $HTTPGW
		
	done
}

function send_msg(){
	if [ $1 -ge 3 ]; then
		RETVAL=1
		NOW_TIME=`date +"%F %T"`
		SUBJECT_CONTENT="http://$2 is error, ${NOW_TIME}."
		echo -e "$SUBJECT_CONTENT" | tee $LOG_FILE
		Mail $SUBJECT_CONTENT
		pager $SUBJECT_CONTENT $NOW_TIME
	else
		echo "http://$2 is ok"
		RETVAL=0
	fi
	return $RETVAL
}

function main(){
	url_list
	for url in `cat $path/domain.list`
	do
		check_url $url
		send_msg $? $url
	done
}

main