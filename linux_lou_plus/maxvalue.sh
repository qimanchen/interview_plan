#!/bin/bash

max(){
	while test $1
	do
		if test $maxvalue;then
			if test $1 -gt $maxvalue;then
				maxvalue=$1
			fi
		else
			maxvalue=$1
		fi
		shift
	done
	return $maxvalue
}

max $*
echo "max value is $maxvalue"

# bash maxvalue.sh 1 2 3 8 4
# max value is 8