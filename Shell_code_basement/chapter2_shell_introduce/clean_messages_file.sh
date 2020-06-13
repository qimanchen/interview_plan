#!/bash/bash
# Function: This scripts functions is for clear /var/log/messages
# Ps: this scripts is copy from the book.

LOG_DIR="/var/log"
ROOT_UID=0

if [ "${UID}" -ne "${ROOT_UID}" ]; then
	echo "Must be ROOT to run this script."
	exit 1
fi

cd $LOG_DIR || {
	echo "Cannot change to necessary directory."
	exit 1
}

cat /dev/null > messages && {
	echo "Logs cleaned up."
	exit 0
}

echo "Logs cleaned up fail."
exit 1