#!/bin/bash
# 多线程ping测试
IP_HEAD="10.0.2."
for i in $(seq 100)
do
	{
	ping -c1 -W1 "$IP_HEAD$i" &>/dev/null
	[ $? -eq 0 ] && echo "$IP_HEAD$i可以ping通"
	}&
done
wait # 等待子进程完成
echo "在线取IP完成"

