# 课程介绍
	1. 负载均衡遗留知识点补充
	2. 高可用服务的概念介绍
	3. 部署安装高可用服务
	4. 高可用服务配置文件参数说明
	5. 高可用服务VRRP协议原理
	6. 高可用服务常见问题（脑裂问题）
	7. 高可用服务如何进行监控
	8. 高可用服务实现双主配置
	
# 课程回顾
	1. LNMP架构常见问题
		a 如何实现web服务器和存储服务器建立关系
			web + nfs
				1. 找到网站数据存储的本地目录
				2. 如果本地存储目录有数据，需要进行迁移备份
				3. 编写查看nfs服务配置参数 root 和普通用户的访问
				4. 实现挂载操作（实现开机自动挂载）
				-- 进企业之前，检查服务器的配置
			web + mysql
				1. 将本地数据数据进行备份 mysqldump mysqladmin
					mysqldump --all-database
				2. 将备份数据进行迁移
				3. 将数据进行还原，并设置好远程连接的服务
				4. 修改代码文件，连接新的数据库服务
		b 负载均衡概念
			集群
			负载
			反向代理
		c 负载均衡集群架构部署
			集群环境部署
			负载均衡部署
			upstream模块 实现负载均衡
			proxy_pass  反向代理
		d 负载均衡相关模块详细说明
			proxy_set_header
		e 负载均衡异常排错思路
	
