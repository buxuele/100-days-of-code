import glob
import sys

# 用于文件匹配的
print(glob.glob("*.png")) 


# script = sys.argv.pop(0)
args = sys.argv[0]  # this is the current file

# print(script)
print(args)


# run like this :
# python3 test.py ok hi

print(sys.argv[1:]) # ['ok', 'hi']
