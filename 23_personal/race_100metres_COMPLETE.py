#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time: 2019/04/28 10:08 PM
# About:

import re
import requests
import base64


url = "http://ctf5.shiyanbar.com/jia/index.php"         # 100 race
s = requests.Session()

resp = s.get(url)
# print(resp.text)
# print(s.cookies)

ques = re.findall(r"'my_expr'>(.*?)</div>=?", resp.text)
ques2 = ques[0].strip().replace("x", "*")
anws = str(eval(ques2))

print(ques2)
print(anws)
print(type(anws))

data = {"pass_key": anws}
resp2 = s.post(url + "?action=check_pass", data=data)
print(resp2.text)
# print(s.cookies)
#
with open("shit9.html", "wb") as f:
    f.write(resp2.content)

# 百度网盘搜索引擎
# 叔本华的辩论艺术 免费下载























