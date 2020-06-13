#!/bin/bash
#Function: compare two integer
info() {
	echo "Please input two 'num' again."
	exit 2
}
# [ "$#" != 2 ] &&{
	# echo "输入参数个数错误."
	# exit 1
# }

[ -z "$1" ] || [ -z "$2" ] &&{
	info
}

num1=$1
expr $num1 + 1 &> /dev/null
# [ $? -ne 0 ] &&{
	# info
# }
RETVAL1=$?
num2=$2
expr $num2 + 1 &> /dev/null
# [ $? -ne 0 ] &&{
	# info
# }
RETVAL2=$?
[ $RETVAL1 -eq 0 -a $RETVAL2 -eq 0 ] ||{
	info
}
[ $num1 -gt $num2 ] && {
	echo "$num1 > $num2"
	exit 0
}

[ $num1 -lt $num2 ] && {
	echo "$num1 < $num2"
	exit 0
}
echo "$num1 == $num2"