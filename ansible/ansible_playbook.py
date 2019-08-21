# ansible playbook实战

# 自动化运维中批量进行系统配置和部署服务才是自动化的核心用法
"""
Playbook 介绍

YAML 语法格式

Playbook 语法结构

Ansible 模块介绍

Playbook 执行控制

Playbook 示例
"""

# playbook介绍
"""
Playbook 是一种非常简单的配置管理系统以及是多机器部署系统的基础

Playbook 还可以用于声明配置，以及编排有序的执行过程，
使得在多组机器之间有序的执行指定步骤，或者同步或异步的发起任务

Playbook 也是一个任务列表，这个列表中的可以包含一个或者多个 plays

它与 AD-HOC 最大的不同之处就在于它是把这些任务放在源码中进行控制
"""

# YAML语法格式
"""
 Ansible 官方默认使用 YAML 这种格式来书写 Playbook
 
 对于 Ansible 来说，几乎每个 YAML 文件都以一个列表开始。
 列表中的每个项都是 key/value 对的列表，通常称为 Hash 或 Dictionary

"""
# YAML格式说明
"""
文件均以 --- 作为开始，以 ... 结束

列表中同级别的项使用相同缩进以及短横线加空格（-）开始

字典（dictionary）用 key: value 的简单形式表示，其中冒号后面必须有个空格。
value 部分可以用几种形式（yes/no/true/false）来指定布尔值

换行符：value 部分还可以使用 | 或 >，使用 | 可以将内容进行分行处理，
而使用 > 将忽略换行符，任何情况下缩进都会被忽略。

语句过长可以使用 "" 括起来，
例如：foo: "somebody said I should put a colon here: so I did"。
"""

# playbook语法结构
"""
play 的内容也被称为 task （任务），执行一个任务就是对模块的调用。
"""
#示例
"""
---
- hosts: test
  remote_user: root
  vars:

  tasks:
   - name: Install the package "bc"
      apt:
        name: bc
        state: present
  handlers:
...
"""
# 参数对应说明
"""
1. 主机和用户（hosts）
hosts 参数表示一个或多个组或主机，多个时用逗号分隔。
remote_user 表示用户名，这里还可用 sudo: yes 来表示使用 sudo 的权限执行操作。

2. vars - 变量
在任务行中可以使用变量来定义，像这样 "{{item}}" 括起来。
将变量独立出来，可以方便后期的修改和维护等，也可以在其他任务中使用

变量的定义可以放在如下几处：
	Inventory 中
	全局中（var:）或者某个任务（task）中
	在 roles 结构中用于存放单独的文件
	在 registered 模块中注册变量，主要用于调试和判断
	
3. tasks - 任务
在运行 playbook 时是从上到下依次执行，
并且一个 task 在其对应的所有主机上执行完毕之后才会执行下一个 task。
如果一个 host 执行 task 失败，那么这个 host 将会从整个 playbook 的 rotation 中移除。
如果发生执行失败的情况，需要修正 playbook 中的错误，然后再重新执行

！！！
每一个 task 必须有一个 name，这样在输出任务时才可以清楚地辨别出属于哪个任务，
若没有定义将会被特定标记。

4. handlers
Handlers （可选项）和一般的 task 没有什么区别，也是一个列表项，
只是通过名字来对它进行引用。Handlers 是由通知者进行 notify，
如果没有被通知handlers 不会被执行，不管有多少个通知者进行了 notify，
等到所有 task 执行完成之后，handlers 也只会被执行一次。同时 handlers 也会按照声明的顺序执行。

!!!
Handlers 最佳的应用场景是用来重启服务，或者触发系统重启操作，除此以外很少用到了。
"""

# Ansible模块
"""
Ansible 的模块（modules），也被称为 task plugins 或者 library plugins，是在 Ansible 中真正进行实际工作方式，在每个任务中执行相应的内容。

模块（modules）具有幂等性，即在一个序列中多次运行一个模块和运行一次的效果相同，
因而重复多次执行 playbook 也会是安全的。
"""

# 几个常用的模块
# service模块
"""
这是一个比较基本的模块定义，主要用于管理服务 -- 用 key=value 这种参数格式来书写

# 开启服务
- name: make sure apache is running
    service: name=httpd state=started

# 也可以用下面这种 key：value 参数格式来书写
- service:
    name: httpd
    state: started
"""
# shell模块
"""
shell 模块（和 command 模块）是唯一不会使用 key=value 参数格式的模块，它们只取得参数的列表。

# 安装一个程序
- name: make install gucad
      shell: ./configure --with-init-dir=/etc/init.d && make && make install && ldconfig && update-rc.d guacd defaults
      args:
          chdir: /home/ubuntu/src/guacamole-server-0.9.9/
		  
shell 命令中大多数的常用命令已经被做成了一个模块，可以直接使用而不用采用 shell 命令来执行，
只是有些命令的参数还未完全转化成模块，这种情况下才采用 shell 模块来实现

# 在 Ubuntu 中我们常用的命令像 apt-get update、apt-get install 这样的命令，
以及创建文件（file）和复制文件（copy）这些命令操作都是有专门的模块来实现，
"""
# 指定目录下创建一个文件
"""
#  在指定目录下创建一个文件，并赋予权限
- name: create a file
    file:
         path: /home/shiyanlou/file
         state: touch
         owner: shiyanlou
         mode: 'u+rw,g+rw'
"""
# 复制一个文件到指定目录
"""
# 复制一个文件到指定目录
  - name: copy a file
    copy:
         src: /etc/ansible/ansible.cfg
         dest: /home/shiyanlou/file
"""
# 安装一个软件包
"""
# 安装一个软件包
- hosts: test
  sudo: yes
  vars:
      apt_packages_ca:
         - apt-transport-https
         - ca-certificates
         - apparmor-utils

  tasks:
    - name: add CA certificates are installed.
      apt:
          name: "{{ item }}"
          update_cache: yes
      with_items: apt_packages_ca
"""

