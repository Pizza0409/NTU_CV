import numpy as np
import os
from PIL import Image as im

img = im.open('./lena.bmp')

img_arr = np.array(img)
img_size0 = img_arr.shape[0]
img_size1 = img_arr.shape[1]

# img binary
img_arr_binary = img_arr.copy()
for row in range(img_size0):
    for col in range(img_size1):
        if img_arr_binary[row, col] < 128:
            img_arr_binary[row, col] = 0
        else:
            img_arr_binary[row, col] = 255

img_binary = im.fromarray(img_arr_binary)
# img_binary.show()

# define the kernel the hw asked
ort_kernel = np.array([[0, 1, 1, 1, 0], 
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [0, 1, 1, 1, 0]])

kernel_j = np.array([[0,0,0],[1,1,0],[0,1,0]])
kernel_k = np.array([[0,1,1],[0,0,1],[0,0,0]])

# Q1 dilation
def dilation(img, kernel):
    kernel_size = len(kernel)
    dilation_img = np.zeros_like(img)
    
    for i in range(img_size0):
        for j in range(img_size1):
            max_value = 0
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    ni, nj = i + ki - kernel_size // 2, j + kj - kernel_size // 2
                    if 0 <= ni < img_size0 and 0 <= nj < img_size1:
                        if kernel[ki][kj] == 1:
                            pixel_value = img[ni][nj]
                            if pixel_value > max_value:
                                max_value = pixel_value
            dilation_img[i, j] = max_value

    return dilation_img.astype(np.uint8)

dilated_img = dilation(img_arr_binary, ort_kernel)
dilated_img = im.fromarray(dilated_img)
dilated_img.show()
dilated_img.save('img_a.bmp')

# Q2 erosion
def erosion(img, kernel):
    kernel_size = len(kernel)
    erosion_img = np.zeros_like(img)

    for i in range(img_size0):
        for j in range(img_size1):
            min_value = 255
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    ni, nj = i + ki - kernel_size // 2, j + kj - kernel_size // 2
                    if 0 <= ni < img_size0 and 0 <= nj < img_size1:
                        if kernel[ki][kj] == 1:
                            pixel_value = img[ni][nj]
                            if pixel_value < min_value:
                                min_value = pixel_value
            erosion_img[i, j] = min_value

    return erosion_img.astype(np.uint8)


erosion_img = erosion(img_arr_binary, ort_kernel)
erosion_img = im.fromarray(erosion_img)
erosion_img.show()
erosion_img.save('img_b.bmp')

# Q3 opening
def opening(img, kernel):
    return (dilation(erosion(img, kernel), kernel))

opening_img = opening(img_arr_binary, ort_kernel)
opening_img = im.fromarray(opening_img)
opening_img.show()
opening_img.save('img_c.bmp')

# Q4 clossing
def closing(img, kernel):
    return (erosion(dilation(img, kernel), kernel))

closing_img = closing(img_arr_binary, ort_kernel)
closing_img = im.fromarray(closing_img)
closing_img.show()
closing_img.save('img_d.bmp')

# Q5 hit and miss
def hit_and_miss(img, kernel1, kernel2):
    hit = erosion(img, kernel1)
    miss = erosion(-img+255, kernel2)
    # print(miss)     

    return (hit & miss).astype(np.uint8)


hit_and_miss_img = hit_and_miss(img_arr_binary, kernel_j, kernel_k)
hit_and_miss_img = im.fromarray(hit_and_miss_img)
hit_and_miss_img.show()
hit_and_miss_img.save('img_e.bmp')


