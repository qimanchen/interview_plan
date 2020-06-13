#!/bin/bash
#Function: mysql - create table in database
PATH="$PATH"
MYUSER=root
MYPASS=centos
# SOCKET=/data/3306/mysql.sock
MYCMD="mysql -u$MYUSER -p$MYPASS"
for dbname in oldboy oldgirl xiaoting bingbing
do
	echo "==================${dbname}.test====================="
	$MYCMD -e "use $dbname;select * from ${dbname}.test;"
done