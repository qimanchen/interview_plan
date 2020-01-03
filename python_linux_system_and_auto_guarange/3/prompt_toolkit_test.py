#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
prompt_toolkit
# python版本高于3.6
交互式实现REPL(读取-求值-输出)
prompt # 可以使用bash的一些快捷键
history.FileHistory 可以通过上下键查询历史输入
auto_suggest # 实现历史输入提示
contrib.completers # 实现tab补全命令
"""
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
# from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.completion import WordCompleter

SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete', 'drop'], ignore_case=True)

while True:
	user_input = prompt('SQL>', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(),completer=SQLCompleter)
	print(user_input)