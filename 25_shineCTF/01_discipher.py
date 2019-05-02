#!/usr/bin/python3
# Time: 2019/04/30 11:52 AM
# About: 

import base64
import requests

s = requests.Session()
url = "http://files.sunshinectf.org/misc/brainmeat.txt"

resp = requests.get(url)
print(resp.text)

# base64.a85decode
ret = base64.a85decode(resp.text)
print(ret)































