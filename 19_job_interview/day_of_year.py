# when: 2019/04/04 9:37 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

import datetime


def rename_me():
    year = input("year")
    month = input("month")
    day = input("day")

    d1 = datetime.date(year=int(year), month=int(month), day=int(day))
    d2 = datetime.date(year=int(year), month=1, day=1)
    print(d1)
    print(d2)
    print((d1-d2).days)


if __name__ == "__main__":
    rename_me()



