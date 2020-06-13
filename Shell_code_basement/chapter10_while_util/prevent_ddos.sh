#!/bin/bash
#Function: check ddos and close these connections by network connet status(ESTABLISHED)
# netstat -tunp|awk 'NR>2{print}' > /tmp/netstat.log # get connect ip
# grep "ESTABLISHED" /tmp/netstat.log | awk -F"[ :]+" '{print $(NF-5)}'|sort|uniq -c|sort -rn -k1|head -5
# iptables -I INPUT -s 121.204.108.160 -j DROP
netstat_file=/tmp/netstat.log
netstat -tunp|awk 'NR>2{print}' > $netstat_file # netstat.log
file=$netstat_file

function usage(){
	echo $"USAGE: $0 xxx.log"
	exit 1
}
ip_count(){
	grep "ESTABLISHED" $file | awk -F"[ :]+" '{print $(NF-5)}'|sort|uniq -c|sort -rn -k1|head -5 > /tmp/tmp.log
}

iptables_set(){
	local ip=$1
	if [ `iptables -L -n | grep "$ip"|wc -l` -lt 1 ];then
		iptables -I INPUT -s $ip -j DROP
		echo "$line is dropped" >> /tmp/droplist_$(date +%F).log
	fi
}
function main(){
	if ! expr "$file" : ".*\.log" &> /dev/null;then
		usage
	fi
	
	while true
	do
		ip_count
		while read line
		do
			ip=`echo $line|awk '{print $2}'`
			count=`echo $line|awk '{print $1}'`
			if [ $count -gt 3 ];then
				iptables_set $ip
			fi
		done</tmp/tmp.log
		sleep 180
	done
}
main

