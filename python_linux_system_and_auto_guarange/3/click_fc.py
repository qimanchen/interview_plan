#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用click实现类似fc的功能
"""

from __future__ import print_function
import click

message = click.edit()
print(message, end=" ")
