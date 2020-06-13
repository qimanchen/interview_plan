#!/bin/bash
#Function: show word color
BLACK_COLOR='\e[30;1m'
RED_COLOR='\e[31;1m'
GREEN_COLOR='\e[32;1m'
YELLOW_COLOR='\e[33;1m'
BLUE_COLOR='\e[34;1m'
PINK_COLOR='\e[35;1m'
WHITE_COLOR='\e[37;1m'
RES='\e[0m'

function usage(){
	echo "Usage $0 content {red|yellow|blue|green}"
	exit 1
}

function add_color(){
	case "$2" in
		"red")
			echo "${RED_COLOR}$1${RES}"
			;;
		"yellow")
			echo "${YELLOW_COLOR}$1${RES}"
			;;
		"blue")
			echo "${BLUE_COLOR}$1${RES}"
			;;
		"green")
			echo "${GREEN_COLOR}$1${RES}"
			;;
		*)
			usage
	esac
}

function main(){
	[ $# -ne 2 ] &&{
		usage
	}
	add_color $1 $2
}
main $*
