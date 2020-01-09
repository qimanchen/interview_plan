#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sys.stdin.readlines()
一次性读入全部的内容，并读取到一个列表中
"""

from __future__ import print_function
import sys


def get_content():
	return sys.stdin.readlines()

	
print(get_content())