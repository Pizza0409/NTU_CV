import os
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt

img = im.open("./lena.bmp")

img_arr = np.array(img)

# Q1
his_a = np.zeros(256)

for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        his_a[img_arr[i, j]] += 1

plt.fill(his_a)
plt.show()
plt.savefig("img_a.jpg")
im.open("./img_a.jpg").save("img_a.bmp")
plt.clf()


# Q2
his_b = his_a.copy() / 3
img_b_arr = (img_arr / 3).astype(img_arr.dtype)

plt.fill(his_b)
plt.ylim(0, max(his_a))
plt.show()
plt.savefig("img_b_his.jpg")
im.open("./img_b_his.jpg").save("img_b_his.bmp")
plt.clf()

img_b = im.fromarray(img_b_arr)
img_b.show() 
img_b.save("img_b.bmp")

# Q3
img_c_arr = np.zeros_like(img_b_arr)
his_e = np.zeros(256)

hist = np.zeros(256)
for i in range(img_b_arr.shape[0]):
    for j in range(img_b_arr.shape[1]):
        hist[img_b_arr[i, j]] += 1

cdf = hist.cumsum()
cdf_min = cdf.min()
cdf_max = cdf.max()

cdf_normalized = ((cdf - cdf_min) / (cdf_max - cdf_min) * 255).astype('uint8')

img_c_arr = cdf_normalized[img_b_arr]

for i in range(img_c_arr.shape[0]):
    for j in range(img_c_arr.shape[1]):
        his_e[img_c_arr[i, j]] += 1

plt.bar(range(256), his_e)
plt.ylim(0, )
plt.show()
plt.savefig("img_c.jpg")
im.open("./img_c.jpg").save("img_c.bmp")