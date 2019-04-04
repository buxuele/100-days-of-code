# when: 2019/04/04 6:40 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径

"""

import os


def rename_me(p):

    abs = os.path.abspath(p)
    for d in os.listdir(p):
        files_path = os.path.join(p, d)

        # print(files_path)
        if os.path.isdir(files_path):
            rename_me(files_path)
        else:
            print(files_path)

        # rename_me(d)
    #
    # print("***30")
    # print(dirname)
    # print(abs)



if __name__ == "__main__":
    rename_me("/home/fc/Pictures/")



