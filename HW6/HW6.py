from PIL import Image as im
import os
import numpy as np

img = im.open("./lena.bmp")
# img.show()

img_arr = np.array(img)
img_size0, img_size1 = img_arr.shape

# for i in 