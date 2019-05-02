#!/usr/bin/python3
# Time: 2019/04/26 7:23 PM
# About: 

import requests
import base64


url = "http://ctf5.shiyanbar.com/web/earnest/index.php"        # 简单的登录问题
s = requests.Session()
data = {"id": "' * LIKE ?", "submit": "Submit"}


#
resp = requests.post(url, data=data)
print(resp.text)
print(s.cookies)


































