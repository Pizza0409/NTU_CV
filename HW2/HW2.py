import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

img = Image.open("./lena.bmp")

# Convert image to array
img_arr = np.array(img)

# Q1
img_arr_binary = img_arr.copy()

for row in range(img_arr_binary.shape[0]):
    for col in range(img_arr_binary.shape[1]):
        if img_arr_binary[row][col] >= 128:
            img_arr_binary[row][col] = 255
        else:
            img_arr_binary[row][col] = 0

img_a = Image.fromarray(img_arr_binary)
# img_a.show()
img_a.save('img_a.bmp')

# Q2 
histogram = np.zeros(256)

for row in range(img_arr.shape[0]):
    for col in range(img_arr.shape[1]):
        histogram[img_arr[row][col]] += 1

plt.fill(histogram)
plt.xlim(0, 255)
plt.ylim(0, max(histogram))
# plt.show()
plt.savefig("lena_b.jpg")

# Q3 
img_arr_ccl = img_arr.copy()

# Convert image to binary (0 and 1) manually
for row in range(img_arr_ccl.shape[0]):
    for col in range(img_arr_ccl.shape[1]):
        img_arr_ccl[row, col] = 1 if img_arr_ccl[row, col] >= 128 else 0

region = {}
idx = 2

# Ensure img_arr_cc is of type int32 to avoid overflow issues with idx
img_arr_ccl = img_arr_ccl.astype(np.int32)

for i in range(img_arr_ccl.shape[0]):
    for j in range(img_arr_ccl.shape[1]):
        if img_arr_ccl[i, j] == 1:
            up = i
            bottom = i
            left = j
            right = j
            area = 1
            stack = [(i, j)]
            rows = i
            cols = j
            while stack:
                i1, j1 = stack.pop()
                img_arr_ccl[i1, j1] = idx
                up = min(up, i1)
                bottom = max(bottom, i1)
                left = min(left, j1)
                right = max(right, j1)
                area += 1
                rows += i1
                cols += j1
                # Check and push valid neighbors to the stack
                for x, y in [(i1, j1+1), (i1+1, j1), (i1-1, j1), (i1, j1-1)]:
                    if 0 <= x < img_arr_ccl.shape[0] and 0 <= y < img_arr_ccl.shape[1] and img_arr_ccl[x, y] == 1:
                        stack.append((x, y))
            # Store region info (center of centroid, up, bottom, left, right, area)
            region[idx] = (rows // area, cols // area, up, bottom, left, right, area)
            idx += 1

# Filter regions with area greater than 500 pixels
answer = [val for val in region.values() if val[6] > 500]

img_c = np.stack([img_arr_binary] * 3, axis=-1).astype(np.uint8)

for i in answer:
    cv2.rectangle(img_c, (i[4], i[2]), (i[5], i[3]), (0, 0, 255), 2)
    cv2.circle(img_c, (i[1], i[0]), 5, (255, 0, 0), 2)

img_c = Image.fromarray(img_c)
# img_c.show()
img_c.save("img_c.bmp")