# 课程内容
	01. 负载均衡的企业应用
		1） 根据用户访问的uri信息进行负载均衡
			多个集群
			a 架构环境规划
				/uploads		10.0.0.8:80		html/www/upload		upload服务器
					mkdir /html/www/upload
					echo "upload-web 10.0.0.8" > /html/www/upload/oldboy.html
				/static			10.0.0.7:80		html/www/static		static服务器
					mkdir /html/www/static
					echo "static-web 10.0.0.7" > /html/www/static/oldboy.html
				/				10.0.0.9:80		html/www
					echo "default-web 10.0.0.9" > /html/www/oldboy.html

			b 编写负载均衡配置文件
				upstream upload {
					server 10.0.0.8:80;
				}
				upstream static {
					server 10.0.0.7:80;
				}
				upstream default {
					server 10.0.0.9:80;
				}
				server {
					listen	80;
					server_name www.oldboy.com;
					location / {
						proxy_pass http://default;
						proxy_set_header Host $host;
						proxy_set_header X-Forwarded-For $remote_addr
						proxy_next_upstream error timeout http_404 http_502 http_503;
					}
					location /upload {
						proxy_pass http://upload;
						proxy_set_header Host $host;
						proxy_set_header X-Forwarded-For $remote_addr
						proxy_next_upstream error timeout http_404 http_502 http_503;
					}
					curl -H host:www.oldboy.com 172.16.1.9
					location /static {
						proxy_pass http://static;
						proxy_set_header Host $host;
						proxy_set_header X-Forwarded-For $remote_addr
						proxy_next_upstream error timeout http_404 http_502 http_503;
					}
				}
			c 测试
				systemctl restart nginx
			总结：
				实现网站集群动静分离
				- 提高网站服务安全性
				- 管理操作工作简化
				- 可以划分不同人员管理不同的集群服务
		2）根据用户访问的终端信息显示不同页面
			a 准备架构环境
				iphone		www.oldboy.com		-- iphone_access 10.0.0.7:80	mobile移动端
					echo "iphone_access 10.0.0.7:80" > /html/www/oldboy.html
				谷歌		www.oldboy.com		-- google_access 10.0.0.8:80	web端集群
					echo "google_access 10.0.0.8:80" > /html/www/oldboy.html	default
				IE 360		www.oldboy.com 		-- IE 10.0.0.9:80
					echo "IE 10.0.0.9:80" > /html/www/oldboy.html
			upstream web {
				server 10.0.0.8:80;
			}
			upstream mobile {
				server 10.0.0.7:80;
			}
			upstream default {
				server 10.0.0.9:80;
			}
			server {
				listen	80;
				server_name www.oldboy.com;
				location / {
					if ($http_user_agent ~* iphone) {
						# 目标字符串中只要包含该字符即可实现
						proxy_pass http://mobile;
					}
					if ($http_user_agent ~* Chrome) {
						proxy_pass http://default;
					}
					proxy_pass http://default;
					proxy_set_header Host $host;
					proxy_set_header X-Forwarded-For $remote_addr
					proxy_next_upstream error timeout http_404 http_502 http_503;
				}
			}
	03. 高可用服务的介绍
		-- 多台负载均衡服务器
			一主一备
			监控主是否服务正常，否则切换为备
			避免负载均衡服务出现单点问题
	04. 高可用服务原理
		keepalived -- VRRP协议
			-- 通过VRRP协议进行沟通，确定主和备
			1. VRRP协议，进行主备通讯
			2. VRRP协议，进行主备竞选
			3. VRRP协议，主向备发送组播包
			4. VRRP协议，不传输密文信息 -- 影响效率
			-- 主出现问题，当备收不到组播包
			5. 主不在发送组播包
				备顶上
		客户端通过虚拟ip地址来确定
	05. 如何实现部署高可用服务
		利用keepalived软件实现
		作用
			1. 为LVS服务而诞生出来的
				LVS负载均衡软件
			2. 实现高可用服务
	06. 高可用keepalived服务部署流程
		a 准备两台服务
		b 安装keepalived
			yum install -y keepalived
		c 编写keepalived 文件
			rpm -ql keepalived -- 查找配置文件
			/etc/keepalived/keepalived.conf
			-- 分成三个部分
				GLOBAL CONFIGURATION	-- 全局配置部分
				VRRPD CONFIGURATION		-- VRRP协议配置部分
				LVS CONFIGURATION		-- LVS服务管理配置部分
			global_defs {  -- 全局配置部分
		   notification_email { -- 设置发送邮件信息的收件人，这部分可以不用配置，通过监控服务配置
			 acassen@firewall.loc
			 failover@firewall.loc
			 sysadmin@firewall.loc
		   }
		   notification_email_from oldboy@163.com -- 设置连接的邮件服务器信息
		   smtp_server smtp.163.com
		   smtp_connect_timeout 30
		   
		   router_id lb01 -- 高可用集群主机身份表示（集群中身份标识名称不能重复）
			-- 
		   vrrp_skip_check_adv_addr
		   vrrp_strict
		   vrrp_garp_interval 0
		   vrrp_gna_interval 0
		}

		vrrp_instance oldboy { -- VRRP相关配置（VRRP实例配置 -- 一个服务可以启动多个主进程）
			state MASTER		-- 表示该主机在VRRP实例中身份（MASTER/BACKUP)
			interface eth0		-- 指定虚拟IP地址出现在什么网卡上
			virtual_router_id 51	-- 标识主机在集群身份信息，多台高可用服务配置要一致，否则会出现脑裂
			priority 100		-- 设定优先级，优先级越高，就越有可能成为主
			advert_int 1		-- 发送VRRP组播包的时间间隔，主和从设置要一致，否则会出现脑裂
			authentication {	-- 实现通讯需要有认证
				auth_type PASS -- 明文
				auth_pass 1111
			}
			virtual_ipaddress {	-- 配置虚拟IP地址信息
				10.0.2.3/24 -- 主和从配置一致，对外的虚拟IP地址
			}
		}
		
		# 配置文件
		[root@lb01 keepalived]# cat keepalived.conf 
		! Configuration File for keepalived

		global_defs {
		   router_id lb01
		}

		vrrp_instance oldboy {
			state MASTER
			interface eth1
			virtual_router_id 51
			priority 150
			advert_int 1
			authentication {
				auth_type PASS
				auth_pass 1111
			}
			virtual_ipaddress {
			192.168.90.90
			}
		}

		c 启动keepalived
			systemctl start keepalived
			systemctl enable keepalived
		d 改变访问负载均衡服务器地址为虚拟IP 192.168.90.90
			# 访问过程
			1 - 90
			90 - 17
			17 - 90
			90 - 1
	07. 高可用服务企业应用
		1. 高可用服务常见异常问题 -- 脑裂问题）
			出现原因：
				高可用备用服务器接收不到主服务器发送的组播报，导致备也成为主（同样占用虚拟IP）
			物理原因： -- 心跳线
				高可用集群之间通讯线路出现问题
			逻辑原因：
				有安全策略阻止
			如何解决脑裂问题
				a 进行监控，发出告警
					-- 备服务器出现VIP地址的原因
						a 主服务器出现故障
						b 出现脑裂问题
					ip a
					-- check_backup_get_VIP.sh
					#!/bin/bash
					ip a s eth0 | grep "10.0.0.3" > /dev/null
					if [ $? -eq 0 ];then
						echo "keepalived warning, please check" | mail -s Warning -- keepalived 18770917247@163.com
					fi
					
					-- 如果出现问题，那么查看messages日志
				b 直接把一台服务器的keepalived服务
		2. keepalived服务自动释放VIP资源
			-- 比如当主的nginx服务停止后，要切换到备
			nginx + keepalived; nginx服务停止，keepalived也必须停止
			1. 主，编写监控nginx服务状态
				-- 进程信息
				-- 端口号
				netstat -tunlp nginx | grep 80
				-- 脚本名称会被ps所检测到
				check_web.sh
				#!/bin/bash
				num=`ps -ef|grep -c nginx`  -- 这里会导致异常,注意这个判断条件
				if [ $num -lt 3 ]; then
					systemctl stop keepalived
				fi
			2. 测试
			3. 实时监控nginx服务状态 --- keepalived配置文件
				vrrp_script check_web { -- 
					script "/server/scripts/check_web.sh"  -- 定义要监控的脚本（绝对路径，脚本具有执行权限）
					interval 2	-- 执行脚本的间隔时间（秒）
					weight 2	-- 查询这个服务
				}  -- 放置到全局和vrrp中间
				track_script {		-- 
					check_web		-- 调用执行你的脚本信息
				} --放置到vrrp区域中
				-- vim： set list 查看符号标记
				ps -- 检测的脚本必须有执行权限
		3. keepalived实现双主配置
			有效利用资源， 互为主备的过程（不同的资源blog,www，访问不同的主）
			a 编写lb01，keepalived配置文件
				global_defs {
				   router_id lb01
				}

				vrrp_instance oldboy {
					state MASTER
					interface eth1
					virtual_router_id 51  -- 主和备要一致
					priority 150
					advert_int 1	-- 定义组播包发送的间隔时间（秒），这个时间主和备配置要一致
						# 如果不一致，会出现脑裂
					authentication {
						auth_type PASS
						auth_pass 1111
					}
					virtual_ipaddress {
					192.168.90.90
					}
				}
				
				vrrp_instance oldgirl{ -- 定义一个不同的实例
					state BACKUP
					interface eth1
					virtual_router_id 52 -- 实例
					priority 100
					advert_int 1
					authentication {
						auth_type PASS
						auth_pass 1111
					}
					virtual_ipaddress {
					192.168.90.91
					}
				}
			b 编写lb02
			502 -- 后台服务有问题
			c 测试
				curl -H host:www.oldboy.com 10.0.0.5
				编写域名和IP解析信息 --
				192.168.90.90 www.oldboy.com
				192.168.90.91 bbs.oldboy.com
				-- 解析抓包查看
					www.oldboy.com -- 192.168.90.90
					bbs.oldboy.com -- 192.168.90.91
		4. 高可用服务安全方位配置 -- 负载均衡主机必须有外网
			1. 修改nginx负载均衡文件
				www		listen 10.0.0.3:80; -- 指定监听负载均衡的地址
				bbs		listen 10.0.0.4:80；
				-- 监听的地址，不是主机上有的网卡地址
			2. 修改内容文件
				-- 异常问题
					1. 如何设置监听网卡上没有的地址
						修改内核 -- 允许监听不是本机拥有的地址 -- centos7
							echo 'net.ipv4.ip_nolocal_bind = 1' >> /etc/sysctl.conf
							sysctl -p  --- 加载内核文件
							
							echo "1" > /proc/sys/net/ipv4/ip_nonlocal_bind
						-- 涉及到端口和IP的操作，必须restart
			3. 重启nginx服务
			
