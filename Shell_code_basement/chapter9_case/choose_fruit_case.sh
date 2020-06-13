#!/bin/bash
#Functions: choose fruit from menu

RED_COLOR='\e[1;31m'
GREEN_COLOR='\e[1;32m'
YELLO_COLOR='\e[1;33m'
BLUE_COLOR='\e[1;34m'
RES='\E[0m'

function usage(){
	echo "USAGE: $0 {1|2|3|4}"
}

function menu(){
	cat<<EOF
			1. apple
			2. pear
			3. banana
EOF
}

function chose(){
	read -p "Please input your choice: " fruit
	case "$fruit" in
		1)
			echo -e "${RED_COLOR}apple${RES}"
			;;
		2)
			echo -e "${GREEN_COLOR}pear${RES}"
			;;
		3)
			echo -e "${YELLO_COLOR}banana${RES}"
			;;
		*)
			usage
	esac
}

function main(){
	menu
	chose
}
main