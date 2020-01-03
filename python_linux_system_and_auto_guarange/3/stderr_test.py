#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用sys.stderr作为错误输出
sys.exit()返回非零值
"""

import sys


sys.stderr.write('error message')
sys.exit(1)