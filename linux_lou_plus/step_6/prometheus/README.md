# prometheus监控nginx服务
1. 下载并安装prometheus服务
	wget http://labfile.oss.aliyuncs.com/courses/980/05/assets/prometheus-2.2.1.linux-amd64.tar.gz
	tar xvfz prometheus-2.2.1.linux-amd64.tar.gz
	cd prometheus-2.2.1.linux-amd64
	./prometheus # 运行prometheus
2. 安装支持lua脚本的nginx
	sudo apt install nginx-extras
	# 注意通过 nginx -V 2>&1 | grep lua  检测当前nginx版本是否支持lua
3. 拉取lua
   git clone https://github.com/knyar/nginx-lua-prometheus.git
4. 配置nginx.conf，和网站
5. 配置prometheus