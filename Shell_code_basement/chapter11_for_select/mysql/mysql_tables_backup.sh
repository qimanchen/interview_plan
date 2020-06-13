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
	[ ! -d $DBPATH/${dbname}_$(date +%F) ] && mkdir $DBPATH/${dbname}_$(date +%F) -p
	for table in `$MYCMD -e "show tables from $dbname;"|sed '1d'`
	do
		$MYDUMP $dbname $table|gzip > $DBPATH/${dbname}_$(date +%F)/${dbname}_${table}.sql.gz
	done

done