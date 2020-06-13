#!/bin/bash
#Function: mysql - database backup
PATH="$PATH"
MYUSER=root
MYPASS=centos
# SOCKET=/data/3306/mysql.sock
MYCMD="mysql -u$MYUSER -p$MYPASS"
DBPATH=/server/backup
MYDUMP="mysqldump -u$MYUSER -p$MYPASS"
# backup database
[ ! -d "$DBPATH" ]&& mkdir -p $DBPATH
for dbname in `$MYCMD -e "show databases;" | sed '1d'|egrep -v "mysql|schema"`
do
	if [ ! -e $DBPATH/${dbname}_$(date +%F).sql.gz ];then

		$MYDUMP $dbname|gzip > $DBPATH/${dbname}_$(date +%F).sql.gz
	else
		echo "$DBPATH/${dbname}_$(date +%F).sql.gz is exists."
	fi

done