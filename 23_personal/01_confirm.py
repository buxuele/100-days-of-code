#!/usr/bin/python3
# Time: 2019/04/30 10:59 AM
# About: 


import requests


url1 = "http://ctf5.shiyanbar.com/10/upload/step1.php"
url2 = "http://ctf5.shiyanbar.com/10/upload/step2.php"
# resp = requests.post(url + '', data={})
s =requests.Session()


resp = requests.post(url1, data={"emailAddress": "admin@simplexue.com"})
print(resp.text)
print("***"*20)
print(s.cookies)
print("***"*20)

resp2 = s.get(url2, allow_redirects=False)
print(resp2.text)
print("***"*20)
print(s.cookies)
print("***"*20)




























