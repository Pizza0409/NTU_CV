import numpy as np
from PIL import Image as im

lena = im.open("./lena.bmp")
lena_arr = np.array(lena)

img_size0, img_size1 =  lena_arr.shape

def expand_with_replicate(arr, pad_size):
    m, n = arr.shape
    result = np.zeros((m + 2 * pad_size, n + 2 * pad_size), dtype=arr.dtype)
    # Fill the borders
    result[pad_size:-pad_size, pad_size:-pad_size] = arr
    result[:pad_size, pad_size:-pad_size] = arr[0, :]  # Top edge
    result[-pad_size:, pad_size:-pad_size] = arr[-1, :]  # Bottom edge
    result[pad_size:-pad_size, :pad_size] = arr[:, 0][:, None]  # Left edge
    result[pad_size:-pad_size, -pad_size:] = arr[:, -1][:, None]  # Right edge
    # Fill the corners
    result[:pad_size, :pad_size] = arr[0, 0]    # Top-left corner
    result[:pad_size, -pad_size:] = arr[0, -1]  # Top-right corner
    result[-pad_size:, :pad_size] = arr[-1, 0]  # Bottom-left corner
    result[-pad_size:, -pad_size:] = arr[-1, -1]    # Bottom-right corner
    return result

def robert(img, threshold):
    for i in range(img_size0-2):
        for j in range(img_size1-2):  
                r1 =  -img[i][j] + img[i+1][j+1]
                r2 = -img[i][j+1] + img[i+1][j]
                grad = sqrt(r1**2 + r2**2)