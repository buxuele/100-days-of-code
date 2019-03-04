import os
import time

# this file is just quite basic stuff, will be deleted later

PATH = os.getcwd()
dirCount = 0
fileCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

if __name__ == '__main__':
    print(f"dirs: {dirCount}")
    print(f"fiels: {fileCount}")