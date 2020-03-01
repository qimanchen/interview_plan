# Jinja2模板
	模板有效将业务逻辑和页面逻辑分离，可读性，理解和维护
	渲染
		模板中使用占位符表示动态部分
		结合上下文才会响应
		实例
			from string import Template
			s = Template('$who is a $role')
			s.substitute(who='bob',role='teacher')
Jinja2语法入门
	- Jinja2是Flask的一个依赖
		单独安装Jinja2 - $ pip install jinja2
	- 语法块
		Jinja2使用大括号的方式表示Jinja2语法
		Jinja2中存在三种语法
			控制结构 {% %}
				{% if users %}
					<ul>
					{% for user in users %}
						<li>{{ user.username }}</li>
					{% endfor %}
					</ul>
				{% endif %}
			变量取值 {{}}
			注释 {# #}
	- 变量
		字典 {{ mydict['key'] }}
		列表 {{ mylist[3] }}
		列表索引 {{ mylist[myintvar] }}
		对象方法调用 {{ myobj.somemethod() }}
	- Jinja2中的过滤器
		内置函数和字符串处理函数
		过滤器文档
			http://jinja.pocoo.org/docs/2.9/templates/#builtin-filters
		过滤器
			safe 过滤时不转义
			capitalize 值的首字母转换成大写，其他字母转换成小写
			lower 值转换成小写
			upper 值转换成大写
			title 每个单词的首字母大写
			trim 把值得首尾空格去掉
			striptags 去掉所有HTML标签
			join 拼接多个值为字符串
			repalce 替换字符串的值
			round 数字四舍五入
			int
		过滤器与变量使用管道分割，多个过滤器可以链式使用
			{{ "Hello World" | replace("Hello", "Goodbye") }}
			{{ "Hello World" | replace("Hello", "Goodbye") | upper }}
			{ 42.55 | round } -> 43.0
			{{ 42.55 | round | int }} -> 43
	- Jinja2的控制结构
		{% if % }
		{% elif %}
		{% else %}
		{% endif %}
	- Jinja2 for循环
		{% for user in users %}
		{% endfor %}
		
		- for循环中的特殊变量
			loop.index 当前循环迭代次数，从1开始
			loop.index() 党店迭代次数，从0开始
			loop.revindex
			loop.revindex() 到循环结束的次数
			loop.first 是否为第一迭代
			loop.last 是否为最后一次迭代
			loop.length 序列中的项目数
			loop.cycle 在一串序列间取值的辅助函数
			
			- 实例
				{% for key, value in data.iteritems() %}
					<tr class="info">
						<td>{{ loop.index }}</td>
					</tr>
				{% endfor %}
	- Jinja2的宏
		将行为抽象成可重复调用的代码块
		- 声明宏实例
			{% macro input(name, type='text', value='') %}
				<input type="{{ type }}" name="{{name}}" value="{{value}}">
			{% endmacro %}
		- 宏的调用实例
			<p>{{ input('username', value='user' }}</p>
	- Jinja2的继承和super函数
		最强大的功能 - 模板的继承
		{% block head %}
		{% endblock %}
		
		继承，{% extends "base.html" %}
	- Jinja2的其他运算
		- 定义变量
			算数操作
				+-*/ // % * **
			比较操作
				== != > >= < <=
			逻辑操作
				not and or
	- Jinja2实战
		Jinja2管理配置文件
			Environment类 - 用于存储配置和全局对象，从文件系统或其他位置加载模板
			
			- 配置Jinja2为应用加载文档
				from jinja2 import Environment, PackageLoader
				在yourapplication这个python包的templates目录下查找模板
				env = Environment(loader=PackageLoader('yourapplication', 'templates'))
				
				使用模板名称为参数调用 Environment.get_template，返回一个模板
				template = env.get_template('mytemplate.html')
				print(template.render(the='variables', go='here'))
				
				通过文件系统加载
					import os
					import jinja2
					def render(tpl_path, **kwargs):
						path, filename = os.path.split(tpl_path)
						return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)
				