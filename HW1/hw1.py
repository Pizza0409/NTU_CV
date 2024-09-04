from PIL import Image
import numpy as np
import cv2

img = Image.open('./lena.bmp')
#img.show()
img_arr = np.array(img)
print(img_arr.shape)
# Q(a)
img_a = img_arr[::-1]
img_a = Image.fromarray(img_a)
#img_a.show()


# Q(b)
img_b = img_arr[:, ::-1]
img_b = Image.fromarray(img_b)
#img_b.show()

# Q(c)
img_d = np.zeros([512, 512], dtype=img_arr.dtype)
for row in range(img_arr.shape[0]):
    for col in range(img_arr.shape[1]):
        img_d[row][col] = img_arr[row][col]

img_d = Image.fromarray(img_d)
img_d.show()

    