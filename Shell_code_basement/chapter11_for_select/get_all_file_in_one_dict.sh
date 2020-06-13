#!/bin/bash
#Function: get all dict and files in one special dict
dict=/test
for filename in `ls -R‘
do
	echo $filename
done