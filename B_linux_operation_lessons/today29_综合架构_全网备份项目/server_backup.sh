#!/bin/bash

# del 180 day ago data
find /backup -type f -mtime +180 ! -name "*week1.tar.gz" | rm 2> /dev/null

# check backup data
find /backup/ -type f -name "finger.txt" | xargs md5sum -c &> /tmp/check.txt
mail -s "check backup info for $(date +%F)" 1033178199@qq.com < /tmp/check.txt