#!/usr/bin/python3
# Time: 2019/04/26 3:19 PM


"""about:
1. 

"""

import requests
import base64
import codecs



#

st = "S4WPnk%2FgAQwVRriZRbKqzIamr4B8Ru1bE%2BPxfqf97Ms%3D"   # cipher   S4WPnk/gAQwVRriZRbKqzIamr4B8Ru1bE+Pxfqf97Ms=
st2 = "d0BKKXcDqp0I3%2BeHnu04vw%3D%3D"                      # vi       d0BKKXcDqp0I3+eHnu04vw==
res = requests.utils.unquote(st)
# print(res)

cipher = "S4WPnk/gAQwVRriZRbKqzIamr4B8Ru1bE+Pxfqf97Ms="
vi = "d0BKKXcDqp0I3+eHnu04vw=="


x = base64.b64decode(cipher)
x2 = base64.b64decode(vi)
print(x)
print(x2)
# y = codecs.decode(x, "hex")


# ss = s.encode('raw_unicode_escape')


# b'K\x85\x8f\x9eO\xe0\x01\x0c\x15F\xb8\x99E\xb2\xaa\xcc\x86\xa6\xaf\x80|F\xed[\x13\xe3\xf1~\xa7\xfd\xec\xcb'
# b'w@J)w\x03\xaa\x9d\x08\xdf\xe7\x87\x9e\xed8\xbf'




