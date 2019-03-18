import os


"""
get into a specific folder, count how many files in it.
"""
dirname = '/home/fc/Downloads/Python'


os.chdir(dirname)
a = os.listdir('.')
print(len(a))   # 91    # 80 23:30


print(os.getenv('logs'))