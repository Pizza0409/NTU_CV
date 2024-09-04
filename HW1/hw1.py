from PIL import Image
import numpy as np
import cv2

# read the image
img = Image.open('./lena.bmp')
#img.show()
img_arr = np.array(img)
# print(img_arr.shape)

# PART 1
# Q(a)
img_a = img_arr[::-1]
img_a = Image.fromarray(img_a)
# img_a.show()


# Q(b)
img_b = img_arr[:, ::-1]
img_b = Image.fromarray(img_b)
# img_b.show()

# Q(c)
img_c = np.zeros([512, 512], dtype=img_arr.dtype)
for row in range(img_arr.shape[0]):
    for col in range(img_arr.shape[1]):
        img_c[row][col] = img_arr[col][row]

img_c = Image.fromarray(img_c)

# PART1 images save
img_a.save('img_a.bmp')
img_b.save('img_b.bmp')
img_c.save('img_c.bmp')

# PART 2
# Q(d)
img_d = img.rotate(315)
# img_d.show()

# Q(e)
img_e = img.resize((int(img.size[0] / 2), int(img.size[1] / 2)))
# img_e.show()

# Q(f)
_, img_f = cv2.threshold(np.array(img), 128, 255, cv2.THRESH_BINARY)
img_f = Image.fromarray(img_f)
# img_f.show()

# PART2 images save
img_d.save('img_d.bmp')
img_e.save('img_e.bmp')
img_f.save('img_f.bmp')


    