# 实验楼配置 keepalived方案
#全局配置，在发现某个节点出故障的时候以邮件的形式同时管理员
global_defs {
   notification_email {    #设置报警邮件地址，可以设置多个
        shiyanlouAdmin@localhost #每行一个，如果开启邮件报警，需要开启本机的 Sendmail 服务
        shiyanlou@admin.com
   }
   notification_email_from root #设置邮件的发送地址
   smtp_server 127.0.0.1 #设置 STMP 服务器地址
   smtp_connect_timeout 30 #设置连接 SMTP 服务器的超时时间
   router_id LVS_DEVEL    #标识，发邮件时显示在邮件主题中的信息
}

#配置 vrrp 实例
vrrp_instance VI_1 {
    state MASTER  #指定 Keepalived 角色， MASTER 表示此主机是主服务器，BACKUP 表示此主机是备用服务器
    interface eth0    #指定 HA 检测网络的接口
    virtual_router_id 51 #虚拟路由标识，这个标识是一个数字，同一个 vrrp_instance 下，MASTER 和BACKUP 必须是一致的
    priority 101  #定义优先级，数字越大，优先级越高。在同一个 vrrp_instance 下，MASTER 的优先级必须大于 BACKUP 的优先级
    advert_int 1  #设定 MASTER 与 BACKUP 负载均衡器之间同步检查的事件间隔，单位是秒
    authentication { #配置 vrrp 直接的认证 
        auth_type PASS    #设定验证类型和密码，验证类型分为 PASS 和 AH 两种
        auth_pass 1111    #设置验证密码，在一个 vrrp_instance 下，MASTER 与 BACKUP 必须使用相同的密码才能通信
    }   
    virtual_ipaddress { #配置虚拟 IP，可以设置多个，每行一个
        192.168.0.10
    }
}

