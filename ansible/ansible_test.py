# ansible自动化工具实验
# Ansible 是一款基于 python 开发，能够实现了批量系统配置、程序部署、运行命令等功能的自动化运维工具
# 真正实现部署功能的是运行的模块

# Ansible 主要有两种类型的服务器：控制机器和节点
# 通过 SSH 进行管理
# 控制机通过 inventory 来描述节点的位置
# 并以标准输出的 JSON 协议进行通信

# 特点
# 维护简单，开发库多
# 通过ssh管理，不需要客服端和服务端
# playbook不用分发到远端
# playbook使用的jinja2 -- 简单易学
# 基于模块开发，易于拓展（模块可以用任何语言编写），通过json协议通信
# 开源软件

# 安装
"""
1. 需要更新软件包的信息以及安装通用的管理软件库的工具（software-properties-common）
$ sudo apt-get update
$ sudo apt-get install software-properties-common

2. 通过 add-apt-repository 命令来添加 ansible 的源，将 PPA 添加到系统中去
# ppa - 个人软件包档案，ubuntu launchpad提供的源服务，允许个人上传软件源代码，二进制deb软件包
$ sudo python3.4 /usr/bin/add-apt-repository ppa:ansible/ansible -- 添加ansible的源
# 注意
由于 python 升级之后使用 add-apt-repository 会报错（ImportError：No module named 'apt_pkg'），
这是因为在 /usr/lib/python3/dist-packages 中 apt_pkg 的连接只有 python3.4，
所以为了避免因为版本的问题这里我们就特别的指定 python 的版本信息

3. 更新软件包，以了解ppa中的可用包，接着安装ansible软件
$ sudo apt-get update
$ sudo apt-get install ansible

4. 验证版本
$ ansible --version
Ansible 安装完成后，不会添加数据库，也不会有守护进程启动或继续运行。
你只需要把它安装在至少一台机器上，它可以从该中心点来管理远程机器了
"""

# SSH
"""
在和远程主机通信时，Ansible 默认假设使用 SSH 密钥，
在需要时可以使用 ansible 命令的参数 --ask-pass 来进行密码认证。
$ ansible --ask-pass
"""

# Inventory
"""
Ansible 能够同时对单台或多台机器亦或部分机器操作是通过 Inventory 来实现的， 
Inventory 默认保存在 /etc/ansible/hosts 配置文件中，
而 Ansible 通过这个文件就可以知道要追踪的服务器了。

# 编辑打开配置文件
$ sudo vim /etc/ansible/hosts

 Inventory 中列出我们需要操作的机器，可以单纯的列出这些主机，
 但是推荐有条理地为他们分组，这样在使用时就可以只对其中的某组操作
 
 Inventory 文件可以有多种不同的格式（如：INI、YAML 等），
 具体要取决于相应的插件，这里我们举几个 Ansible 的默认格式（INI）的示例
"""
 # 配置示例
 """
 # 1.常用主机（IP 地址）分组，标题是组名，用于分类系统和决定系统的控制等，可以有一台或多台。
[test]
127.0.0.1
foo.example.com

# 2.分组后添加对该组机器的登录用户和验证方式。添加主机和用户名以及私钥文件。
[dev_test]
192.168.42.3 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=/path/of/keyfile

# 3.不使用分组，采用文件别名的方式。通过端口及主机来描述。
Alias ansible_host=192.168.1.50 ansible_port=6666
"""
# 测试示例
"""
在配置文件 /etc/ansible/hosts
添加
[test] --组
127.0.0.1 ansible_ssh_user=shiyanlou ansible_ssh_pass=666666
在 Asible 中并不推荐将 SSH 登录密码以文本形式存储在 Inventory 中的方式。
但是此处使用只是因为本实验环境中的密码容易输入错误，避免后续可能出现的一些常见错误
"""
# Inventory参数
"""
常见配置参数
主机连接：
ansible_connection 连接到主机的类型，任何可能的连接插件名称，例如，SSH 协议类型中有：ssh、smart 或 paramiko 。

一般连接：
ansible_host 要连接的主机名称。
ansible_port ssh 端口号。
ansible_user 默认 ssh 用户名。

具体的 SSH 连接：
ansible_ssh_pass ssh密码
ansible_ssh_private_key_file 由 ssh 使用的私钥文件。
"""

# AD-HOC
"""
ad-hoc ：临时命令，是在输入内容后，快速执行某些操作，但不希望保存下来的命令

 Ansible 主要是通过模块来实现各种功能的
"""
# 实际操作
"""
# /etc/ansible/hosts -- 中ansible_ssh_pass的密码要正确
# 对test分组执行命令
$ ansible test -m ping

# 可能出现failed错误
主要原因是 ssh 连接时需要检查验证 HOST KEY ，
可在 ssh 连接命令中使用 -o 参数将 StrictHostKeyChecking 设置为 no 来临时禁用检查。
如果要保存设置，可修改 Ansible 配置文件，
将 /etc/ansible/ansible.cfg 中的 host_key_checking 的注释符删除即可

# 对所有机器执行命令
$ ansible all -m ping
"""
# 命令格式
"""
ansible 主机名称/组名 -m 模块名 -a "模块参数" 其他参数
"""
# 示例
"""
$ ansible all -m setup 查看setup模块中所有我们需要操作的机器的信息

# 执行命令让操作的机器输出 Hello shiyanlou
$ ansible test -a "/bin/echo Hello shiyanlou"

# 执行命令让 test 组中的主机在指定目录下创建文件，并设置权限
$ ansible test -m file -a "dest=/home/shiyanlou/file state=touch mode=777"

"""

# 说明
"""
Ansible 提供了很多的模块，还可以创建文件和文件夹、修改文件内容、创建用户、
从源代码管理部署、管理软件包等操作。
更多的模块及操作大家可以参考 Ansible 官方文档中的模块章节。
http://docs.ansible.com/ansible/latest/list_of_all_modules.html
"""
"""
不过对于使用 shell 操作在 Ansible 中没有相应的模块支持的操作时，
我们可以尝试的解决办法是直接使用 shell 模块来执行命令即可

$ ansible test -m shell -a "free -m"
"""

# AD-HOC返回类型
"""
success：这个结果表示操作成功，其中有两种情况，
第一种情况是当执行一些查询的简单操作并且不需要修改内容时，表示该操作没问题；
第二种情况就是当这个操作曾经执行过再执行时就会直接表示成功。

changed：true 这样的结果表示执行的一些修改操作执行成功，
如上文的创建了一个文件，或者修改了配置文件，
复制了一个文件等等这类的操作就会有这样的结果。

failed：这样的结果表示这个操作执行失败，可能是密码错误，参数错误等等，
具体看提示中的 msg 的值。并且在 playbook 中会有多个任务，
中间的某个任务出现这样的情况都不会继续往下执行。（playbook 会在后续的试验中详细讲解）
"""
