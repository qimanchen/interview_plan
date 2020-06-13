#!/bin/bash
# check opt
# set env
export PATH=$PATH:/bin:/sbin:/usr/sbin

# Require root to run this script
if [ "$UID" != "0" ];then
	echo "Please run this script by root."
	exit 1
fi

# Source function library.
. /etc/init.d/functions

function check_yum(){
    Base=/etc/yum.repos.d/CentOS-Base.repo
    if [ `grep aliyun $Base|wc -l` -ge 1 ];then
        action "$Base config" /bin/true
    else
        action "$Base config" /bin/false
    fi
}
function check_selinux(){
    config=/etc/selinux/config
    if [ `grep "SELINUX=disabled" $config|wc -l ` -ge 1 ];then
        action "$config config" /bin/true
    else
        action "$config config" /bin/false
    fi
}
function check_service(){
    export LANG=en
    if [ `chkconfig|grep 3:on|egrep "crond|sshd|network|rsyslog|sysstat"|wc -l` -eq 5 ]
      then
        action "sys service init" /bin/true
    else
        action "sys service init" /bin/false
    fi
}
function check_open_file(){
    limits=/etc/security/limits.conf
    if [ `grep 65535 $limits|wc -l` -eq 1 ]
      then
        action "$limits" /bin/true
    else
        action "$limits" /bin/false
    fi
}
main(){
    check_yum
    check_selinux
    check_service
    check_open_file
}
main