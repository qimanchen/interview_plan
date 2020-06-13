#!/bin/bash
#Function: check the file extension is or not meeting the requirements
if `expr "$1" : ".*\.pub" &> /dev/null`;then
	echo "you are using $1"
else
	echo "Please use *.pub file."
fi