# Docker包含Registry API，Docker Hub API，Docker OAuth API，Docker Remote API

# Docker Remote API可以提供docker命令的全部功能
# Docker API 基本概念与认证
$ docker version | grep "API version" -- 查看api的版本
如果要提供远程访问，需要添加
-H=tcp://0.0.0.0:2375的配置 -- 将Docker守护进程监听到所有的网络接口的2375上

# 配置
$ sudo vim /etc/default/docker
DOCKER_OPTS="-H=tcp://0.0.0.0:2375 -H=unix:///var/run/docker.sock"
后面那个配置允许使用本地访问连接
$ sudo service docker restart

$ docker -H localhost:2375 info -- 查看docker信息
$ export DOCKER_HOST=tcp://localhost:2375
$ docker info -- docker命令连接的是远程api接口

# 使用TLS认证


# 使用Remote API使用方法
GET /info API
curl http://127.0.0.1:2375/info -- > docker info类似的信息
python -mjson.tool 美化一下

POST
$ curl -X POST -H "Content-Type: application/json" \
http://127.0.0.1:2375/containers/create \
-d '{"Image":"redis"}'

若没有镜像可以先拉取




# 使用 API 管理容器：创建，查看，删除等操作

实验需求是查找所有的容器（包含关机状态的容器），显示最后创建的一个，同时返回容器的大小。
接口的三个参数：
	all=1 所有的容器（包含关机状态的容器）
	limit=1 显示最后创建的一个
	size=1 返回容器的大小
GET /containers/json
$ curl http://127.0.0.1:2375/containers/json\?all\=1\&limit\=1\&size\=1
类似于$ docker container ls -a -n 1 -s


# 创建容器
实验需求创建一个 nginx 容器，将容器的 80 端口映射到宿主机 80 端口，挂载宿主机的 /home/shiyanlou/data 目录作为数据卷到容器中的 /data 目录。
POST /container/create
$ curl -X POST -H "Content-Type: application/json" \
http://127.0.0.1:2375/containers/create?name=test_nginx \
-d '{
    "Image": "nginx",
    "HostConfig": {
        "Binds": ["/home/shiyanlou/data:/data"],
        "PortBindings": {"80/tcp": [{"HostPort": "81"}]}
    }
}'
# 删除指定容器
DELETE /containers/(id)
force=1 -- 强制删除
$ curl -X DELETE http://127.0.0.1:2375/containers/9899\?force\=1


# 其他常用接口
docker container inspect：GET /containers/(id)/json
docker container top：GET /containers/(id)/top
docker container logs：GET /containers/(id)/logs
docker container export：GET /containers/(id)/export
docker container start：POST /containers/(id)/start
docker container attach：POST /containers/(id)/attach


使用 API 管理镜像：创建，查看，删除等操作
# 查看所有的镜像
GET /images/json
$ curl http://127.0.0.1:2375/images/json | python -mjson.tool

# 拉取镜像
POST /images/create
$ curl -X POST http://127.0.0.1:2375/images/create\?fromImage\=busybox:ubuntu-14.04
# 删除镜像
DELETE /images/(name)
curl -X DELETE http://127.0.0.1:2375/images/busybox
# 其他接口
docker image inspect：GET /images/(name)/json
docker image tag：POST /images/(name)/tag
docker image push: POST /images/(name)/push
docker image build：POST /build
docker search：GET /images/search


使用 API 管理数据卷：创建，查看，删除等操作
# 创建数据卷
POST /volumes/create
$ curl -X POST -H "Content-Type:application/json" http://127.0.0.1:2375/volumes/create -d '{"Name": "shiyanlou"}'
# 查看数据卷
GET/volumes
$ curl http://127.0.0.1:2375/volumes | python -mjson.tool
# 删除数据卷
DELETE /volumes/(name)
$ curl -X DELETE http://127.0.0.1:2375/volumes/shiyanlou


使用 API 管理网络：创建，查看，删除等操作
# 列出所有的网络
GET /networks
$ curl http://127.0.0.1:2375/networks | python -mjson.tool
# 创建新的网络
POST /networks/create
创建一个新的网络，名字为 shiyanlou，驱动类型为bridge，配置网段为172.10.0.0/16。
$ curl -X POST -H "Content-Type: application/json" \
http://127.0.0.1:2375/networks/create \
-d '{
    "Name": "shiyanlou",
    "Driver": "bridge",
    "IPAM": {"Config": [{"Subnet": "172.10.0.0/16"}]}
}'

连接容器到网络
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:2375/networks/shiyanlou/connect -d '{"Container": "e132d"}'

# 删除网络
DELETE /networks/(id)
# 先断开容器
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:2375/networks/shiyanlou/disconnect -d '{"Container": "e132d"}'

$ curl -X DELETE http://127.0.0.1:2375/networks/shiyanlou
$ curl http://127.0.0.1:2375/networks/shiyanlou