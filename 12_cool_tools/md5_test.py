# date: 2019/03/21 8:08 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. 

"""

import hashlib


# 数字加密算法。
def md5_test(someStr):
	# 直接传入也可以，使用 update() 也可以。
	# hash = hashlib.md5(someStr.encode("utf-8"))
	hash = hashlib.md5()
	hash.update(someStr.encode("utf-8")) # 这个必须转为 bytes类型
	return hash.hexdigest() # 使用一个32位的16进制字符串表示。

print(md5_test("hello"))



