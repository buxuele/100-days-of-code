# when: 2019/03/23 12:38 AM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. remove some files

"""

import os


def rename_me():
    print()
    fs = os.listdir('.')
    for i in fs:
        if i[:2] == 'se':
            print(i)
            os.remove(i)


if __name__ == "__main__":
    rename_me()



