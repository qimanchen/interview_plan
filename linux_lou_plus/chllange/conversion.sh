#!/bin/bash

if [ $# -lt 1 -o $# -gt 1 ];then
    echo "param is error!"
    exit 1
fi

K=1024
M=$((K*1024))
G=$((M*1024))

if [ $1 -gt $G ];then
    result=$(echo "${1}/${G}"|bc|awk 'BEGIN{FS="."}{print $1}')
    echo "$result GB"
elif [ $1 -ge $M ];then
    result=$(echo "${1}/${M}"|bc|awk 'BEGIN{FS="."}{print $1}')
    echo "$result MB"
elif [ $1 -ge $K ];then
    result=$(echo "${1}/${K}"|bc|awk 'BEGIN{FS="."}{print $1}')
    echo "$result KB"
else
    echo "$1 B"
fi
