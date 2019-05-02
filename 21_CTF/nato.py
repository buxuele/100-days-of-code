# when: 2019/04/10 7:22 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""


from string import ascii_letters, digits
import time
import codecs

h = codecs.encode(b"494-please", "hex")
print(h)

g = codecs.encode((b"%d-admin" % 89), "hex").decode('utf-8')

print(g)
# 3439342d706c65617365
# 3136392d

print("some".encode("utf-8"))