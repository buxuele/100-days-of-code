#!/usr/bin/python3
# Time: 2019/04/23 10:42 PM

import requests
import base64
import codecs


username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'
url = f'http://{username}.natas.labs.overthewire.org/'

s = requests.Session()
resp = s.post(url, auth=(username, password), data={"query": "b"})

print(resp.text)
x = requests.utils.unquote(resp.url[60:])
print(x)


# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLof/YMma1yzL2UfjQXqQEop36O0aq+C10FxP/mrBQjq0eOsaH+JhosbBUGEQmz/to=
# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIYiwNnSJY7KHJGU+XjuMzVvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
