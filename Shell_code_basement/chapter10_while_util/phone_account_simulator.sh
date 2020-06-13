#!/bin/bash
#Function: simulator for phone call count

START_FEE=10*1000
MSG_FEE=15
INFO_FEE=15

function is_num(){
	expr $1 + 1 &> /dev/null
	[ $? -ne 0 ] && {
		return 1
	}
	return 0
}
while [ $sum -ge $error_m ]
do
	echo "messages"
	((sum=sum-i))
done
echo "the money is not enough: $sum"