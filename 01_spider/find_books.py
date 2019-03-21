# date: 2019/03/21 7:52 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
这个文件的作用：
1. 检查电子书网站否有更新，更新了哪些内容
2. 是否需要下载这些电子书。
"""

import requests
from bs4 import BeautifulSoup

url = 'http://mebook.cc/category/gjs/bckf'
s = requests.Session()


# 这个文件只在初始运行一次，获取书单
def set_up(url):
    resp = s.get(url)  # just response obj
    # print(resp.status_code)	#200
    # print(resp.encoding)	# utf-8

    soup = BeautifulSoup(resp.text, 'lxml')
    booknames = soup.find_all("h2")
    for b in booknames:
        if b.contents:
            # 这样一行解决战斗。更简洁。
            print(b.contents[1].get('title') + b.contents[1].get('href'))


# 	# 下面需要把爬虫的结果，写入文件
set_up(url)




