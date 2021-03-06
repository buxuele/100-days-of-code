# date: 2019/03/22 9:27 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com

"""about:
1. a library for wikidata api
    https://github.com/dahlia/wikidata
2. pip3 install Wikidata
"""

from wikidata.client import Client

c = Client()

# 一个词条
item = c.get("Q20145", load=True)
print(item)
print(item.description)

# 一个图片
img_prop = c.get("P18")
img = item[img_prop]
print(img)
print(img.image_resolution)
print(img.image_url)


