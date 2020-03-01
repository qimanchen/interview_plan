#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取HTML页面中所有超链接
"""
import re
import requests

r = requests.get('https://news.ycombinator.com/')

re.findall('"(https?://.*?)"', r.content)
