#/bin/bash

Backup_dir="/backup"
IP_info=$(hostname -i)
# hostname -I 所有地址
# hostname -i 内网地址
# sh -x *.sh 测试
# create backup dir
mkdir $Backup_dir/$IP_info -p
# tar backup data
cd /
tar zchf $Backup_dir/$IP_info/system_backup_$(date +%F_week%w -d "-1day").tar.gz ./var/spool/cron/root ./etc/rc.local ./server/scripts ./etc/sysconfig/iptables
# del 7 day ago data
find /backup -type f -mtime +7 | xargs rm
# create finger file
find /backup/ -type f -mtime -1 ! -name "finger"| xargs md5sum > $Backup_dir/$IP_info/finger.txt
# backup push data info
rsync -avz /backup/ rsync_backup@$IP_info::backup --password-file=/etc/rsync.password