#!/usr/bin/python3
# Time: 2019/04/30 12:30 PM
# About: learn how to use pwn-tool

from pwn import *


# nc archive.sunshinectf.org 19004
conn = remote("archive.sunshinectf.org", 19004)


print(conn.recvline())
conn.send("39")
print(conn.recvuntil(' ', drop=True))



conn.close()




























