# kubernetes最基本和核心的概念： pod

# 实验原理
	Pod是一组（可以是一个）container的集合，这些container一起调度，可以视为一个基本单元
	
	kubernetes的需求：
		1. 这个unit需要有个唯一的ip，并且可以跨机器，在集群内互相访问
		2. 最好不能太依赖于docker，而要支持多种container runtime
		3. 用户最终使用kubernetes将应用部署在集群中，这个unit最好贴近于app的概念，而不是底层系统
		4. 支持在pod中运行多个程序，（container支持的不是很好）,pod中的多个容器虽然各自独立，但默认是共享网络和内存的
		   并且还可以定制为其他共享资源
		应用/服务 -- 用户想在容器平台运行的程序 -- 以pod的形式存在
		
Pod的基本结构 -- pod.yaml
	spec字段 -- 具体的属性描述
		pod的这个字段是个container列表，内部信息与docker类似，配置应用，运行应用，只是语法上的一个差别
		container里面的主要基本信息：
			启动命令：command
			镜像信息：
				image： 镜像地址
				imagePullPolicy:镜像拉取策略，IfNotPresent -- 没有才去pull，Always -一直去pull，适用于镜像tag不变但内容会变化的场景
			名称：容器的名称，kubernetes所有资源的查找和使用主要都是靠名称，我们使用kubectl exec时，就会用到
			resources: 具体描述了这个pod对于计算资源的需求信息
			terminationMessagePath: 记录容器退出时的最后信息（成功或异常）,用于检测
			terminationMessagePolicy: 从那些地方取容器最终的状态信息
				File:默认值，表示只从上面的terminationMessagePath所在位置取状态信息
				FallbackToLogsOnError:如果上面的文件没有内容，那么就从容器的日志中取一部分作为状态信息（一般为stdout的输出）
			
	status字段 -- 状态信息 -- 创建后不断改变
	
	
Pod的状态
	执行过程：
		1. 调度到某台机器上，kubernetes根据一定的优先级算法选择一台机器将其作为pod运行的机器
		2. 拉取镜像
		3. 挂载存储装置等
		4. 运行起来；如果有健康检查，会根据检查结果来设置状态
	pod的状态结果：
		主要包含两部分:
		
		# pod级别的信息
			hostIP: pod所在主机的ip
			phase: pod的状态
				Pending: 表示还没有开始调度到某台机器上，如果没有符合条件的主机，就会一直处于Pending状态
				Running: 运行中
				Succeeded: 有些pod不是长久运行的，比如cronjob，需要发馈执行结果
				Failed: Pod的container异常退出，比如command写的有问题
				Unknown: 未知，比如pod所在的机器无法连接
			podIP: pod分配的ip，这个ip是全集群唯一的
			qosClass: 资源分配相关
			startTime: 启动时间
		# 各个container的信息
			包含每个container的运行信息
			probe信息：一列状态检查信息，表明pod是否到达某个状态
				type字段：有些固定值，大体代表部署的一个过程
					PodScheduled/Unschedulable:已经调度到某台机器上了/无法调度到某台机器
					Initialized: 所有的init containers都成功启动
					ContainersReady:所有的containers都已经ready
					Ready:pod完全可以对外提供服务了
				status字段：具体表明是否达到这个状态
		containerStatuses：提供pod各个容器的基本信息：
			restartCount: 重启次数。kubernetes对于资源的处理不是一次性的，如果某一次部署出错了，它会一直重试，直到到达目标状态
			state: pod下每个container的状态，这个状态比pod.phase更加准时和精确-- pod.phase 是根据此计算出来的
	# kubectl在展示状态时，会将pod的phase字段以及container的状态信息结合起来计算出一个状态展示出来
	一个有问题的pod文件
	
	$ kubectl create -f bad-pod.yaml # 创建bad-pod
	$ kubectl get pods -w # 执行
	# ImagePullBackoff
	
	
