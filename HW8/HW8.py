import numpy as np
from PIL import Image as im
import random

img = im.open("./lena.bmp")
img_arr = np.array(img)
img_size0, img_size1 = img_arr.shape

# calculate the snr
def SNR(origin, noisy):
    vs = np.var(origin)
    vn = np.var(origin - noisy)
    return 20 * np.log10(np.sqrt(vs) / np.sqrt(vn))

# generator the gaussian noise
def gaussian_noise(imgarr, amp):
    img_gauss_arr = np.zeros([img_size0, img_size1])
    for i in range(img_size0):
        for j in range(img_size1):
            img_gauss_arr[i, j] = max(0, min(255, imgarr[i, j] + amp * random.gauss(0, 1)))

    snr = SNR(imgarr, img_gauss_arr)
    print("SNR for Gaussian noisy with amp = {amp} is {snr}.".format(amp=amp, snr=snr))
    img_gauss = im.fromarray(np.array(img_gauss_arr, dtype=np.uint8))
    # img_gauss.save("./gauss_{amp}.bmp".format(amp=amp))
    # img_gauss.show()

gaussian_noise(img_arr, 10)
gaussian_noise(img_arr, 30)

def salt_and_pepper(imgarr, threshold):
    img_st_arr = np.zeros((img_size0, img_size1))
    for i in range(img_size0):
        for j in range(img_size1):
            tmp = random.random()
            if tmp <= threshold:
                img_st_arr[i, j] = 0
            elif tmp > 1 - threshold:
                img_st_arr[i, j] = 255
            else:
                img_st_arr[i, j] = imgarr[i, j]
    
    # calculatet the snr
    snr = SNR(imgarr, img_st_arr)
    print("SNR for salt&pepper with amp = {threshold} is {snr}.".format(threshold=threshold, snr=snr))
    
    img_st = im.fromarray(np.array(img_st_arr, dtype=np.uint8))
    # img_st.save("./st_{threshold}.bmp".format(threshold=threshold))
    # img_st.show()

salt_and_pepper(img_arr, 0.1)
salt_and_pepper(img_arr, 0.05)

# Expand the image array with zeros
def expand_with_zeros(arr, pad_size):
    m, n = arr.shape
    result = np.zeros((m + 2 * pad_size, n + 2 * pad_size), dtype=arr.dtype)  
    for i in range(m):
        for j in range(n):
            result[i + pad_size, j + pad_size] = arr[i, j]  # Put the original pixel to the center
    return result

# Apply a box filter of size `k x k`
def box_filter(img, k):
    pad_size = k // 2
    imgarr = np.array(img)
    img_padded = expand_with_zeros(imgarr, pad_size)
    m, n = imgarr.shape
    result = np.zeros_like(imgarr)
    
    for i in range(m):
        for j in range(n):
            total = 0
            for p in range(k):
                for q in range(k):
                    total += img_padded[i + p, j + q]
                result[i, j] = total / (k * k)
    

    # calculate SNR
    snr = SNR(img_arr, result)
    print("SNR for box filter {k}x{k} is {snr}.".format(k=k, snr=snr))
    
    result = im.fromarray(result.astype(np.uint8))
    # result.save("./boxfilter_{k}.bmp".format(k=k))
    result.show()


img_gauss_10 = im.open("./gauss_10.bmp")
img_gauss_30 = im.open("./gauss_30.bmp")
img_gauss_10_arr = np.array(img_gauss_10)
box_filter(img_gauss_10, 3)
box_filter(img_gauss_10, 5)

