#!/bin/bash
#Function: test operation calculation
# check the number of input is two
[ $# -ne 2 ] && echo "Please input two integer && exit 1"
expr $1 + 2 &> /dev/null
# [ $? -ne 0 ] && echo "first number($1) DON'T integer, Please input integer." && exit 2
[ $? -ne 0 ] &&{
	echo "first number($1) DON'T integer, Please input integer."
	exit 2
}
expr $2 + 2 &> /dev/null
[ $? -ne 0 ] && echo "second number($1) DON'T integer, Please input integer." && exit 2
a=$1
b=$2
echo "a-b=$(($a-$b))"
echo "a+b=$(($a+$b))"
echo "a*b=$(($a*$b))"
echo "a/b=$(($a/$b))"
echo "a**b=$(($a**$b))"
echo "a%b=$(($a%$b))"