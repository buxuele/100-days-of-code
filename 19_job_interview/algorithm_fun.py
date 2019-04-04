# when: 2019/04/04 11:38 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

# 1. reverse int
# seen it at leetcode

# 2. find all .pyc file
#
# import os
#
#
# def get_pyc(dir, suffix):
#     res = []
#     for root, dirs, files in os.walk(dir):
#         for filename in files:
#             name, suf = os.path.splitext(filename)
#             if suf == suffix:
#                 res.append(os.path.join(root, filename))
#     print(res)
#
#
# get_pyc('./', '.py')


# from glob import iglob
#
# def func(fp, postfix):
#     for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
#         print(i)
#
# func('./', '.py')


# print(sum([i for i in range(1, 101)]))
# print(sum(range(10)))



# 列表元素过滤

# a = [1,2,3,4,5,6,7,8]
# b = filter(lambda x: x>4, a)
# print(type(b))  # class 'filter'
# print(list(b))


# c = [i for i in a if i > 3]
# print(c)


#
#
# from string import ascii_lowercase
#
# # print(ascii_lowercase)
# def get_missing(s):
#     s1 = set(str(ascii_lowercase))
#     s2 = set(s)
#     ret = "".join(s1-s2)
#     print(ret)
#
# get_missing("hello")
#
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [i for i in a if i%2==1]
# print(b)

# 用一行python代码写出1+2+3+10248
#
# n = sum([1, 2, 3, 10248])
# print(n)

# from functools import reduce

# # 个人理解： reduce 就是一个构造数组的工具
# n2 = reduce(lambda x,y: x+y, [1, 2, 3, 10248])
# print(n2)


# print(ord('1'))

# print(ord('l'))
# print(ord('o'))
# print(ord('v'))
# print(ord('e'))

# Counter(re.sub("\W+", " ", f.read()).split()).most_common(10)

from collections import Counter

a = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
x = Counter()

















