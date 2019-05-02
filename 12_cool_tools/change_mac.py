# date: 2019/03/21 7:50 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. sudo apt-get install macchanger

"""
import time
import os

interface = 'lalalalala'

os.system(f'sudo ifconfig {interface} down')
os.system(f'sudo macchanger -r {interface}')
os.system(f'sudo macchanger -r {interface}')
os.system(f'sudo ifconfig {interface} up')
time.sleep(1)




