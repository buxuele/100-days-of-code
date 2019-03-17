import os
import imageio

im = imageio.imread('imageio:chelsea.png')

print(im.size)
print(im.shape)

# gary-scale and jpg
imageio.imwrite('./chelsea_gray.jpg', im[:, :, 0])
