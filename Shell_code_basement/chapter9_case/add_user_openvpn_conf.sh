#!/bin/bash
#Function: add user for /etc/openvpn_authfile.conf
. /etc/init.d/functions
FILE_PATH="/etc/openvpn_authfile.conf"

function usage(){
	cat <<EOF
		USAGE: `basename $0` {-add|-del|-search} username
EOF
}



function search_user(){
	if grep "^$1$" ${FILE_PATH} &> /dev/null; then
		action $"vpnuser, $1 is exist" /bin/true
		return 1
	else
		action $"vpnuser, $1 is not exist" /bin/false
		return 2
	fi
}

function add_user(){
	chattr -i ${FILE_PATH}
	/bin/cp ${FILE_PATH} ${FILE_PATH}.$(date +%F%T)
	echo "$1" >> ${FILE_PATH}
	[ $? -eq 0 ] && action $"Add $1" /bin/true
	chattr +i ${FILE_PATH}
}

function del_user(){
	chattr -i ${FILE_PATH}
	/bin/cp ${FILE_PATH} ${FILE_PATH}.$(date +%F%T)
	sed -i "/^${1}$/d" ${FILE_PATH}
	[ $? -eq 0 ] && action $"Del $1" /bin/true
	chattr +i ${FILE_PATH}	
}

function actions(){
	case "${1}" in
		"-a"|"-add")
			search_user $2
			[ $? -eq 2 ] && add_user $2
			;;
		"-d"|"-del")
			search_user $2
			[ $? -eq 1 ] && del_user $2
			;;
		"-s"|"-search")
			search_user $2
			;;
		*)
			usage
	esac
}

function main(){
	[ ! -f ${FILE_PATH} ] && touch $FILE_PATH
	# judge run user
	if [ $UID -ne 0 ]; then
		echo "You are NOT SUPPER USER, please call root!"
		exit 1
	fi

	# judge arg numbers.
	if [ $# -ne 2 ]; then
		usage
		exit 2
	fi
	actions "$@"
}

main "$@"
