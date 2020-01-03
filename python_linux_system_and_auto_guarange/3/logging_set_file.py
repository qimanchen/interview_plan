#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
logging 日志模块展示
使用loggin.config来读取配置文件
"""

import logging
import logging.config

logging.config.fileConfig('logging.cnf')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')