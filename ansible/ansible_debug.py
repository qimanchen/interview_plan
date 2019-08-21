# Ansible调试技巧
"""
ansible-playbook 参数使用

Debug 的使用

Ansible 的安装

Developing Plugins
"""

# 参数
"""
通过：
$ ansible-playbook -h 查看详细的参数列表
or
$ man

# 参数的使用格式
ansible-playbook [options] playbook.yml
"""
# verbose参数
"""
-v
--verbose
-vvv # 更详细的模式， -vvvv启用连接调试

# 选择verbose模式时，会打印出所有模块运行后的变量
# -v 和 -verbose 参数的效果相同
$ ansible-playbook -v test_apache.yaml

$ ansible-playbook -vvv test_apache.yaml
# 更详细的信息
"""

# Debug模块的使用
"""
debug 模块在执行过程中会打印出详细信息，同时还可以用在调试变量或表达式中

debug 模块的使用相对简单，主要参数是 msg （用于调试输出信息）和 
var 变量（需要调试的变量名称，即将任务执行的输出结果作为一个变量传递给 debug 模块）

我们往往会用某个变量来储存某个命令的结果，以备日后访问的使用。
在后面我们会用到 register 这个关键词（注册变量，Registered Variables）来决定将结果存储在哪个变量中。

# testdebug.yaml
---
- hosts: test

  tasks:

     - name: test register
       shell: echo $PATH  # 调用 shell 模块输出路径
...
"""
# 加入debug
"""
---
- hosts: test

  tasks:

     - name: test register
       shell: echo $PATH
       register: test

     - debug: msg={{test}}
...
"""

# Plugins
"""
Ansible 中另一个强大的功能——Plugins（插件）来帮助我们在执行命令后输出一些信息

Plugins 是一种增强 Ansible 核心功能的一段代码，Ansible 提供了一些插件

# 相应内部提供的插件
Action plugins：是模块的前端，在调用模块之前在控制器上执行动作

Cache plugins：用于保存缓存

Callback plugins：能够 hook 到 ansible 的事件，然后用于显示或记录

Connection plugins：定义了如何与 inventory 的主机进行通信

Filters plugins：允许操作 ansible 中的数据，这是一个 jinja2 的功能

Lookup plugins：用于从外部来源获取数据

Strategy plugins：用于控制和执行逻辑的流程

Shell plugins：用于处理 ansible 在远程主机上遇到的不同 shell 的命令和格式

Test plugins：用于验证 ansible 中的数据

Vars plugins：将额外的变量数据用到运行的 ansible 中
"""
# 这些插件可以在/etc/ansible/ansible.cfg可以查看到
# $ sudo vim /etc/ansible/ansible.cfg

# Callback plugins
"""
通过模块就可以解决详尽显示出执行后的信息的问题，同样我们也可以通过这个 Callback 插件来帮助我们显示信息
# 源码
$ git clone https://github.com/n0ts/ansible-human_log.git
将这个文件放置在预定义的插件位置
（/usr/share/ansible/plugins/callback），这里默认没有创建这个文件夹，需要我们自行创建。

$ sudo mkdir -p /usr/share/ansible/plugins/callback
$ sudo mv /home/shiyanlou/ansible-human_log/human_log.py /usr/share/ansible/plugins/callback/human_log.py

这里我们看到会涉及到了 .py 文件，这是因为在 Ansible 的使用中是通过 Python API 来管理节点，
再通过扩展 Ansible 来响应 python 事件，同时也可以通过相应插件（plugins）来调取数据源。
git 下来的 human_log.py 文件正是插件使用的一个 python API。可以用 cat 命令来查看下里面的内容。

Ansile 宣称能够接受任何语言的模块或插件，所以像 C、shell 等只要能够达到需求的语言都可以用来编写一个插件
"""

# Lookup plugins
"""
Lookup plugins 可以用于从外部数据存储中获取数据。

简单的例子来是实现查找插件的功能，需求是查找并返回一个文本文件的内容来作为变量。

"""