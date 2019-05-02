#!/usr/bin/python3
# Time: 2019/04/26 3:35 PM


"""about:
1. 

"""
import base64
import requests



# s = "MDEzMjE5MDAyMTg0MTUzMjQwMTQ0MDc3MjUzMDk2MTc1MTUzMTE4MTg4MDEwMDA2MTg4MDA0MjM4MDI1MTA3MTU4MTc5MTM4"
# print(len(s))
#
# g = "013219002184153240144077253096175153118188010006188004238025107158179138"
# print(len(g))
# print(base64.b64decode(s))



url = "https://www.jianshu.com/search?q=%E8%AE%B2%E4%B8%AA%E7%AC%91%E8%AF%9D&page=1&type=note"
raw = "https://www.jianshu.com/search?q=我是中文&page=1&type=note"


print(requests.utils.unquote(url))
print()
print(requests.utils.quote(raw))










