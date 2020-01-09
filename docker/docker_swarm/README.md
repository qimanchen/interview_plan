# Docker Swarm是一个Docker集群部署和管理工具
# 可以将一组Docker服务器虚拟成一台容器服务器
# 提供标准的Docker API
# 所有直接连接docker服务器工具都可以连接Docker Swarm

# 实验步骤
# 1. 下载Docker Swarm
# 2. 部署和管理Swarm集群

# 阿里云Docker Hub
$ vim /etc/docker/daemon.json
{
	"registry-mirrors":["https://n6syp70m.mirror.aliyuncs.com"]
}
$ sudo service docker restart

# Swarm概述
Swarm 是 Docker 发布的管理集群的工具，一个集群由多个运行 Docker 的主机组成

Swarm被集群到Docker Engine中 -- swarm mode

# 关键概念
集群由多个运行Docker的主机组成：
两种 -- 管理者，工作者

Node -- 集群中的一个结点

一个服务是任务在管理节点或工作节点执行的定义，
服务中运行的单个容器被称为任务。

堆栈（stack）是一组相互关联的服务，即是一个分布式的应用程序。



# 实验环境搭建 -- 可以替换为本地两台安装有Docker且在同一局域网的主机
1. 创建一个swarm -- Docker1.12后被集成到Docker Engine中
$ docker swarm init --advertise-addr <IP> -- IP本地局域网址
模拟时主机上有多张网卡

$ docker info 查看swarm状态
$ docker node ls 查看有关结点信息

2. 向swarm中添加结点
运行docker swarm init时会输出向swarm中添加结点的命令

获取向swarm添加管理结点和工作结点的命令：
# 管理结点
$ docker swarm join-token manager
# 工作结点
$ docker swarm join-token worker

3. 移除结点
被移除的结点必须状态为down
$ docker node rm NODE -- NODE 为该结点的ID

4. 提权或撤销权限
worker -> manager: $ docker node promote NODE
manager->worker: $ docker node demote NODE



# Docker Compose 与 Docker Swarm
$ docker stack deploy命令-- 使用集群服务
swarm只支持version:3.0版本的docker-compose.yml文件

$ docker stack deploy -c docker-compose.yml app -- 执行compose服务
使用集群 -- 会部署一个堆栈  -- 创建的是服务而不是任务
--运行的是分布式应用程序



# 管理堆栈和服务

# 堆栈
$ docker stack ls --> 查看所有的堆栈

$ docker stack services app -- 查看app这个具体服务

$ docker service ls -- 查看所有的服务
$docker stack ps app -- 查看app堆栈任务
$ docker service ps app_redis -- 查看服务app_redis的任务

$ docker stop d76 -- 手动暂停容器
集群为了任务会自动重启一个容器

$ docker stack rm app --> 移除一个堆栈，将会移除堆栈中所有服务
$ docker service rm app_redis app_wed --> 移除一个或多个服务
# 移除堆栈中所有的服务，堆栈会自动被移除

