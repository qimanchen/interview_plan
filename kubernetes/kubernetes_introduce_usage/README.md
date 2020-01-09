# 安装Kubernetes集群
# Kubeadm-dind-cluster -- 使用预先提供的脚本直接运行一个Kubernetes
	1. cd /home/shiyanlou
	2. ./dind-cluster-v1.10.sh
	3. 通过./dind-cluster-v1.10.sh up 启动一个集群
	
	master-slave架构，master结点上会部署很多控件，slave只运行一些agent
	
# kubectl -- kubernetes集群交互的一个命令工具
# kubernetes对外通过http端口暴露服务，kubectl通过与kubernets api server的http端口
	1. 查看版本和信息
		$ kubectl version
			版本信息显示了client(kubectl)以及server(api server)组件的版本详细信息
		$ kubectl cluster-info
	2. 配置文件
		cat ~/.kube/config
	kubectl可以配置访问本地的集群也可以访问远程的集群
		'current-context' -- 当前kubectl所交互的环境
	# 详细信息见kube_config
	
# 基本概念
	
	Resource -- 表示集群中的各个资源
		pod结点-主机、container容器、proxy路由、config配置文件等
		
		这些有着的共同属性：名称、创建时间、标签、uuid等
	kubernetes对这些信息抽象，提供一个通用的metadata结构
	构成一个形式类似的数据结构
	
	# 查看一个配置文件的信息
		$ kubectl get cm cluster-info -n kube-public -o yaml
		- get: 查看某个资源
		- -o yaml: 输出格式为yaml，也可以为json
		- node/cm: 查看资源类型，node - 结点，cm(ConfigMap)-配置文件
		- -n <namespace>: 查看某个namespace下的资源
		- kind： 表示类型，结点Node,配置文件ConfigMap
		- apiVersion: api版本
		- spec: 这个resource自己特定的信息
		- metadata: 基本信息，所有resource都有这个字段，且结构一样
			- name: resource 名称
			- resourceVersion:版本，修改此resource后会向上增加
			- selfLink:通过http api访问此resource路径
			- uid: uuid 唯一标识
			- creationTimestamp:创建时间
			- labels: 这个resource标签，可以通过标签来过滤匹配
			- annotations: 类似labels，记录一些附加的信息，但不能用来做过滤匹配
			- namespace: 资源所属的命名空间，有的资源有，有的资源没有
	# 查看一个结点的信息
		$ kubectl get node kube-master -o yaml
		
		
	Namespace -- 名称隔离
		kubernetes的资源分为两类：一种属于Namespace，一种不属于
		
		namespace也是一种 resource
		# 集群提前建好的
		$ kubectl get ns kube-system -o yaml
			- ns: namespace的简写
			
		#集群创建完成后会自动创建三个namespace：
			- default: 默认的namespace，在命令行中如果要查看所属namespace下的资源
			  时，可以忽略掉-n参数
			- kube-system: 系统的namespace，系统的一些组件都运行在这个下面
			- kube-public: 存放系统信息的namespace
		$ kubectl get ns -- 查看这些namespace
			-- 列举出某种资源，会以表格的形式输出
			显示所有namespace的名称、状态和创建时间
		# namespace本身不属于namespace，所以只需要指定类型(ns),
		  其他属于namespace的资源需要在查看时指定namespace（-n参数）
	
	
	操作Resource
		kubectl可以对资源进行增删改
		1. 操作namespace
			- 创建一个namespace
				$ kubectl create ns test
				$ kubectl get ns test -o yaml  -- 查看这个新建namespace
				
				通过给kubectl加 -v参数可以看到详细的创建步骤：
					$ kubectl create ns test-2 -v=9
					kubectl与kubernetes api是通过rest api进行交互的，
					kubectl通过命令行传入的参数生成合适的body发送个api server
					9标识日志级别，数字越大，信息越全
				- 创建执行过程
					- 读取kubectl的配置文件，判断需要与那个api server交互
					- 生成request body，可以看到创建完成后的yaml数据类似
					- 调用API,终端打印了详细的参数以及结果
					- 输出结果
					
				生成body-调用apiserver-返回结果，许多做了简化，不用用户填写参数
				可以通过指定参数文件来执行
					$ kubectl create -f test-3.yaml
				
				- 通过将需要创建资源的信息保存到yaml中，在使用create命令去创建。
					同样可以是json格式的文件
					该配置文件可以包含任何资源
					
					- 创建时用的yaml和创建好后的yaml的字段是不同的，有些字段，api server
					会自动添加上去，即使自己提供了，api server也会覆盖
						- uid
						- creattionTimestamp
						- selfLink
						- resourceVersion
						- status: 表示资源的状态，只有创建成功后才有意义
		2. 操作ConfigMap
			ConfigMap -- 像环境变量或很多软件的配置文件
			$ kubectl create cm config --from-literal=a=a --from-literal=b=b -n test -v=9
				- cm: ConfigMap的简写
				- config: 要创建的ConfigMap的名称，可以自己定义
				--from-literal=a=a:表示直接从命令行指定key-value值,
				  a=a得格式 <key>=<value>，这个参数可以指定多次
				-n test: 在test这个namespace下面创建ConfigMap
				-v=9: 显示创建过程得详细信息
			
			# 对于kubectl而言，不管创建什么资源都是restapi调用
			$ kubectl get -n test cm config -o yaml
				data部分就是 ConfigMap的数据部分 -- 通过命令行指定的参数
				
		3. 删除资源
			$ kubectl delete cm config -n test 
			# 删除之前创建的ConfigMap资源
			
			$ kubectl delete ns test test-2 test-3
			# 删除之前创建的Namespace
			-- 同类型的资源删除，可以一次指定多个名字后删除多个资源
			
		# namespace下的资源和namespace是从属关系
		# 所以删除namespace时，会将其下的资源一并删除

# 查看集群结构
	kubernetes自身的组件是通过Resource结构来呈现的
	
	可以通过研究 kube-system这个namespace来查看对应的集群结构
	$ kubectl get pods -n kube-system
		- pods: 类似于docker中的container，是kubernetes最基本单元之一
		kubernetes 本身的组件是通过容器化的方式运行在集群中，并且都存放在kube-system
		这个namespace下
		
		- etcd: kubernetes的存储组件，它的数据主要都存储在其中
		- apiserver: kubernetes对外提供api服务的组件，主要负责于etcd交互
		- scheduler:负责调度pod的组件，决定将pod放在那个机器上运行
		- controller-manager: 当pod调度到机器上后，其他服务将pod运行起来
		  相当于一个具体执行任务的组件
		- proxy: 负责pod/服务访问的组件，每个机器上都有一个，所以上面有三个结点
		- dns：负责集群内的dns功能
		- dashboard: 提供一个UI管理界面
		- kubelet 每个结点上都会有的agent，负责本地机器上的一些任务执行
					