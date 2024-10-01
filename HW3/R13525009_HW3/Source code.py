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

plt.bar(range(256), his_a)
# plt.show()
plt.savefig("img_a.jpg")
im.open("./img_a.jpg").save("img_a.bmp")
plt.clf()

# Q2
img_b_arr = (img_arr / 3).astype(img_arr.dtype)

his_b = np.zeros(256)

for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        his_b[img_b_arr[i, j]] += 1

plt.bar(range(256), his_b)
# plt.show()
plt.savefig("img_b_his.jpg")
im.open("./img_b_his.jpg").save("img_b_his.bmp")
plt.clf()

img_b = im.fromarray(img_b_arr)
# img_b.show() 
img_b.save("img_b.bmp")

# Q3
img_c_arr = np.zeros_like(img_b_arr)
his_e = np.zeros(256)

hist = his_b.copy()

cdf = hist.cumsum()
cdf_min = cdf.min()
cdf_max = cdf.max()

cdf_normalized = ((cdf - cdf_min) / (cdf_max - cdf_min) * 255).astype('uint8')

# Use the CDF to map the original pixel values to the new range
img_c_arr = cdf_normalized[img_b_arr]

img_c = im.fromarray(img_c_arr)
# img_c.show()
img_c.save("img_c.bmp")

# Compute the histogram of the equalized image
for i in range(img_c_arr.shape[0]):
    for j in range(img_c_arr.shape[1]):
        his_e[img_c_arr[i, j]] += 1

plt.bar(range(256), his_e)
# plt.show()
plt.savefig("img_c_his.jpg")
im.open("./img_c_his.jpg").save("img_c_his.bmp")