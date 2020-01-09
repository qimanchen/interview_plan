#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用sys.stdout，sys.stderr输出
分别对应着shell中标准输出和标准错误输出
"""
import sys


sys.stdout.write('hello')
sys.stderr.write('world')