# 资源申请
	pod也可以实现对cpu和内存的使用，但仍然是容器级别的，需要对pod的每个容器做设置
	没有设置时，表示不限制
	
	pod提供了requests和limit两个限制：
		requests:pod运行所需的最少资源，kubernets在调度pod时，就是通过这个设置来挑选node
		limits:pod运行资源上限，超过就会被pod kill掉
	wp.pod
	
	# 创建
	$ kubectl create -f wp.pod
	$ kubectl describe pods wp
	# describe -- 查看某个资源的信息，包含的信息更多，凸显重要信息
	
	pod在调度到某个机器上之后，在这个机器的状态信息中看到资源占用的情况
	$ kubectl describe node kube-node-2(node的名称)
	
# Qos-表示Kubernetes对不同pod因其requests/limits设置而对其运行情况的保障
	Guaranteed: requests=limits, 高优先级，kubernetes保证只要资源使用不超过limits就不会被kill
	Burstable: requests< limits,Pod可以使用其中的资源，中优先级，当机器资源紧张时，pod资源超过requests可能会被kill掉
	BestEffort: 没有设置具体的requests和limits，低优先级，如果机器资源紧张，这些pod会优先被kill掉
	
	# Guaranteed example -- qos-demo.yaml
	$ kubectl create -f qos-demo.yaml
	$ kubectl describe pods qos-demo
	
	# BestEffort example -- qos-demo.yaml
	$ kubectl create -f qos-demo-2.yaml
	$ kubectl describe pods qos-demo-2
	
	
# 启动命令
	pod中，kubernetes使用了更加简单的command/args的参数设置
	参数设置规则：
		pod不设置任何参数，直接用镜像里面自带的参数
		pod的command和args都设置，使用设置的命令和参数
		pod只设置command，完全忽略镜像中的参数
		pod只设置args，镜像中的命令与新参数一起使用
		
	建议：
		将启动命令在镜像中设置好参数，或者在pod中设置的参数的同时，要填好command
	- commands.yaml
	$ kubectl create -f commands.yaml
	$ kubectl get pods -w # 查看command-demo是否是Running或Completed的状态，如果不是就等待一会
	$ kubectl logs command-demo
	
	
# 健康检查
	容器并不等于应用/服务。所以我们需要健康检查来统一两者的状态，这样我们就知道当服务异常时，容器也会退出。
	
	# 存活检查
		liveness probe): 用于判断容器是否需要重启
	# 可用性检查
		readiness probe): 用于判定容器是否可以正常提供服务并被挂载在负载均衡后面
		
	一般的应用不会有这么精细的区分，这时候存活性检查和可用性检查用同样的配置即可。
	
	对于端口服务：可以通过检查其端口是否开启，http endpoint 是否可以访问来判断其健康状态。
	非端口服务：可以通过 exec 进去之后执行相应的命令来检查，pod 所在机器的 kubelet 来执行这些检查
	
	# EXEC
		通过 exec 到容器中执行命令来进行健康检查
		liveness-exec.yaml
		1. 让 command 不断地创建删除文件，健康检查去检查这个文件
		2. 这个例子中只配置了 livenessProbe
		3. command: 就是健康检查执行的命令。如果执行结果状态码为 0，就认为通过，其它的认为失败
		4. periodSecounds: command 执行的间隔，健康检查是一个持续性的过程，需要反复执行。
		5. initialDelaySeconds：因为好多程序启动时有初始化时间。比如 java 程序，初始化一般就比较慢。这时候如果立马做健康检查就不太合适，
		   initialDelaySeconds 就是设置了一个合理的时间，等过了这个时间再做检查。
		
		# 执行检查
		$ kubectl create -f liveness-exec.yaml
		# 然后反复执行
		$ kubectl describe pods liveness-exec
		
		# 通过get查看pods信息
		$ kubectl get pods | grep liveness
		等待的时间越久，重启的次数越多
	
	# HTTP
		即是通过调用 http 服务的某个路径，然后根据错误码来判定。 http status code 的 200-400 代表成功，其它代表失败。
		
		liveness-http.yaml
		
		httpGet: 表示这是一个 http 类型的健康检查
		path: http 的路径
		httpHeaders: 发送请求所带的 headers 字段，不同的场景可能有不能的需求。
		
		kubectl create -f liveness-http.yaml
		kubectl describe pods liveness-http
	# TCP
		对于监听 tcp 端口的服务，我们可以尝试与这个端口建立连接。如果成功，则认为服务正常。
		liveness-tcp.yaml
		
		这个实例中配置了 livenessProbe 和 readinessProbe,从具体的配置上来看，与 http 的配置是很像的。只是其配置中需要指明的是端口
		
		kubectl create -f liveness-tcp.yaml
		kubectl describe pods goproxy
		着重看下 liveness 和 readiness 的一些其他默认值：
			timeout: 
				超时时间，如果超时了就认为失败了
			success/failure: 
				图中的配置是如果成功一次了就认为正常，如果失败了三次才认为失败。这样可以有效地避免因为偶然的偏差导致容器被标记为异常。
				
				
