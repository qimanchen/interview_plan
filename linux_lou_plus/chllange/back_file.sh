#!/bin/bash

CONFIG=files-to-backup.txt
ARCHIVE=archive-$(date +%Y%m%d).tar.gz

cd ~

if ! [ -f $CONFIG ]
then
	echo "$CONFIG does not exist."
	exit 1
fi

while read -r file
do
	if [ -f $files -o -d $file ]
	then
		file="$files $file"
	else
		echo "$file does not exist, it will be skipped."
	fi
done < "$CONFIG"

echo "Starting archive..."
tar -czf $ARCHIVE $files
echo "Archive completed"