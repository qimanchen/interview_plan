#!/bin/bash
#Function: mysql backup
PATH="$PATH"
MYUSER=root
MYPASS=centos
# SOCKET=/data/3306/mysql.sock
MYCMD="mysql -u$MYUSER -p$MYPASS"


# create database
for dbname in oldboy oldgirl xiaoting bingbing
do
	$MYCMD -e "create database $dbname"
done

