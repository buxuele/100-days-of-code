import time
from multiprocessing import Pool
import requests

# use multiprocessing

def gen():
    us = []
    for i in open('x.m3u8'):
        if i[0] != "#":
            url = 'http://video.ynianyongheng.com:8091/20190201/0054_sd/1000kb/hls/' + i.strip()
            # yield url

            #   http://video.ynianyongheng.com:8091/20190201/HEFJ0DWO1517/1000kb/hls/
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

    # mp
    t1 = time.time()
    print("start: ", t1)

    urls = gen()

    my_pool = Pool(30)
    my_pool.map(download, urls)
    my_pool.close()
    my_pool.join()

    t2 = time.time()
    print("cost time: ", t2 - t1)
    '''
    cat *.ts > all.ts
    
    '''

    # cost time:  309.54209423065186