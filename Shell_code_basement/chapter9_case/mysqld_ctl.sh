#!/bin/bash
#Function: manager nginx in centos6

start_path=/data/3306/my.cnf
stop_path=/data/3306/mysql.sock
RETVAL=0
. /etc/init.d/functions

start() {
	if [ `netstat -tunlp|grep 3306|wc -l` -eq 0 ]; then
		mysqld_safe --defaults-file=$start_path &
		RETVAL=$?
		if [ $RETVAL -eq 0 ]; then
			action "mysql is started" /bin/true
			return $RETVAL
		else
			action "mysql is started" /bin/false
			return $RETVAL
		fi
	else
		echo "mysql is running"
		return 0
	fi
}
stop(){
	if [ `netstat -tunlp|grep 3306|wc -l` -eq 1 ]; then
		mysqladmin -uroot -pcentos -S $stop_path shutdown
		RETVAL=$?
		if [ $RETVAL -eq 0 ];then
			action "mysql is stopped" /bin/true
			return $RETVAL
		else
			action "mysql is stopped" /bin/false
		fi
	else
		echo "mysql is no running."
		return $RETVAL
	fi
}

case "$1" in
	start)
		start
		RETVAL=$?
		;;
	stop)
		stop
		RETVAL=$?
		;;
	restart)
		stop
		sleep 1
		start
		RETVAL=$?
		;;
	*)
		echo $"Usage: $0 {start|stop|restart}"
		exit 1
esac

exit $RETVAL