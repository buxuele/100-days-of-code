import sys
from PIL import ImageDraw, ImageFont, Image


"""
add water-mark to an image 

"""

text = "Apple is the best!"
text_size = 20
text_color = [200, 0, 200]  # r, g, b


def waterMark():
    img = Image.open('a.jpg')
    img = img.convert("RGBA")
    pix_data = img.load()

    print(img.size)

    # on bash: man -k font, then [fc-list] show all fonts
    font = ImageFont.truetype("/usr/share/fonts/truetype/tlwg/Kinnari-BoldOblique.ttf", size=text_size)

if __name__ == '__main__':
    waterMark()



