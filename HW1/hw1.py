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
img_c = np.zeros([512, 512], dtype=img_arr.dtype)
for row in range(img_arr.shape[0]):
    for col in range(img_arr.shape[1]):
        img_c[row][col] = img_arr[col][row]

img_c = Image.fromarray(img_c)

img_a.save('img_a.bmp')
img_b.save('img_b.bmp')
img_c.save('img_c.bmp')

# Q(d)

# Q(e)

# Q(f)

    