#!/bin/bash
#Function: string is number?

echo "by seed"
[ -n "`echo oldboy303|sed 's/[0-9]//g'`" ] && echo char || echo int

echo "vari replace"
[ -z $(echo "${num//[0-9]/}") ] && echo int || echo char

echo "check string that is delete no numbers char length"
[ -n "$num" -a "$num" == "${num//[^0-9]/}" ] && echo "it is num"

echo "using expr"
expr $var + 1 &> /dev/null && {
	echo "error"
	exit 2
}

echo "using =~"
[[ olboy123 =~ ^[0-9]+$ ]] && echo int || echo char

echo "using bc"
echo 123odlboy |bc # this action will execute failed.

