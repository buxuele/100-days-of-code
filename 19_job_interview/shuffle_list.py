# when: 2019/04/04 9:44 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

import random

l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)


# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
a = "k:1 |k1:2|k2:3|k3:4"

s = {}

# a = ''.join(a.split('|'))
a2 = a.split('|')
for i in a2:
    s[i.split(":")[0]] = i.split(":")[1]

print(s)
