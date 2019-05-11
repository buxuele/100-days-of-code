#!/usr/bin/python3
# Time: 2019/05/03 8:35 PM
# About: 

import codecs

s = "893c539a84e6c96acf5f2ceea2ad9ef7be895580"
s2 ="ok"

res = codecs.decode(s, "hex")
print(res)
print(type(res))

x = "\x89<S\x9a\x84\xe6\xc9j\xcf_,\xee\xa2\xad\x9e\xf7\xbe\x89U\x80"
print(x)





























