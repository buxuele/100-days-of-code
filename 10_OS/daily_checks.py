import platform
import os
import sys
import time


"""
1. loads everything I need to start my work.

2. print(sys.argv[0])   current-file-abs-path
3. print(os.getenv('USERNAME'))     user-name
4. print(platform.node())       PC-name
"""


def greet():
    print("晚上好！" + os.getenv('USERNAME'))
    print(f"{sys.argv[0]} is running on {platform.node()}")


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('CLS')


def change_mac():
    os.chdir('/home/fc/')
    # print('\n'.join(os.listdir('.')))
    os.system('sudo python3 mac.py')
    os.system('sudo netease-cloud-music')


def open_editor():
    os.system('charm')
    time.sleep(3)
    os.system('atom')
    time.sleep(3)


if __name__ == '__main__':
    greet()
    change_mac()
    open_editor()


