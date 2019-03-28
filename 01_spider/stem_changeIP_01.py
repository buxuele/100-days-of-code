# when: 2019/03/26 6:36 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1.  change my IP , use stem
2.  pip3 install stem
"""

import requests
from stem.control import Controller
from stem import Signal

#
# resp = requests.get("http://icanhazip.com/")
# print(resp.text.strip())
# 116.238.131.199


with Controller.from_port(port=9051) as c:
    c.authenticate(password='mypassword')
    c.signal(Signal.NEWNYM)

    resp2 = requests.get("http://icanhazip.com/")
    print(resp2.text.strip())

#
#
# def rename_me():
#     pass
#
#
# if __name__ == "__main__":
#     pass



