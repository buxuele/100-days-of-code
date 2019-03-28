from gevent import monkey
monkey.patch_all()

import os
import time
import requests
import gevent
from gevent import pool

"""how to use
1. set url pattern
2. run 

next step
1. find 720P?
2. auto-download with a single url
3. checkout sele-deep 

"""

# https://1-398-19-12.b.cdn13.com/hls/008/327/912/720p.h264.mp4/seg-1-v1-a1.ts?cdn_creation_time=1553428800&cdn_ttl=14400&cdn_cv_data=116.238.131.199&cdn_hash=6404e417a16f4a6d2d78a96917619b9e
def gen():
    us = []
    for i in open('index.m3u8'):
        if i[0] != "#":
            url = "https://1-398-19-12.b.cdn13.com/hls/008/327/912/720p.h264.mp4/" + i.strip()
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


def get_mp4():
    os.system('cat *.ts > all.ts')
    os.system('ffmpeg -i all.ts -acodec copy -vcodec copy all2.mp4')
    os.system('rm *.ts')
    os.system('ls -a')


if __name__ == '__main__':
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

    print("start deal with ts-files...\tplease wait for a moment...\n")
    # get_mp4()

    '''
    option 1 (no-key is needed):
        cat *.ts > all.ts   
        ffmpeg -i all.ts -acodec copy -vcodec copy h2.mp4

    option 2(need key):
        1. change *.m3u8: 
            #EXT-X-KEY:METHOD=AES-128,URI=key.key !!! no-quote-marks
        2. run : 
            #  # this is a good one!
            ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy h1.mp4  

    option 3(not sure about this):
        ffmpeg -i index.m3u8 -c copy rename_me.mp4
    '''


