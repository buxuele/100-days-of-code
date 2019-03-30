# when: 2019/03/30 9:22 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1.  pip3 install fake-useragent
2. 知乎的技术提高了。给了我虚假的信息。。。有待改进
3.

"""

import requests
from fake_useragent import UserAgent

ua = UserAgent()
# url = "https://www.zhihu.com/question/305792030/answer/615096534"
url = 'https://www.zhihu.com/topic'
headers = {"User-Agent": ua.random}


def grab():
    html = requests.get(url, headers=headers).text
    print(html)


if __name__ == "__main__":
    grab()



