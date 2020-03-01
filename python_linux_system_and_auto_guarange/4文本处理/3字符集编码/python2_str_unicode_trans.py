#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
python2转码辅助函数
str to Unicode
Unicode to str
"""


def to_unicode(unicode_or_str):
	"""转换为unicode"""
	if isinstance(unicode_or_str, str):
		value = unicode_or_str.decode("utf-8")
	else:
		value = unicode_or_str
	return value
	
def to_str(unicode_or_str):
	""" 转换为str"""
	if isinstance(unicode_or_str, str):
		value = unicode_or_str.encode("utf-8")
	else:
		value = unicode_or_str
	return value