#!/usr/bin/python3
# Time: 2019/04/28 4:18 PM
# About: 


"""
all_peaches = " "

i = 10  p = 1  pre = 1
i = 9   p = 4 = 2*2 = 2*1+1 =
i = 8   p = all /2 -1

"""
#  ((x+1)*2 +1)*2


def eat(remains):
    all_num = (remains + 1) * 2


cont = 1

for i in range(0, 10):
    # print(i)    # 此时的桃子数量是1
    cont = (cont + 1) * 2
    print(i, cont)

























