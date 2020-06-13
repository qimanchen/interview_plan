#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
import os
import time


# 企业号及应用相关信息
CORP_ID = 'wwc4aeeb2e6b2ef06d'
CORP_SECRET = 'm81zpd9JH4HsBlRn6vSucJB5ZF4vpFPV8zt7lAx0Ncw'
AGENT_ID = 1000002

# access_token 请求地址
ACCESS_TOKEN_REQUEST_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

# 发送应用消息请求地址
SEND_MESSAGES_REQUEST_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send'

# 存储 access_token 文件
ACCESS_TOKEN_FILE = '/tmp/access_token.txt'


# 获取 access_token，并写入文件
def get_access_token():
    get_token_url = '{}?corpid={}&corpsecret={}'.format(ACCESS_TOKEN_REQUEST_URL,
                                                        CORP_ID,
                                                        CORP_SECRET)
    r = requests.get(get_token_url)
    r = r.json()
    access_token = r['access_token']
    with open(ACCESS_TOKEN_FILE, 'w') as f:
        f.write(access_token)
    return access_token


# 从文件获取 access_token
def get_access_token_from_file():
    if os.path.exists(ACCESS_TOKEN_FILE):
        with open(ACCESS_TOKEN_FILE, 'r') as f:
            access_token = f.read()
    else:
        access_token = get_access_token()
    return access_token


# 发送应用消息
def main():
    access_token = get_access_token_from_file()
    i = 0
    while i < 3:
        try:
            message = sys.argv[3]
            # message = '来自python的测试消息'
            send_message_url = '{}?access_token={}'.format(SEND_MESSAGES_REQUEST_URL,
                                                           access_token)
            message_params = {"touser": "@all",
                              "msgtype": "text",
                              "agentid": AGENT_ID,
                              "text": {"content": message},
                              "safe": 0
                              }
            r = requests.post(send_message_url, json=message_params, timeout=5)
            r = r.json()
            if r['errmsg'] == 'ok':
                break
            else:
                access_token = get_access_token()
        except Exception as e:
            print(e)
        i += 1
        time.sleep(2)


if __name__ == '__main__':
    main()