# 多容器Pod
	任务：
		收集日志。
			这样不用修改原来的服务，可以用另外的容器来适配各种日志收集系统。
		做 Proxy。
			比如我们的程序需要访问外部服务（ db 等），可以固定配置为 localhost, 
			由其他的容器来决定如何转发请求，相当于将动态配置的需求交由其他的容器来做。
	好处就是让主要的服务容器不做修改，就能更好地适配各种系统。
	另外，也能较好地做到职责分离，不需要由一个容器来处理过多的任务
	
	two-containers.yaml
	
	kubectl create -f two-containers.yaml
	kubectl get pods -w
	
	-w 参数：
		-w 的意思是 watch, 就是监听的意思。加了这个参数后， kubectl 不会退出，会一直监听 pods 的变化。
	READY 下面的 0/2 ，这个 2 就是表示两个容器的意思。一般情况下，需要等到 2 个容器都是 ready 之后 Pod 才会处于运行中。
	在这个例子中，因为一个 container 运行完程序就结束了
	
	# 使用exec命令查看能否读取到debian-container写入的文件
	$ kubectl exec -it two-containers -c nginx-container bash
		kubectl的exec命令类似于docker的exec，区别在于其exec的目标是Pod
		当pod是单个容器时，其结构与docker是一致的，当pod有多个容器时
		就需要指明具体的目标container，默认值是yaml里的第一个容器
		

# InitContainers
	initContainers 是 Pod 提供的另外一个非常有用的功能。它的结构与普通的 container 类似，但是作用上有很大的区别：
		1. 它们是短期运行的程序，不是持久运行的进程。
		2. 顺序执行，并且每一个 initContainer 必须等待前一个执行成功才能继续执行。
		   正常的 container 必须等待前面的 initContianer 都执行完成之后才能开始执行。
	用途：
		程序在运行前需要等待某个条件才能执行。比如服务 A 需要等待服务 B 可用时才能开始运行
		程序需要某些动态的配置信息生成之后才能正常运行
		程序需要同步好某些数据之后才能正常运行，比如 mysql-slave
		
	就是说某个服务的运行，需要一些前置条件（服务依赖、文件等等）才能正常运行。
	init.yaml
	
	$ kubectl create -f init.yaml
	$ kubectl get pods -w   # 继续 watch pods 的变更
	PodInitializing 表示 initContainers 已经执行完毕，开始执行正常的 containers。
	如果大家看不到 STATUS 的状态变化可能是因为其它的 pod 干扰了，可以执行 kubectl delete pod <pod-name> 删除多余的 pod
	
	$ kubectl exec -it init-ctr-demo sh
	