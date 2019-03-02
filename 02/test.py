import glob
import sys

# 用于文件匹配的
print(glob.glob("*.png")) 



script = sys.argv.pop(0)
args = sys.argv


print(script)
print(args)

