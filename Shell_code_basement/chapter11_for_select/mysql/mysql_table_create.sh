#!/bin/bash
#Function: mysql - create table in database
PATH="$PATH"
MYUSER=root
MYPASS=centos
# SOCKET=/data/3306/mysql.sock
MYCMD="mysql -u$MYUSER -p$MYPASS"
for dbname in oldboy oldgirl xiaoting bingbing
do
	$MYCMD -e "use $dbname;create table test(id int,name varchar(16));insert into test values(1,'testdata');"
done