# 基于docker api开发应用
	使用镜像源
		修改$ sudo vim /etc/docker/daemon.json
		重启docker服务
			$ sudo service docker restart

# Docker包的安装和使用
	通过调用python类和函数来实现Docker Remote API的操作
		创建容器
		镜像管理
		
	1. 更新pip源
		vim ~/.pip/pip.conf
		$ sudo pip install --upgrade pip -- 更新pip版本
		
	2. 配置远程访问
		如果需要提供远程访问，需要绑定到网络接口上
			-H=tcp://0.0.0.0:2375 -- 表示将Docker daemon监听到所有网络接口的2375端口上
		- 修改配置文件 /etc/default/docker
			$ sudo vim /etc/default/docker
			# 在末尾添加一下配置
			- DOCKER_OPTS="-H=tcp://0.0.0.0:2375 -H=unix:///var/run/docker.sock"
			# "-H=unix:///var/run/docker.sock -- 表示允许本地访问连接
		- 重启Docker服务
			$ sudo service docker restart
		- 测试
			$ docker -H localhost:2375 info
			# 检测是否会出现系统的详细信息
	3. 配置虚拟环境
		- 使用virtualenv配置环境
			$ cd ~
			$ sudo apt-get install python-virtualenv -- 安装virtualenv
			
			# 安装python3.5及其依赖
			$ sudo add-apt-repository ppa:fkrull/deadsnakes
			$ sudo apt-get update
			$ sudo apt-get install python3.5
			
			# 使用python3.5，Venv为虚拟环境目录命名
			$ virtualenv -p /usr/bin/python3.5 venv
			
			# 激活虚拟环境
			$ source venv/bin/activate
	# !!! 以下其他操作全部在虚拟环境下进行
	
	4. 安装ipython
		$ pip install ipython==5.3
	5. 安装docker包
		pip install docker
	6. 基本使用
		启动ipython
		# 后续操作在ipython中操作
			> import docker
			> client=docker.DockerClient(base_url="tcp://127.0.0.1:2375"
			# 配置了一个tcp实例化客户端
			> client.containers.list()
			# 若为空则新建一个容器
			> client
		# 调用Docker Remote API启动nginx容器
		# 绑定主机的/home/shiyanlou/data和容器的/data
		# 绑定主机端口84和容器端口80
		> container=client.containers.run(name='syl_nginx',image='nginx:latest',volumes={'/home/shiyanlou/data':{'bind':'/data','mode':'rw'}},ports={'80/tcp':84},detack=True)
		# 其中detach表示后台运行
		# 如果不加latest则必须要先拉取否则会出现错误
		# 可以使用localhost:84查看nginx页面
		
		# 列出所有镜像
			> client.images.list()
		

# 获取容器信息
	 获取容器信息
		client.containers.list() 获得容器列表及基本信息
		容器对象的各种属性
	
	- 现在终端中拉取最新版本的redis镜像
		$ docker pull redis:latest
	- 进入ipython
		# 创建两个容器
		> c1 = client.containers.run(image="redis", detach=True)
		> c2 = client.containers.create(image='nginx',volumes={'/home/shiyanlou/data':{'bind':'/data','mode':'rw'}},ports={'80/tcp':85})
		
		# 启动nginx容器
		> c2.start()
		# 获取所有容器的基本信息
		> client.containers.list(all=True) -- 不加all参数只会列出运行中的容器
		
		# 使用字典获取返回信息的存储，获取各种属性
		> results = {}
		> container_list=client.containers.list()
		
		> for container in container_list:
				results['short_id']=container.short_id -- id前10个字符
				results['image']=container.image -- 容器的镜像
				results['top']=container.top() -- 容器的运行进程
				results['stats']=container.stats() -- 容器的流统计信息
		
		
# 使用Dockerfile创建镜像
	> client.images.build()方法
	1. 程序结构，将实现程序放在/home/shiyanlou/build-image.py中
		初始化Client对象
			import docker
			client=docker.DockerClient(base_url='tcp://127.0.0.1:2375")
			
			# 程序逻辑
				处理参数：判断是否输入的是两个参数，读取第一个参数判断是否为路径并且路径下存在 Dockerfile。
				如果存在 Dockerfile，就调用创建镜像的 API 创建镜像。
				
	2. 处理逻辑
		判断是否输入两个参数
	
	4. 测试程序
		$ mkdir /home/shiyanlou/imagetest
		$ cd /home/shiyanlou/imagetest
		$ vim Dockerfile
		创建dockerfile
			FROM ubuntu:14.04
			ENV HOSTNAME=shiyanlou
		$ python bulid-image.py /home/shiyanlou/imagetest build_test
	5. test
		$ docker image ls