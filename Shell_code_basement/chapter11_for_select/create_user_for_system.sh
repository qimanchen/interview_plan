#!/bin/bash
#Function: create system account
. /etc/init.d/functions

pre_username="oldboy"
passfile="/tmp/user_passwd.log"

for username in ${pre_username}{01..5}
do
	# useradd -s /sbin/nologin -M $username
	# echo -en "$username:\t" >>/tmp/new_user_password
	# echo $RANDOM| tee >>/tmp/new_user_password|md5sum |passwd --stdin $username
	
	# version 1
	# pass="`echo "test$RANDOM"|md5sum| cut -c3-11`"
	# useradd $username &> /dev/null &&\
	# echo "$pass" | passwd --stdin $username &> /dev/null &&\
	# echo -e "user:$username\tpasswd:$pass" >> $passfile
	
	# if [ $? -eq 0 ];then
		# action "$username is ok" /bin/true
	# else
		# action "$username is fail" /bin/false
	# fi
	
	#version 2
	pass="`echo "test$RANDOM" |md5sum|cut -c3-11`"
	useradd $username &> /dev/null &&\
	echo -e "${username}:$pass">>$passfile
	if [ $? -eq 0 ];then
		action "$username is ok" /bin/true
	else
		action "username is failed" /bin/false
	fi
done

echo ---------------
chpasswd < $passfile
cat $passfile && > $passfile
