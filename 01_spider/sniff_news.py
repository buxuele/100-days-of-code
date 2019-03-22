# date: 2019/03/22 8:15 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. 检查这个网站上Python话题的更新情况，每天运行一次

"""

import re
import requests
from bs4 import BeautifulSoup


# 1--45

url = 'https://www.itcodemonkey.com/category/LovePython/p/1/'
url_linux = 'https://www.itcodemonkey.com/category/LoveLinux1024/p/1/'
s = requests.Session()


# 拿到每一个页面中 文章的标题和链接
def set_up(url):
    resp = s.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    span9 = soup.find("div", {"class": "span9"})
    zone = span9.find_all("a")

    for t in zone:
        link = t.get("href")
        if link[-5:] == ".html":
            print(t.find("h2").text, "https://www.itcodemonkey.com" + link)    # this is the link


if __name__ == '__main__':
    set_up(url_linux)




