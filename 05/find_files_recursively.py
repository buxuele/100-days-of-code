import os
import fnmatch

'''
!!! Attention:
1. os.walk()
2. fnmatch.filer()
3. 
'''


PATH = '/home/fc/Desktop/'
PATTERN = '*.js'

def get_file_names(filepath, pattern):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            # print(root, dirnames, filenames)

            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(filename))
        if matches:
            print('Found {} files:'.format(len(matches)))
            output_files(matches)
        else:
            print("No files found.")
    else:
        print("Sorry, path does not exist. Try again.")


def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)


if __name__ == '__main__':
    get_file_names(PATH, PATTERN)
