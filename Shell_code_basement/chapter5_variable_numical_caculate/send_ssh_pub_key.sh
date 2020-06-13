#!/bin/bash
#Function: send ssh key by command ssh-copy-id
if [ "-i" == "$1" ]; then
	shift
	# check if we have 2 paramenters left, if so the first is the new ID file
	if [ -n "$2" ]; then
		if `expr "$1" : ".*\.pub" > /dev/null`;then
			# expr
			# STRING : REGEXP
			# anchored pattern match of REGEXP in STRING
			ID_FILE="$1"
		else
			ID_FILE="$1.pub"
		fi
		shift
	fi
fi