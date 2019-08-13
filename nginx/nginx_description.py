# nginx功能描述

"""
1. nginx是什么
	nginx是一款轻量级的web服务器/反向代理服务器及电子邮件代理服务器
	BSD-like协议下发行
	特点：
		占用内存少，并发能力强
	
	
2. nginx为什么会流行

	高性能、高并发、低 CPU 内存消耗；
	在功能方面：负载均衡、反向代理、访问控制、热部署、高扩展性等特性又十分适合现代的网络架构
	
	
3. 为什么选择nginx
	nginx与apache的相同点：
		同是 HTTP 服务器软件，都采用模块化结构设计
		支持通用语言接口，如 PHP、Python 等
		支持正向代理和反向代理
		支持虚拟主机及 SSL 加密传输
		支持缓存及压缩传输
		支持 URL 重写
		模块多,扩展性强
		多平台支持
	
	Nginx 的优势
		轻量级：安装文件小，运行时 CPU 内存使用率低；
		性能强：支持多核，处理静态文件效率高，内核采用的 poll 模型最大可以支持 50K 并发连接；
		支持热部署，同时启动速度快，可以在不间断服务的情况下对软件和配置进行升级；
		负载均衡，支持容错和健康检查；
		代理功能强大，支持无缓存的反向代理，同时支持 IMAP/POP3/SMTP 的代理。
	Nginx 的劣势
		相比 Apache 模块要少一些，常用模块都有，支持 LUA 语言扩展功能
		对动态请求支持不如 Apache
		Windows 版本功能有限，受限于 Windows 的特性，支持最好的还是 Unix/Linux 系统
		
		
4. nginx工作原理
	
	Nginx 的模块从结构上分为核心模块、基础模块和第三方模块。
		核心模块： HTTP 模块、EVENT 模块和 MAIL 模块
		基础模块： HTTP Access 模块、HTTP FastCGI 模块、HTTP Proxy 模块和 HTTP Rewrite 模块
		第三方模块： HTTP Upstream Request Hash 模块、Notice 模块和 HTTP Access Key 模块及用户自己开发的模块
		
		Nginx 的模块默认编译进 Nginx 中，如果需要增加或删除模块，需要重新编译 Nginx，这一点不如 Apache 的动态加载模块方便
		
		
5. nginx的常用架构简介

	LAMP（Linux + Apache + Mysql + PHP
	LNMP（Linux + Nginx + Mysql + PHP
	Apache 默认配置在未优化的情况下比较占用 CPU 和内存
	
	Nginx 的负载均衡和反向代理配置灵活，并发能力强，处理静态资源性能强，这些特性十分适合在前端调度
	缺点是处理动态资源差一些，这正是 Apache 的强项，所以动态资源交给 Apache 处理。
	nginx + linux+apache + mysql + php
	
	web调度员 Nginx
	这个调度员要求能高效的接收并分发请求，知道后端的服务器健康状态，要能方便的扩展和移除
	
6. 我该如何学习nginx

"""