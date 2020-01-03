Python生态工具

2.1 Python内置小工具
	# 下载服务器
		在指定目录下执行
			$ python -m SimpleHTTPServer # 启动一个下载服务器
			python3
			$ python3 -m http.server
			# 默认打开的是8000端口
		然后可以通过浏览器访问：IP:Port
		# 注：如果当前目录下存在index.html，则显示的是该文件的内容，否则显示的是对应目录内的文件列表

		# 指定端口和IP
		$ python3 -m http.server [-h] [--cgi] [-b Address] [port]
		--cgi 运行一个CGI服务器

	# 字符串转JSON
		$ echo '{"job": "developer", "name": "lmx", "sex": "male"}' | python -m json.tool
		# 转换结果
		{
			"job": "developer",
			"name": "lmx",
			"sex": "male"
		}

		# 同样该工具会将其转化结果进行对齐和格式化
		$ echo '{"address": {"province": "zhejiang", "city": "hangzhou"}, "name": "lmx", "sex": "male"}' | python -m json.tool
		# 结果
		{
			"address": {
				"city": "hangzhou",
				"province": "zhejiang"
			},
			"name": "lmx",
			"sex": "male"
		}
	
	# 验证第三方库是否正确安装
		$ python -c "import paramiko" # 更容易放到shell脚本中集群执行
		
2.2 pip高级用法
	$ sudo apt-get install python-pip # 安装pip
	$ python -m pip install --upgrade pip # 升级pip安装包
	
	# pip介绍
		pip提供安装，卸载，显示安装列表
		pip很好支持虚拟环境
		pip可以通过requirements.txt集中管理依赖
		pip能够处理二进制格式（.whl)
		pip是先下载后安装，如果安装失败，也会清理干净，不会留下一个中间状态
	
	# python源码安装包
		$ git clone https://github.com/paramiko/paramiko.git
		$ cd paramiko
		$ python setup.py install
	
	# pip常用命令
		$ pip command
		install # 安装软件包
		$ pip install flask==version
		download # 下载安装包
		uninstall # 卸载安装包
		freeze # 按照requirements格式输出安装包，pip install -r requirements.txt直接安装软件
		list # 列出当前系统中安装的pip包
		show # 查看安装包完整的信息
		check # 检查安装包的依赖是否完整
		search # 查找安装包
		wheel # 打包软件到wheel格式
		hash # 计算安装包的hash值
		completion # 生成命令补全配置
			$ pip completion --bash >> ~/.profile
			$ source ~/.profile
		help # 获取pip和子命令的帮助信息
	
	# 加速pip安装的技巧
		pypi.python.org不稳定 -- 主要原因因为网络不稳定
		
		# 使用豆瓣或阿里云的源加速软件安装
			pip install -i https://pypi.douban.com/simple/ flask
			
			# 更改镜像，linux -> ~/.pip/pip.conf
			# 这一设置对所有pip有效
				[global]
				index-url = https://pypi.douban.com/simple/
		
		# 将软件下载到本地
			针对大批量的服务器安装软件包 -- 脚本部署大量的服务器
			
			# 下载到本地
				$ pip install --download=`pwd` -r requirements.txt ??有问题
				$ pip download [-d dir] -r requirements.txt
			# 本地安装
				$ pip install --no-index -f file://`pwd` -r requirements.txt
			
2.3 Python编辑器
	Windows - PyCharm
	Linux - vim
	
	# 编写Python的vim插件
		a. 一键执行
			见配置文件 vim_f5.txt
		
		b. 代码补全插件snipmate
			
		c. 语法检查插件Syntastic
		
		d. 编程提示插件jedi-vim
			先安装jedi $ pip install jedi
			
	# Windows 下Python编辑PyCharm介绍
		
