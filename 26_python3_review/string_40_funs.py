#!/usr/bin/python3
# Time: 2019/05/01 9:58 PM
# About: 40 python3 strings functions

import string
import codecs

text = "this is a good day!"
# text2 = "中文来测试字节码编码!"
# binary_string = b'another binary line'

# print(text.capitalize())       # 只是一个字母

# print(text.center(40, "*"))

# print(text.count("s"))
# print(text.count("d", 0, len(text)))

# print(binary_string.decode("utf-8"))
# print(text2.encode("UTF-8"))    # == print(text2.encode("utf-8"))
# print(text2.encode("GBK"))      # 是不同的
# print(text2.encode("hex"))


# *********************************  codecs  ***********************************************

# print(codecs.encode(binary_string, "hex"))  # b'616e6f746865722062696e617279206c696e65'
# print(codecs.encode(text.encode("utf-8"), "hex"))   # 74686973206973206120676f6f642064617921
# print(codecs.encode(text2.encode("utf-8"), "hex"))   #e4b8ade69687e69da5e6b58be8af95e5ad97e88a82e7a081e7bc96e7a08121


# donkey = "this is a \tlittle\t otter!"
# bird = "iamfloppy bird"
# nums = "154"
# space = " \n \t  "
# title = "     I Am #The Title!"

# print(donkey.endswith("!"))       # 是 endswith 有一个 s

# print(donkey)
# print(donkey.expandtabs(tabsize=8))     # 默认是8空格, 也可以换成 0
# print(donkey.find("x"))             # 没有找到 返回 -1

# print(donkey.index("a"))              # 返回索引的位置

# print(donkey.isalnum())         # isalnum(), 是否是由 字母和数字 组成
# print(bird.isalpha())           # isalpha(), 是否都是由字母组成的, 空格也不算
# print(bird.islower())           # islower() 会忽略空格
# print(nums.isdigit())             # isdigit() 不会忽略空格
# print(nums.isnumeric())

# print(space.isspace())          # \n \t 都算
# print(title.istitle())          # 检查每个单词的首字母是否都是大写, 会忽略标点
# print(donkey.isupper())
# print(nums.join("ll"))
#
# print(title.ljust(50, "*"))         # ljust() 左对齐填充
# print(title.lstrip())               # lstrip() 用来截断左边的空格, 或者是指定的字符

intab = "aeiou"
outtab = "12345"

text = "this is a string example...wow...oops"
transtab = text.maketrans(intab, outtab)        # maketrans( , )    # 制作一个转换映射表
# print(text.translate(transtab))

# print(max(intab))   # u
# print(min(intab))   # a
#
# print(text.replace("wow", "shit"))
# print(text.rfind("k"))              # 从右边开始查找, 没有找到 返回 -1

# print(text.rjust(50, "*").ljust(80, "*"))              # 右对齐填充
# print(text.rstrip())
# print(text.split())                     # 默认的分隔符是  空格

# print(text.splitlines())  # 按照换行分割
# print(text)
#
# print(text.swapcase())      # 将字符串中 大小写互换
# print(text.startswith("this"))          # 注意是startswith 有一个 s
#
# print(text.zfill(100))











