import numpy as np
from PIL import Image as im
import random

img = im.open("./lena.bmp")
img_arr = np.array(img)
img_size0, img_size1 = img_arr.shape

# Calculate the SNR
def SNR(origin, noisy):
    m, n = origin.shape
    mu = np.mean(origin)
    mu_n = np.mean(noisy - origin)
    vs = np.mean((origin - mu) ** 2)
    vn = np.mean((noisy - origin - mu_n) ** 2)
    return 20 * np.log10(np.sqrt(vs) / np.sqrt(vn))


# Generate the gaussian noise
def gaussian_noise(imgarr, amp):
    img_gauss_arr = np.zeros(imgarr.shape)
    for i in range(imgarr.shape[0]):
        for j in range(imgarr.shape[1]):
            img_gauss_arr[i, j] = max(0, min(255, imgarr[i, j] + amp * random.gauss(0, 1)))

    snr = SNR(imgarr, img_gauss_arr)
    print(f"SNR for Gaussian noisy with amp = {amp} is {snr}")
    img_gauss = im.fromarray(img_gauss_arr.astype(np.uint8))
    # img_gauss.save(f"./gauss_{amp}.bmp")
    # img_gauss.show()
    return img_gauss_arr

imgarr_gauss_10 = gaussian_noise(img_arr, 10)
imgarr_gauss_30 = gaussian_noise(img_arr, 30)

# Add salt and pepper noise to the image
def salt_and_pepper(imgarr, threshold):
    img_st_arr = np.zeros(imgarr.shape)
    for i in range(imgarr.shape[0]):
        for j in range(imgarr.shape[1]):
            tmp = random.random()
            if tmp <= threshold:
                img_st_arr[i, j] = 0
            elif tmp > 1 - threshold:
                img_st_arr[i, j] = 255
            else:
                img_st_arr[i, j] = imgarr[i, j]
    
    # Calculate the SNR
    snr = SNR(imgarr, img_st_arr)
    print(f"SNR for salt & pepper with threshold = {threshold} is {snr}")
    
    img_st = im.fromarray(img_st_arr.astype(np.uint8))
    # img_st.save(f"./st_{threshold}.bmp")
    # img_st.show()
    return img_st_arr

imgarr_st_01 = salt_and_pepper(img_arr, 0.1)
imgarr_st_05 = salt_and_pepper(img_arr, 0.05)

# Expand the image array using replicate padding
def expand_with_replicate(arr, pad_size):
    m, n = arr.shape
    result = np.zeros((m + 2 * pad_size, n + 2 * pad_size), dtype=arr.dtype)
    # 填充邊界
    result[pad_size:-pad_size, pad_size:-pad_size] = arr
    result[:pad_size, pad_size:-pad_size] = arr[0, :]  # 上邊界
    result[-pad_size:, pad_size:-pad_size] = arr[-1, :]  # 下邊界
    result[pad_size:-pad_size, :pad_size] = arr[:, 0][:, None]  # 左邊界
    result[pad_size:-pad_size, -pad_size:] = arr[:, -1][:, None]  # 右邊界
    # 填充四個角
    result[:pad_size, :pad_size] = arr[0, 0]
    result[:pad_size, -pad_size:] = arr[0, -1]
    result[-pad_size:, :pad_size] = arr[-1, 0]
    result[-pad_size:, -pad_size:] = arr[-1, -1]
    return result

# Apply box filter
def box_filter(img, k, noise_name):
    pad_size = (k - 1) // 2
    img_padded = expand_with_replicate(img, pad_size)
    m, n = img.shape
    result = np.zeros((m, n), dtype=float)

    for i in range(m):
        for j in range(n):
            result[i, j] = img_padded[i:i + k, j:j + k].mean()
    
    result_img = im.fromarray(result.astype(np.uint8))
    # result_img.show()
    result_img.save(f"./box_{k}_{noise_name}.bmp")

    snr = SNR(img_arr, result)
    print(f"SNR for box filter {k}x{k}: {snr:.6f}")

# Load noisy images and apply box filter
print("------------------------------------")
print("box filter : ")
print("------------------------------------")
print("gaussian noise with 10")
print("++++++++++++++++++++++++++++++++++++")
box_filter(imgarr_gauss_10, 3, "gauss_10")
box_filter(imgarr_gauss_10, 5, "gauss_10")
print("------------------------------------")
print("gaussian noise with 30")
print("++++++++++++++++++++++++++++++++++++")
box_filter(imgarr_gauss_30, 3, "gauss_30")
box_filter(imgarr_gauss_30, 5, "gauss_30")
print("------------------------------------")
print("salt and pepper noise with 0.1")
print("++++++++++++++++++++++++++++++++++++")
box_filter(imgarr_st_01, 3, "st_01")
box_filter(imgarr_st_01, 5, "st_01")
print("------------------------------------")
print("salt and pepper noise with 0.05")
print("++++++++++++++++++++++++++++++++++++")
box_filter(imgarr_st_05, 3, "st_05")
box_filter(imgarr_st_05, 5, "st_05")

