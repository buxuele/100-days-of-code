#!/usr/bin/python3
# Time: 2019/05/02 11:02 PM
# About: 

import itertools as it

# bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
#
# lett = ['a', 'b', 'c']
#
# print(list(it.combinations(lett, 2)))
# print(list(it.combinations_with_replacement(lett, 2)))

# [('a', 'b'), ('a', 'c'), ('b', 'c')]
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


# res = []
# for i in range(1, len(bills) + 1):
#     for combination in it.combinations(bills, i):
#         if sum(combination) == 100:
#             print("this is the one", combination)
#             res.append(combination)
#
#
#         # print(combination)
# # print(res)
#
# print(len(res))
#
# res = set(res)
# print(res)
# print(len(res))

# 题目是 , 有以下几种面额的钞票, 不计数量, 总共有多少中组合方式, 使总和为100元
# bills = [50, 20, 10, 5, 1]
# res = []
#
# # # 101 指的是 100张1元的也是可能的.并且是钞票总数最多的可能性了
# for n in range(1, 101):
#     for c in it.combinations_with_replacement(bills, n):
#         if sum(c) == 100:
#             res.append(c)
#             # print(c)
#
# print(len(res))

# color = ['r', 'g', 'b']
# print(list(it.permutations(color, 2)))
# print(list(it.combinations(color, 2)))
# print(list(it.combinations_with_replacement(color, 2))) #
#

# ct = it.count(start=1, step=2)
# print(list(next(ct) for _ in range(5)))

# print(list(zip(it.count(), ['a', 'b', 'c'])))

# def fibs():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# print(list(it.accumulate([1, 2, 3, 4, 5])))

# print(list(it.product([1, 2, 3], ['a', 'b', 'c'])))

# Poke Game

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']
cards = list(it.product(ranks, suits))
print(len(cards))
print(cards)















