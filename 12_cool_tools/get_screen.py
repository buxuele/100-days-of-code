# date: 2019/03/21 7:39 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. Windows 下的定时截屏工具，可以看看自己在某段时间内在做什么
2. ubuntu 下。不能用。#　ImageGrab is macOS and Windows only
"""

from PIL import ImageGrab
import time


def screen():
    im = ImageGrab.grab()
    # fn = time.strftime("%Y-%m-%d %H:%-M:%S")
    fn = str(int(time.time()))
    savePath = '%s.png' % fn

    im.save(savePath)
    print('done')


def timer():
    print(time.strftime("%H:%M:%S"))
    while True:
        x = time.strftime("%S")
        if x == "00":
            screen()
            time.sleep(59)

# screen()
timer()





