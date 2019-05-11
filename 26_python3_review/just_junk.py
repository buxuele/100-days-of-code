#!/usr/bin/python3
# Time: 2019/05/02 10:44 PM
# About: zip(), map(), iter()都是内建的函数

#
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
#
# pack = list(zip(l1, l2))
# print(pack)
#
# h = list(map(len, ["abc", "de", "fghi"]))
# print(h)
#
# g = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
# print(g)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def naive_grouper(inputs, n):
#     num_groups = len(inputs) // n
#     return [tuple(inputs[i*n: (i+1)*n]) for i in range(num_groups)]
#
#
# def better_grouper(inputs, n):
#     iters = [iter(inputs)] * n
#     # return zip(*iters)              # 这里的这个星号, 是把元组解压为列表
#     return zip(*(iters))              # 这里的这个星号, 是把元组解压为列表
#
# print(list(better_grouper(nums, 2)))
#
#




























