DNS 简介
# dns -- Domain Name system域名系统 -- 是一个分布式命名系统
域名翻译成 IP 地址
主机名.二级域名.顶级域名.不同域直接通过 . 来分割
名在前，姓在后，越是大的域越在后面。
 
# 域名分布
	主机名：一般代表公司或者组织的主机名或者某个服务名
	二级域名（second-level domains）：一般代表公司或者组织的名字
	顶级域名（top-level domains，TLDS）：一般代表的是该公司或者组织在社会中的某个领域，或者所说的国家
	com 表示的是商业，edu 表示的教育机构，gov 表示的政府机构，org 表示的组织机构
	例如 cn 代表的是中国，jp 代表的是日本，ca 代表的是加拿大等等

 
DNS 解析
# dns解析过程
	1. 浏览器首先查看其自己的解析记录缓存
		若是缓存记录中存在域名所对应的 IP 地址，则直接使用该 IP 地址
		若是缓存记录中不存在该域名的相关记录则进入下一步
		
	2. 查找系统的 DNS 解析缓存，因为 DNS 每次查询的记录都会记录在缓存在中，以免再次查询
		在 Windows 中系统启动时便会加载位于 C:\windows\system32\drivers\etc\ 目录中的 hosts 文件于 DNS 缓存中
		Linux 中的 hosts 文件位于 /etc/hosts，其与 Windows 中使用 hosts 类似，但具体实现方式不同
		hosts是dns的前身
		
	3. 若是在系统的 DNS 解析缓存中也未能找到相关的记录，此时便会去请求系统中设置的 DNS 服务器
	（系统中设置的 DNS 服务器可能是路由器分配的默认，也可能是自己设置的权威机构的，也可以能运营商自己的）
	
	4. 部分路由器会有 DNS 解析的缓存，此时会在路由器中查询
	
	5. 若还是没有便会将查询的请求交给 ISP 的 DNS 缓存服务器
	
	6. 依旧没有查询到相关的记录便会开始递归搜索
		由本地 DNS 服务器或者你配置的服务器将相关的请求转发给根域服务器
		根域服务器查询相关的顶级域服务器，然后将请求转发给相关的顶级域服务器
		顶级域服务器查询相关的二级域服务器，然后将请求转发相关的二级域服务器
		最后将查询结果返回给主机
	
	7. 若还是没有相关记录则访问失败

# DNS解析优先级
在 Linux 中我们可以通过 /etc/nsswitch.conf 配置文件修改 DNS 查询的顺序
	$ sudo vim /etc/nsswitch.conf 
		#hosts:		do files nisplus nis dns
		hosts:		files dns myhostname
		# files代表/etc/hosts 文件
		# dns代表系统配置的dns服务器地址
# hosts文件
	hosts 文件中存放常用的 DNS 记录与开发中测试使用的服务器记录.
	文件格式
		IP地址		域名或hostname
	我们可以将测试服务器的 IP 地址与测试域名映射关系存放于此
	这种记录是不会放在公共 DNS 服务器中，一般存放于本地 DNS 或者 hosts 中
	
# DNS服务器配置文件
/etc/resolv.conf
# 格式
	nameserver 10.143.22.118
nameserver 后面对应的便是内网中的 DNS 服务器地址，一般会配置两个，防止一个不可用而导致无法域名解析



DNS 搭建
# dns开源软件
1. BIND：全名为 Berkeley Internet Name Domain，是早在 1980 年左右有 Berkeley 大学公开出来的 DNS 服务实现，
也是使用最为广泛的方案。后由 ISC 基于 BIND 重写发布 BIND9

2. PowerDNS：PowerDNS 由 C++ 实现于 1990 年末，起源一个商业软件于 2002 年开源，
相对于 BIND 在数据库选用上与集群上功能更多更灵活。

3. CoreDNS：由 SkyDNS 进化而来，主要作为一种可插拔的中间件。

4. DNSpod-sr：一款由国内服务商开源的一套 DNS 的实现

# 使用BIND9搭建dns服务器
	1. 安装和配置BIND
		sudo apt-get update # update 可能会有警告
		sudo apt-get install -y bind9 bind9utils bind9-doc
	2. 激活IPv4 Mode
		先修改bind9 service参数文件 -- 设置为IPv4 Mode
		$ sudo vi /etc/default/bind9
			修改：OPTIONS="-4 -u bind"
	3. 确定主DNS服务器
		一般设置两个DNS服务器，一个主要，一个备用
		$ ifconfig -a 查看ip地址
		# 尝试取ping几个有效的内网ip
		$ ping -c 3 192.168.42.1
# DNS服务器的配置
	bind配置文件由多个文件组成-- 这些文件包含在主配置文件/etc/bind/named.conf中
	以named开头的文件 -- bind运行进程的名称
	
	1. 配置选项文件
		$ sudo vim /etc/bind/named.conf.options
		acl "trusted" {
              192.168.42.5; #ns1    信任的名单，只允许它查询dns服务器
			};
			options {
				directory "/var/cache/bind";
	2. 配置本地文件
		$ sudo vim /etc/bind/named.conf.local
		# 在配置文件中添加正向解析和反向解析的文件位置
	3. 创建正向解析域文件
		正向解析：通过主机名获取其对应的广域网 IP 地址，我们以 "host1.shiyanlou.example.com" 为例来编写来这个文件
		根据现有的域文件db.local复制一份db.shiyanlou1.example.com的编辑文件
		$ sudo mkdir /etc/bind/zones
		$ sudo cp /etc/bind/db.local /etc/bind/zones/db.shiyanlou.example.com
		$ sudo vim /etct/bind/zones/db.shiyanlou.example.com
		
		

DNS 验证