def median(img, k, noise_name):
    pad_size = (k - 1) // 2
    img_padded = expand_with_replicate(img, pad_size)
    result = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            result[i, j] = np.median(img_padded[i:i+k, j:j+k])

    result_img = im.fromarray(result.astype(np.uint8))
    # result_img.show()
    result_img.save(f"./median_{k}_{noise_name}.bmp")

    snr = SNR(img_arr, result)
    print(f"SNR for mdeian filter {k}x{k}: {snr:.6f}")

print("------------------------------------")
print("median filter : ")
print("------------------------------------")
print("gaussian noise with 10")
print("++++++++++++++++++++++++++++++++++++")
median(imgarr_gauss_10, 3, "gauss_10")
median(imgarr_gauss_10, 5, "gauss_10")
print("------------------------------------")
print("gaussian noise with 30")
print("++++++++++++++++++++++++++++++++++++")
median(imgarr_gauss_30, 3, "gauss_30")
median(imgarr_gauss_30, 5, "gauss_30")
print("------------------------------------")
print("salt and pepper noise with 0.1")
print("++++++++++++++++++++++++++++++++++++")
median(imgarr_st_01, 3, "st_01")
median(imgarr_st_01, 5, "st_01")
print("------------------------------------")
print("salt and pepper noise with 0.05")
print("++++++++++++++++++++++++++++++++++++")
median(imgarr_st_05, 3, "st_05")
median(imgarr_st_05, 5, "st_05")

# define the kernel the hw asked
oct_kernel = np.array([[0, 1, 1, 1, 0], 
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [0, 1, 1, 1, 0]])

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

def opening(img, kernel):
    return (dilation(erosion(img, kernel), kernel))

def closing(img, kernel):
    return (erosion(dilation(img, kernel), kernel))

def opening_then_closing(img, noise_name="", kernel=oct_kernel):
    otc_arr = closing(opening(img, kernel), kernel)
    snr = SNR(img_arr/255, otc_arr/255)
    print(f"SNR for opening-then-closing filter : {snr:.6f}")

    otc = im.fromarray(otc_arr)
    otc.save(f"otc_{noise_name}.bmp")

    return otc_arr

def closing_then_opening(img, noise_name="", kernel=oct_kernel):
    cto_arr = opening(closing(img, kernel), kernel)
    snr = SNR(img_arr/255, cto_arr/255)
    print(f"SNR for closing-then-opening filter : {snr:.6f}")

    cto = im.fromarray(cto_arr)
    cto.save(f"cto_{noise_name}.bmp")

    return cto_arr

print("------------------------------------")
print("opening-then-closing filter : ")
print("------------------------------------")
print("gaussian noise with 10")
print("++++++++++++++++++++++++++++++++++++")
opening_then_closing(imgarr_gauss_10, "gauss_10")
print("------------------------------------")
print("gaussian noise with 30")
print("++++++++++++++++++++++++++++++++++++")
opening_then_closing(imgarr_gauss_30, "gauss_30")
print("------------------------------------")
print("salt and pepper noise with 0.1")
print("++++++++++++++++++++++++++++++++++++")
opening_then_closing(imgarr_st_01, "st_01")
print("------------------------------------")
print("salt and pepper noise with 0.05")
print("++++++++++++++++++++++++++++++++++++")
opening_then_closing(imgarr_st_05, "st_05")


print("------------------------------------")
print("closing-then-opening filter : ")
print("------------------------------------")
print("gaussian noise with 10")
print("++++++++++++++++++++++++++++++++++++")
closing_then_opening(imgarr_gauss_10, "gauss_10")
print("------------------------------------")
print("gaussian noise with 30")
print("++++++++++++++++++++++++++++++++++++")
closing_then_opening(imgarr_gauss_30, "gauss_30")
print("------------------------------------")
print("salt and pepper noise with 0.1")
print("++++++++++++++++++++++++++++++++++++")
closing_then_opening(imgarr_st_01, "st_01")
print("------------------------------------")
print("salt and pepper noise with 0.05")
print("++++++++++++++++++++++++++++++++++++")
closing_then_opening(imgarr_st_05, "st_05")
