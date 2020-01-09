#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
logging 日志模块展示
"""

import logging

# 表示记录 logging Info级别及以上的日志
# logging.basicConfig(filename='app.log', level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s : %(levelname)s : %(message)s',
filename='app.log')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')