# Playbook执行控制
# 条件
"""
通常一个任务的结果会取决于变量的值、事件、或者之前任务的结果，然后通过某些条件是否满足来判断如何控制执行。

tasks:
    - shell: echo "This certainly is epic!"
      when: epic
when 语句在这里作为一个条件来进行判断执行。
"""
# when语句
"""
有时可能会需要某个主机跳过某个特定的步骤，这时使用 when 子句就很容易实现了，其中包含没有花括号的原始 Jinja2 表达式

# Jinja2的 defined命令
tasks:
        - shell: echo "I've got '{{ foo }}'"
          when: foo is defined

        - fail: msg="Bailing out. this play requires 'bar'"
          when: bar is not defined
"""
# 循环语句
"""
playbook 也有标准循环、嵌套循环、哈希循环、Do-Until 循环等等 -- http://docs.ansible.com/ansible/latest/playbooks_loops.html
"""
# 标准循环
"""
# 添加多个用户
- name: add several users
  user:
    name: "{{ item }}"
    state: present
    groups: "shiyanlou"
  with_items:
     - testuser1
     - testuser2
	 
item：用于放置需要读取的变量的位置
with_items：用来指定需要读取出来的值

# 等价于
- name: add user testuser1
  user:
    name: "testuser1"
    state: present
    groups: "shiyanlou"
- name: add user testuser2
  user:
    name: "testuser2"
    state: present
    groups: "shiyanlou"
"""
# 嵌套循环
"""
- name: give users access to multiple databases
  mysql_user:
  name: "{{ item[0] }}"
  priv: "{{ item[1] }}.*:ALL"
  append_privs: yes
  password: "shiyanlou"
  with_nested:
    - [ 'Jay', 'Chou' ]
    - [ 'studentdb', 'coursedb', 'classdb' ]
"""

# playbook控制方式
"""
# 操作步骤
1. 编写一个 yaml 的 playbook 文件：vim *.yaml
2. 使用 ansible-playbook 命令执行即可：ansible-playbook *.yaml
"""

# 简单的尝试
"""
---
- hosts: test

  tasks:
      - name: test condition
        command: echo {{ item }}
        with_items: [ 0, 2, 4, 6, 8, 10 ]
        when: item > 5
...

when：列出判断的条件，条件为真则执行命令，为假则 skipping 略过

# 显示结果
shiyanlou:~/ $ ansible-playbook test.yaml                            [16:58:26]

PLAY [test] ********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [127.0.0.1]

TASK [test condition] **********************************************************
skipping: [127.0.0.1] => (item=0) 
skipping: [127.0.0.1] => (item=2) 
skipping: [127.0.0.1] => (item=4) 
changed: [127.0.0.1] => (item=6)
changed: [127.0.0.1] => (item=8)
changed: [127.0.0.1] => (item=10)

PLAY RECAP *********************************************************************
127.0.0.1                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
"""
# !!! 格式注意，缩进不能是tab，而是空格

# playbook示例
"""
安装Apache2服务并启动
"""
# 安装脚本
"""
#!/bin/bash

# install apache2
apt-get install apache2

# start-up apache
service apache2 start
"""
# playbook
"""
# 不要用tab
---
- hosts: test
  sudo: yes

  tasks:
    - name: "Install Apache"
      apt:
        name: apache2
        state: present
    - name: "Startup Apache"
      service:
        name: apache2
        state: started
        enabled: yes
...

$ sudo vim test_apache.yaml
$ ansible-playbook test_apache.yaml
"""

# 通过playbook安装dockers
"""
---
- hosts: test # 对 test 组执行下面的任务
  sudo: yes  # 下面的任务将有 sudo 的执行权限
  vars:      # 定义一个变量，安装多个包，以免增加多个类似的代码
      apt_packages_ca:
         - apt-transport-https
         - ca-certificates

  tasks:    # 定义任务列表

    - name: add docker source list file for  install docker
      file:
          path: /etc/apt/sources.list.d/docker.list
          state: touch
          owner: root
          mode: 'u+r,g+rw'

    - name: write deb url of docker to docker.list
      blockinfile:
          dest: /etc/apt/sources.list.d/docker.list
          marker: ""
          block: |
            deb https://apt.dockerproject.org/repo ubuntu-trusty main

    - name: add CA certificates and ensure installed
      apt:
          name: "{{ item }}"
          update_cache: yes
      with_items: "{{ apt_packages_ca }}"

    - name: add apt-key of dockers
      apt_key:
          keyserver: p80.pool.sks-keyservers.net
          id: 58118E89F3A912897C070ADBF76221572C52609D

    - name: install docker-engine
      apt:
          name: docker-engine
          state: latest
          force: yes
...
"""



