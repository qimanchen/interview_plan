#/bin/bash
### backup system special data
### code by qiman in 20200420

Backup_dir="/backup"
IP_info=$(hostname -i)
Backup_server_IP="172.16.1.41"
Backup_server_module="backup"
Backup_server_user="rsync_backup"

cd /
tar_files="./var/spool/cron/root ./etc/rc.local ./server/scripts ./etc/sysconfig/iptables"
avali_tar_files=""
for file in $tar_files; do

        if [ -e ${file} ]; then
                avali_tar_files="${avali_tar_files} ${file}"
        fi
done
# create backup dir
if [ ! -e ${Backup_dir}/${IP_info}/ ]; then
        mkdir $Backup_dir/$IP_info -p
fi

# tar backup data
tar zchf $Backup_dir/$IP_info/system_backup_$(date +%F_week%w -d "-1day").tar.gz $avali_tar_files
tar zchf $Backup_dir/$IP_info/www_backup_$(date +%F_week%w -d -1day).tar.gz ./var/html/www
tar zchf $Backup_dir/$IP_info/www_log_backup_$(date +%F_week%w -d -1day).tar.gz ./app/logs

# del 7 day ago data
Seven_days_ago_file=$(find $Backup_dir -type f -mtime +7)
if [ ! -z ${Seven_days_ago_file}  ]; then
        rm ${Seven_days_ago_file} -f &> /dev/null
fi
# find $Backup_dir -type f -mtime +7 | xargs rm

# create finger file
find $Backup_dir -type f -mtime -1 ! -name "finger*"| xargs md5sum > $Backup_dir/$IP_info/finger.txt

# backup push data info
rsync -az $Backup_dir/  $Backup_server_user@$Backup_server_IP::$Backup_server_module --password-file=/etc/rsync.password