2.4 Python编程辅助工具
	# Python交互式编程	
		$ python -- exit() 退出
	# IPython
		IPython4.0 = Ipython shell + jupyter
		
		$ sudo apt-get install ipython
		$ ipython
		# <tab>补全命令
		# 高亮
		# 更好的获取帮助信息
		
		在IPython下
			$?os.path.is*
			$json.dump? # 通过q退出帮助界面
			# 使用两个？？获取更详细的信息
		# 获取对象的定义
			$ %pdef json
		# 获取对象的文档
			$ %pfile json.dump
		# 获取对象的文件
			$ %pdoc json.dump
			$ %pinfo json -- 用处较大
	
	# magic函数 -- Ipython中以%开头的函数
		提供增强的功能，与操作系统交互，操纵用户的输入和输出，以及对Ipython的配置
		
		%<tab> or %lsmagic 获得所有magic的方法
		%save? # 了解save这个magic函数的帮助信息
		
		magic函数分为三类：
			a. 操作代码：%run %edit %save %macro %recall
			b. 控制IPython的magic函数：%colors 等
			c. 其他magic：%load %paste 等
			
	# 保存历史
		_i _ii _iii分别保存了最近三次的输入
		_,__,___最近三次输出
		# bash
		ctrl+p,ctrl+n查找输入
		ctrl+r反向查找
		
		下次进入可以查找前一次会话的记录历史
		%edit 编辑历史输入，并重新执行
		%save 将IPython中的代码保存到程序文件中
		%return 指定代码行数重新运行
		%macro 将重新运行的代码定义为宏，反复重新运行
	
	# 与操作系统交互
		IPython中
			!cmd -- 执行linux指令
			%cd %pwd -- 执行linux中cd和pwd
			
	# jupyter的使用
		$ pip install jupyter
		# linux下无图形界面时的设置
		jupyter notebook --no-brower --ip=0.0.0.0
		
		输入框 -- cell
		ctrl+enter ->执行cell中的代码
		shift+enter-> 执行当前cell中的代码
		
		jupyter进行编程教学和幻灯片演示，支持富文本和markdown格式
		pip install matplotlib # 绘图支持
		
2.5 Python调试器
	python标准库自带的pdb和开源的ipdb
	
	# 标准库的pdb
		进入pdb的方式
			a. $python -m pdb test_pdb.py # 命令执行时进入
			b. 在.py文件中输入：pdb.set_trace()方法
			
	# 开源的ipdb
		语法高亮
		tab补全
		$ pip install ipdb
		
2.6 python代码规范检查
	PEP8一些规范
		import 一行一个
		三个分组
			标准库，第三方库，当前应用程序库
		显示相对导入
			from . import sibling
			
	# 使用pycodestyle检查代码规范
		$ pip install pep8
		$ pip install pycodestyle
		# $ pycodestyle --first optparse.py
		# --show-source 显示不规范的源码
		$ pycodestyle --show-source --show-pep8 *.py # 会查到调用包内部的代码格式检查
	
	# 使用autopep8将代码格式化
		$ pip install autopep8
		$ autopep8 --in-place *.py
		
2.7 Python工作环境管理
	python版本管理，软件包管理
	
	# pyenv
		a. 安装
			$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
			# 配置 
			# 最好配置在 .bashrc
			$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
			$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
			$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
			#使得配置生效
			$ source ~/.bash_profile
			#验证
			$ pyenv --help
			
		b. 使用
			pyenv install --list # 查看当前pyenv支持的python版本
			
			# pyenv安装不同的python版本
			$ pyenv install -v 3.6.0
			# 指定下载源，指定版本
			v=3.5.2|wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/;pyenv install $v
			$ pyenv install -v 2.7.13
			
			# 安装出错：not avaliable zlib - 缺少依赖
			# centos
			$ sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
			# ubuntu
			$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev l
			ibncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
			
			# 查看当前系统中包含的python版本
			$ pyenv versions
			
			# 选择相应的版本
			$ pyenv global 3.6.0
			
			# 删除python版本
			$ pyenv uninstall 2.7.10
			
	# virtualenv管理不同的项目 -- 用的库的版本不同
		如果组合使用pyenv，需要安装pyenv-virtualenv插件，而不是通过virtualenv软件进行使用
		
		a. pyenv-virtualenv
			$ git clone https://github.com/yyuu/pyenv-virtualenv.git $(pyenv root) /plugins/pyenv-virtualenv
			$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
			$ source ~/.bash_profile
			$ pyenv help virtualenv
			
		b. 使用
			# 新建工作环境
			$ pyenv virtualenv 2.7.13 first_project
			$ pyenv virtualenv 2.7.13 second_project
			
			# 查看工作环境
			$ pyenv virtualenvs
			
			# 进入工作环境
			$ pyenv activate first_project
			
			# 退出工作环境
			$ pyenv deactivate
			
			# 删除虚拟环境
			pyenv virtualenv-delete first_project
			