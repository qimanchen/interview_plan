#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
click 模块官方示例
command: 使函数hello成为命令行接口
option: 增加命令行选项
	prompt选项 -- 当命令行没有输入时，会提示用户输入
	default -- 设置命令行参数的默认值
	help -- 参数说明
	type -- 参数类型，string,int,float
	nargs -- 指定命令行接受值的个数
	hide_input -- 隐藏输入
	confirmation_prompt -- 两次输入确认
echo: 输出结果 -- 兼容性较好（python2 python3)
"""

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help="The person to greet.")
def hello(count, name):
	"""
	Simple program that greets NAME for a total of count times.
	"""
	for x in range(count):
		click.echo('Hello %s!' % name)
		
@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
	"""转换成float"""
	click.echo('%s / %s' % pos)
	
@click.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def digest(hash_type):
	"""参数预设范围"""
	click.echo(hash_type)
	
@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def encrypt(password):
	"""输入密码隐藏"""
	click.echo('Encrypting password to %s' % password.encode('rot13'))
	
		
if __name__ == "__main__":
	hello()
