#!/usr/bin/python3
# Time: 2019/05/03 8:57 PM
# About: 


x = "\x89<S\x9a\x84\xe6\xc9j\xcf_,\xee\xa2\xad\x9e\xf7\xbe\x89U\x80"
print(x)

y = x.encode("raw_unicode_escape")
print(y)

z = y.decode()
print(z)





























