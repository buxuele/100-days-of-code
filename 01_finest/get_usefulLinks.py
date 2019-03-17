import requests

"""
get some interesting links form this domain:
# http://dl.funsaber.net/

"""

def scan():
    url = 'http://dl.funsaber.net/'
    s = requests.get(url)
    print(s.text)



def write_to_file(filename, txt):
    with open(filename, 'w') as file_object:
        s = file_object.write(txt)


if __name__ == '__main__':
    # write_to_file('test.txt', 'I am beven')
    scan()