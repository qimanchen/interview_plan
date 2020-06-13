#!/bin/bash
#Author:chen qiman
#Mail:1033178199@qq.com
#Time:2020-06-07 23:59:41
#Name:trap_clear.sh
#Version:V1.0
#Description: clear file when exec ctrl+c.

trap "find /tmp -type f -name 'oldboy_*'|xargs rm -f && exit" INT

while true
do
    touch /tmp/oldboy_$(date +%F-%H-%M-%S)
    sleep 3
    ls -l /tmp/oldboy*
done
