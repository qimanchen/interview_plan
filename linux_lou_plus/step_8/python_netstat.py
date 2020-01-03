#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob

PROC_FILE = {
    'tcp': '/proc/net/tcp',
    'tcp6': '/proc/net/tcp6',
    'udp': '/proc/net/udp',
    'udp6': '/proc/net/udp6'
}

STATUS = {
    '01': 'ESTABLISHED',
    '02': 'SYN_SENT',
    '03': 'SYN_RECV',
    '04': 'FIN_WAIT1',
    '05': 'FIN_WAIT2',
    '06': 'TIME_WAIT',
    '07': 'CLOSE',
    '08': 'CLOSE_WAIT',
    '09': 'LAST_ACK',
    '0A': 'LISTEN',
    '0B': 'CLOSING'
}


def get_content(type):
    ''' 读取文件内容
    '''
    with open(PROC_FILE[type], 'r') as file:
        content = file.readlines()
        content.pop(0)  # 去除文件的第一行抬头
    return content


def get_program_name(pid):
    '''获取程序名
    '''
    path = '/proc/' + str(pid) + '/comm'
    with open(path, 'r') as file:
        content = file.read()
    content = content.strip()
    return content


def convert_ip_port(ip_port):
    '''转换
    '''
    ip, port = ip_port.split(':')
    port = int(port, 16)
    ip = [str(int(ip[6:8], 16)), str(int(ip[4:6], 16)), str(int(ip[2:4], 16)),
          str(int(ip[0:2], 16))]
    ip = '.'.join(ip)
    return ip, port


def get_pid(inode):
    '''
    获取 PID 的原理：
    内核为每个进程维护一个打开文件的列表，该表被称为文件表（file table）。该表由一些非负整数的文件描述符（file descriptors）作为索引，一个文件描述符对应进程中一个打开的文件。
    在 /proc/net/tcp 可以得到 inode 值，而这个 inode 就是相关进程的 socket 文件所在的 inode 值
    获取的方法：
    1. 首先遍历所有的 /proc/ 进程 id/fd/ 文件夹
        遍历所有的目录有三种方式 walk，listdir，glob
        三者遍历的速度 listdir > glob > walk
        并且只有 glob 支持通配符遍历，而在 /proc/ 目录下有很多系统性能信息相关的目录与文件，没必要全部遍历，只需要找进程相关的目录即可
        当然也可以使用 psutil.pids() 获取所有的 pid，然后用双重循环来遍历所有文件描述符的索引
        但是我们若使用了 psutil 模块的话，很多地方获取起来就会简单很多
    2. 因为 socket 的通信通道没有文件名，所以文件对应的软连接是 socket:inode 值，所以查看有没有匹配的值
    3. 然后获取相关文件的 path 中的 pid 即可
    '''
    for path in glob.glob('/proc/[0-9]*/fd/[0-9]*'):
        try:
            if str(inode) in os.readlink(path):
                return path.split('/')[2]
            else:
                continue
        except:
            pass
    return None


def main(choose):
    '''获取并展示端口连接相关信息
    '''
    templ = "%-5s %-30s %-30s %-13s %-6s %s"
    print(templ % (
        "Proto", "Local address", "Remote address", "Status", "PID",
        "Program name"))
    content = get_content(choose)

    for info in content:
        iterms = info.split()
        proto = choose
        local_address = "%s:%s" % convert_ip_port(iterms[1])
        status = STATUS[iterms[3]]
        if status == 'LISTEN':
            remote_address = '-'
        else:
            remote_address = "%s:%s" % convert_ip_port(iterms[2])
        pid = get_pid(iterms[9])
        program_name = ''
        if pid:
            program_name = get_program_name(pid)
        print(templ % (
            proto,
            local_address,
            remote_address,
            status,
            pid or '-',
            program_name or '-',
        ))


if __name__ == '__main__':
    choose = 'tcp'
    if len(sys.argv) > 1:
        choose = sys.argv[1]
    main(choose)