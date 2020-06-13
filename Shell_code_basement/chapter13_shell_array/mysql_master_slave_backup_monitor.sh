#!/bin/bash
###########################################
# this script function is :
# check_mysql_slave_replication_status
# USER        YYYY-MM-DD - ACTION
# oldboy      2009-02-16 - Created
############################################
path=/server/scripts                   #<==定义脚本存放路径，请大家注意这个规范。
MAIL_GROUP="1111@qq.com 2222@qq.com"   #<==邮件列表，以空格隔开。
PAGER_GROUP="18600338340 18911718229"  #<==手机列表，以空格隔开。
LOG_FILE="/tmp/web_check.log"          #<==日志路径。
USER=root                              #<==数据库用户。
PASSWORD=oldboy123                     #<==用户密码。
PORT=3307 #<==端口。
MYSQLCMD="mysql -u$USER -p$PASSWORD -S /data/$PORT/mysql.sock"
                                       #<==登录数据库命令。
error=(1008 1007 1062)                 #<==可以忽略的主从复制错误号。
RETVAL=0
[ ! -d "$path" ] && mkdir -p $path
function JudgeError(){                 #<==定义判断主从复制错误的函数。
    for((i=0;i<${#error[*]};i++))
    do
        if [ "$1" == "${error[$i]}" ]       #<==如果传入的错误号和数组里的元素相匹配，
                                               则执行then后面的命令。
          then
            echo "MySQL slave errorno is $1,auto repairing it."
            $MYSQLCMD -e "stop slave;set global sql_slave_skip_counter=1;start slave;"
                                      #<==自动修复。
        fi
    done
    return $1
}
function CheckDb(){                   #<==定义检查数据库主从复制状态的函数。
    status=($(awk -F ':' '/_Running|Last_Errno|_Behind/{print $NF}' slave.log))
    expr ${status[3]} + 1 &>/dev/null #<==这个是延迟状态值，用于进行是否为数字的判断。
    if [ $? -ne 0 ];then              #<==如果不为数字。
        status[3]=300                 #<==赋值300，当数据库出现复制故障时，延迟
                                              这个状态值有可能是NULL，即非数字。
    fi
    if [ "${status[0]}" == "Yes" -a "${status[1]}" == "Yes" -a ${status[3]} -lt 120 ]
    #<==两个线程都为Yes，并且延迟小于120秒，即认为复制状态是正常的。
      then
        #echo "Mysql slave status is ok"
        return 0                #<==返回0。
    else
        #echo "mysql replcation is failed"
        JudgeError ${status[2]}  #<==否则，将错误号${status[2]}传入JudgeError函数，
                                       判断错误号是否可以自动修复。
    fi
}
function MAIL(){                #<==定义邮件函数，在范例11-13中讲过此函数。
    local SUBJECT_CONTENT=$1    #<==将函数的第一个传参赋值给主题变量。
    for MAIL_USER  in `echo $MAIL_GROUP`  #<==遍历邮件列表。
    do
        mail -s "$SUBJECT_CONTENT " $MAIL_USER <$LOG_FILE #<==发邮件。
    done
}
function PAGER(){#<==定义手机函数，在范例11-13中讲过此函数。
    for PAGER_USER  in `echo $PAGER_GROUP` #<==遍历手机列表。
    do
        TITLE=$1                #<==将函数的第一个传参赋值给主题变量。
        CONTACT=$PAGER_USER     #<==将手机号赋值给CONTACT变量。
        HTTPGW=http://oldboy.sms.cn/smsproxy/sendsms.action
        #<==发送短信地址，这个地址需要用户付费购买，如果想要免费的，就得用微信替代了。
        #send_message method1
        curl -d  cdkey=5ADF-EFA -d password=OLDBOY -d phone=$CONTACT -d message= "$TITLE[$2]" $HTTPGW
        #<==发送短信报警的命令。cdkey是购买短信网关时，由售卖者提供的，password是密码，
                 也是由售卖者提供的。
    done
}
function SendMsg(){
    if [ $1 -ne 0 ] #<==传入$1，如果不为0，则表示复制有问题，这里的$1即为CheckDb里的返回值（用检测失败的次数作为返回值）,在后文执行主函数main时是通过调用SendMsg传参传进来的值。
      then
        RETVAL=1
        NOW_TIME=`date +"%Y-%m-%d %H:%M:%S"`     #<==报警时间。
        SUBJECT_CONTENT="mysql slave is error,errorno is $2,${NOW_TIME}."
                                                 #<==报警主题。
        echo -e "$SUBJECT_CONTENT"|tee $LOG_FILE #<==输出信息，并记录到日志。
        MAIL $SUBJECT_CONTENT #<==发邮件报警，$SUBJECT_CONTENT作为函数参数
                                     传给MAIL函数体的$1。
        PAGER $SUBJECT_CONTENT $NOW_TIME #<==发短信报警，$SUBJECT_CONTENT作为函数参数传给MAIL函数体的$1，$NOW_TIME作为函数体传给$2。
    else
        echo "Mysql slave status is ok"
        RETVAL=0 #<==以0作为返回值。
    fi
    return $RETVAL
}
function main(){
    while true
    do
        CheckDb
        SendMsg $? #<==传入第一个参数“$?”，即CheckDb里的返回值（用检测失败的次数作为返回值）。
        sleep 30
    done
}
main