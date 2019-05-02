#!/usr/bin/python3
# Time: 2019/04/24 8:21 PM

import base64
# from pwn import *

p = base64.b64decode("S1JZUFRPTklTR1JFQVQ=")
h = p.decode("utf-8")

g = str(p, "utf-8")

print(p, "type: ", type(p))
print(h, "type: ", type(h))

print("g:  ", g, type(g))

# username = 'krypton1'
# password = 'KRYPTONISGREAT'
# host = 'krypton.labs.overthewire.org'
#
# shell = ssh(host=host, user=username, password=password)
# log.info("username: %s" % shell.whoami())
# log.info("pwd: %s" % shell.pwd())