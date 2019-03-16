from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent
from gevent import pool


# https://some.ts
def gen():
    us = []
    for i in open('index.m3u8'):
        if i[0] != "#":
            url = 'https://some' + i.strip()
            # yield url
            us.append(url)
    return us
    # print(url)


def download(url):
    s = requests.Session()
    cont = s.get(url).content
    fn = url.split('/')[-1]
    with open(fn, 'wb') as f:
        f.write(cont)


if __name__ == '__main__':
    # basic
    # for i in gen():
    #     download(i)

    t1 = time.time()
    print("start: ", t1)

    urls = gen()

    poo = pool.Pool(30)

    jobs = []
    for u in urls:
        jobs.append(poo.spawn(download, u))
    gevent.joinall(jobs)

    t2 = time.time()
    print("cost time: ", t2 - t1)

    '''
    option 1 (no-key is needed):
        cat *.ts > all.ts   
        ffmpeg -i all.ts -acodec copy -vcodec copy all2.mp4
    
    option 2(need key):
        1. change *.m3u8: 
            #EXT-X-KEY:METHOD=AES-128,URI=key.key !!! no-quote-marks
        2. run : 
            # ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy tt.mp4
    
    option 3(not sure about this):
        ffmpeg -i index.m3u8 -c copy rename_me.mp4
    '''


