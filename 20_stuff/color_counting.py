# when: 2019/04/10 7:52 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

from PIL import Image
from collections import Counter
import prettytable

img = Image.open("timg.jpeg")
size = w, h = img.size
data = img.load()

colors = []
for x in range(w):
    for y in range(h):
        color = data[x, y]
        # print(color)
        hex_color = '#' + ''.join([hex(c)[2:].rjust(2, '0') for c in color])
        colors.append(hex_color)


pt = prettytable.PrettyTable(["Color", "Count"])
for color, count in Counter(colors).items():
    pt.add_row([color, count])

print(pt)


# test rjust later