#配置虚拟服务器
virtual_server 192.168.0.10 80 { #配置虚拟服务器，需要制定虚拟 IP 地址和端口，IP 与端口用空格隔开
    delay_loop 6 #设置运行情况检查时间，单位是秒
    lb_algo rr   #设置负载调度算法，这里设置为 rr，即论叫算法
    lb_kind DR   #设置 LVS 实现负载均衡的机制，有 NAT，TUN，DR 三个模式可选，这里选择 DR
    #persistence_timeout 50 会话保持时间，单位是秒，一般针对动态网页很有用，这里需要这个配置
    protocol TCP #制定协议转发类型，有 TCP 和 UDP 两种。

    real_server 192.168.0.4 80 { #配置 real server 的信息，服务节点1
        weight 1 #配置该节点的权重，权值大小用数字表示，设置权值的大小可以分不同性能的服务器分配不同的负载，性能较低的方服务器，设置权值较低，这样能合理的利用和分配系统资源
        HTTP_GET {    #设置健康检查
            url {    #访问这个地址，判断状态码是否 200
              path /
          status_code 200
            }
            connect_timeout 3    #表示3秒无响应超时
            nb_get_retry 3    #表示重试次数
            delay_before_retry 3    #表示重试间隔
        }
    }
    real_server 192.168.0.5 80 { #配置服务节点2
        weight 1
        HTTP_GET {
            url {
              path /
              status_code 200
            }
            connect_timeout 3
            nb_get_retry 3
            delay_before_retry 3
        }
    }
}
# 课程总结
	1. 负载均衡服务扩展补充
		根据uri信息进行负载均很（动静分离）
		根据user-agent信息进行负载均衡
	2. 高可用服务作用（避免出现单点故障）
	3. keepalived高可用服务
		管理lvs负载均衡软件
		实现高可用功能 vrrp原理
	4. keepalived服务企业应用
		-- 配置文件
		-- 脑裂问题
		-- 如何实现自动释放资源 -- 编写脚本 修改keepalived文件
		-- 如何实现双主配置	-- 编写配置文件，编写多个实例
		-- 如何实现负载均衡安全访问 -- 配置监听vip地址信息
# 练习
01. 如何实现keepalived服务实现实时监控 -- while
02. nginx服务启动keepalived自动服务 -- 调整优先级，将其切换
	weight
03. 预习 zabbix监控服务 （基础部分（手工配置） + 高级部分）
	克隆好一台zabbix服务器 -- zabbix软件