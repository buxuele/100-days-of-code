#!/usr/bin/python3
# Time: 2019/04/24 7:38 PM


import requests
import base64
import urllib
import codecs

from string import ascii_letters, digits


username = 'buxuele'
password = 'p9c6vQZXHTF3z7p'

url2 = "http://ctf5.shiyanbar.com/web/jiandan/index.php"        # 简单的登录问题


s = requests.Session()
data = {"id": "200"}

# 'or 1=1 ;--
print("=="*50)
for i in range(5):
    resp = s.post(url2, data=data)
    print(resp.text)

    print(s.cookies)

    # LXER7XeN%2BdEor5Sjx0Dp5P55fRS6NHVDfuKz16Ava%2Bk%3D
    # kfKq9JrroKiUt6QcGA8OxQ%3D%3D

    cipher = base64.b64decode(requests.utils.unquote(s.cookies["cipher"]))
    iv = base64.b64decode(requests.utils.unquote(s.cookies["iv"]))

    print(cipher)
    print(iv)
    print("*"*100)
