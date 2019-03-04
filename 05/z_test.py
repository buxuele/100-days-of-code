import os
import re
import requests

import fnmatch      # this is a build-in package

# url = "http://llmb10.com/llzy"
#
# html = requests.get(url).text
#
#
# # m = re.compile(r'href="(.*?)"')
#
# res = re.findall(r'href="(.*?)"', html)
#
# for s in res:
#     print(s)


# os.rename("1_xx.py", "multiprocessing_crawl.py")

# find files

# PATH = '/home/fc/Desktop/'
# PATTERN = '*.js'
#
# def get_file_names(filepath, pattern):
#     matches = []
#     if os.path.exists(filepath):
#         for root, dirnames, filenames in os.walk(filepath):
#             # print(root, dirnames, filenames)
#
#             for filename in fnmatch.filter(filenames, pattern):
#                 matches.append(os.path.join(filename))
#         if matches:
#             print('Found {} files:'.format(len(matches)))
#             output_files(matches)
#         else:
#             print("No files found.")
#
#     else:
#         print("Sorry, path does not exist. Try again.")
#
# def output_files(list_of_files):
#     for filename in list_of_files:
#         print(filename)
#
# if __name__ == '__main__':
#     get_file_names(PATH, PATTERN)

#
#
#
# import subprocess
#
# i = subprocess.check_output(['ls  -al'], shell=True)
# # print(i)
#
# subprocess.call(["ls", "-al"])

# import hashlib
#
#
# a = hashlib.md5()
# print(a)

# def raises(err, lamda):
#     try:
#         lamda()
#         return False
#     except err:
#         return True
#
#
# raises("No", os.getcwd)


a = "ok"

print(type(a) == str)



print('/ok')























