apt-get update
apt-get install vim nginx -y
service nginx start

vim /usr/share/ngnix/html/index.html
# add -- server1
<h1>www.shiyanlou.com</h1>
# 192.168.0.4
# add -- server2
<h1>static.shiyanlou.com</h1>
# 192.168.0.5
# add -- server3
<h1>api.shiyanlou.com</h1>
# 192.168.0.6