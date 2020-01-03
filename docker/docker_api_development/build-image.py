import docker
import os
import sys

# 初始化Client对象
client=docker.DockerClient(base_url='tcp://127.0.0.1:2375')

# 处理逻辑
# 判断是否输入了两个参数
if len(sys.argv) != 3:
	print "Parameter ERROR:args number"
	sys.exit()
	
# 判断第一个参数是否为路径，并且判断路径中是否存在Dockerfile
# 如果存在则创建镜像，若不存在则报错
if os.path.isdir(sys.argv[1]):
	dockerFile = os.path.join(sys.argv[1], 'Dockerfile')
	if os.path.exists(dockerFile):
		# 调用创建镜像的API
		imgae=client.images.build(path=sys.argv[1],tag=sys.argv[2])
		# 打印镜像信息
		print(image)
		# 列出所有镜像
		print(client.image.list())
else:
	print("build error, not found Dockerfile")
