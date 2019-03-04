from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent
from gevent import pool

def gen():
    us = []
    for i in open('x.m3u8'):
        if i[0] != "#":
            url = 'http://video.ynianyongheng.com:8091/20190201/HEFJ0DWO1517/1000kb/hls/' + i.strip()
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
    cat segment1_0_av.ts segment2_0_av.ts segment3_0_av.ts > all.ts
    ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4
    
    decode ts-files
    .m3u8: #EXT-X-KEY:METHOD=AES-128,URI=key.key !!! no-quote-marks
    ffmpeg -allowed_extensions ALL -i x.m3u8 -c copy teacher.mp4
    
    
    ffmpeg -i x.m3u8 -c copy teacher.mp4
    
    
    
    '''

