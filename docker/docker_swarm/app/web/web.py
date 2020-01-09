#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from redis import Redis
"""
该程序会连接redis服务，
在访问页面'/'时，会自动将变量number加1
"""

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	redis.incr('number')
	return 'Hello Shiyanlou! # %s' % redis.get('number')
	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
