# django 问答区项目
# 项目结构
"""

"""

# 创建django项目
# 安装并创建django项目
"""
$ sudo pip3 install Django==2.1.0  
# django1.8.2才可以
$ django-admin startproject community
$ cd community
$ python3 manage.py runserver  -- 可能会出现8000端口已经被占用
"""

# 创建数据库
"""
$ sudo service mysql start # 启动 MySQL 服务器
$ mysql -u root # 进入 MySQL

# 创建数据库
> create database community_db;
"""
# 配置数据库 -- django连接上
"""
# 安装第三方模块支持mysql
$ sudo pip3 install mysqlclient -- 会安装失败

# 解决方案 -- 此方案不行
sudo apt-get isntall libmysqld-dev
sudo pip3 install mysqlclient

# 。。python3.5不支持mysqlclient
# sudo pip3 install PyMySQL

# 注意用sudo权限
apt-get install python3.5-dev
wget https://bootstrap.pypa.io/get-pip.py
python3.5 get-pip.py
pip3.5 install mysqlclient

"""
# 修改 community/community/settings.py
# 数据库设置
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 指定连接 MySQL
        'NAME': 'community_db',        # 刚刚创建的数据库
        'USER': 'root',        # 使用 root 账户
        'PASSWORD': '',        # 因为实验楼环境中的 MySQL 没有密码，所以这里为空
        'HOST': '127.0.0.1',  
        'PORT': '3306',        # MySQL 的固定端口号
    }
}
"""

# 迁移数据库
"""
$ python3 manage.py makemigrations
$ python3 manage.py migrate
"""

# 基础模板分为static静态文件和templates模板两部分
# 静态文件
"""
图片、 CSS 和 JavaScipt

在 Django 中，我们称这些文件为 static files。Django 通过内置的 staticfiles 应用(app)来解决这个问题。

# Django已经将 staticfiles 注册，已存在
INSTALLED_APPS = [
     ...
    'django.contrib.staticfiles',
]

# 定义 STATIC_URL，已存在
STATIC_URL = '/static/'

# 此段代码需自己添加，需添加在文件末尾
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 在根目录中打开终端，输入以下代码，下载必要的静态资源文件。
$ wget http://labfile.oss.aliyuncs.com/courses/1181/static.zip
$ unzip static.zip
"""

# 基本模板
"""
项目以后的页面都将会继承自此模板，这样既能减少代码的编写量，也能增强整个网站样式的统一性

1. 根目录下创建templates文件夹，在此存放模板文件
2. 建一个多语言版的 Django 网站，使用I18N国际化模块来实现，具体意思就是自动根据环境语言来返回相应语言的字段
3. 在模板中导入{% load i18n %}即可，后面只需将需要国际化的文本 替换成{% trans '相应文本' %}
4. 需要导入{% load staticfiles %}使用静态资源文件

$ mkdir templates && cd templates
$ wget http://labfile.oss.aliyuncs.com/courses/1181/base.html

5. 还需要修改community/settings.py中的TEMPLATES,修改其中的DIRS如下：
TEMPLATES = [ { ... 'DIRS': [os.path.join(BASE_DIR, 'templates')], ... ... }, ]
"""

# 创建临时主页面
"""
# 创建一个home应用
$ python3 manage.py startapp home
"""
# 添加应用
"""
首先在community/settings.py中添加home应用:

INSTALLED_APPS = [
     ...
    'home',
]
"""
# 创建视图
"""
在home/views.py中写入如下代码：
from django.shortcuts import render
def home(request):
    """
    主页
    """
    return render(request, 'home/home.html')
"""
# 创建模板
"""
创建home/templates/home/home.html文件，写入以下代码。

{% extends 'home/base.html' %}
在这里我们只是一个展示的作用，所以简单的继承模板就足够了。

在home/templates/home/目录下载base.html文件：

$ wget http://labfile.oss.aliyuncs.com/courses/1181/base.html
"""
# 创建路由
"""
1. 创建home/urls.py文件，写入以下代码：

from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),
]
2. 别忘了在community/urls.py中添加此路由：

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
"""
#!!问题 -- 静态文件不能加载成功
"""
关于django static文件加载异常 -- 404解决方案：

在settings.py文件中添加STATIC_ROOT = 你通用静态文件夹
同时添加STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') or 项目目录下的static files]
关于django 加载css js - 304异常：

由于浏览器自身缓存导致的加载重复的问题
"""
# 完整代码
"""
通过终端下载：
$ wget http://labfile.oss.aliyuncs.com/courses/1181/Community-2.zip
"""