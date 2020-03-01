#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
输入交互进行判断的写法
"""

if __name__ == "__main__":
	yes_or_no = input('please input yes or no:')
	if yes_or_no.lower() == "yes":
		print("continue do something")
	else:
		print("exit...")