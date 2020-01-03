#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试sys.stdin
python read_stdin.py < /etc/passwd # 直接作为输入
"""

from __future__ import print_function
import sys

for line in sys.stdin:
	print(line, end=" ")
