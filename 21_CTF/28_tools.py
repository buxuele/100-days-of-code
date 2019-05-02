#!/usr/bin/python3
# Time: 2019/04/23 10:56 PM


"""about:
1. 

"""



import requests
import base64



a = 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLof%2FYMma1yzL2UfjQXqQEop36O0aq%2BC10FxP%2FmrBQjq0eOsaH%2BJhosbBUGEQmz%2Fto%3D'

b = requests.utils.unquote(a)

c = repr(base64.b64decode(b))
print(c)