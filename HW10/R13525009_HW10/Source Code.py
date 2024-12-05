import numpy as np
from PIL import Image as im

lena = im.open("./lena.bmp")
lena_arr = np.array(lena)
img_size0, img_size1 = lena_arr.shape

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

def my_conv(img_arr, mask, threshold):    
    mk, nk = mask.shape
    mi, ni = img_arr.shape
    m = mi - mk + 1
    n = ni - nk + 1
    res = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            tmp = 0
            for k in range(mk):
                for l in range(nk):
                    tmp += mask[k, l] * img_arr[i+k, j+l]
            if tmp >= threshold:
                res[i, j] = 1
            elif tmp <= -threshold:
                res[i, j] = -1
    return res

def laplace1(img_arr, threshold):
    mask = np.array([[0, 1, 0], 
                     [1, -4, 1], 
                     [0, 1, 0]])
    
    # Expand the image
    img_arr = expand_with_replicate(img_arr, 1)
    
    # Using convolution
    res1 = my_conv(img_arr, mask, threshold)

    res1 = expand_with_replicate(res1, 1)
    res2 = np.ones((img_size0, img_size1))

    # Neighbor checking
    for i in range(img_size0):
        for j in range(img_size1):
            if res1[i + 1, j + 1] == 1:
                tmp = False
                for k in range(3):
                    for l in range(3):
                        if res1[i + k, j + l] == -1:
                            tmp = True
                            break
                    if tmp:
                        break
                if tmp:
                    res2[i, j] = 0

    return res2 * 255

img_arr_laplace1 = laplace1(lena_arr, 15)
img_laplace1 = im.fromarray(img_arr_laplace1.astype(np.uint8))
# img_laplace1.save("./img_laplace1.bmp")
# img_laplace1.show()

def laplace2(img_arr, threshold):
    mask = np.array([[1, 1, 1],
                     [1, -8, 1],
                     [1, 1, 1]], dtype=np.float64)
    mask /= 3
    
    # Expand input for padding using numpy
    img_arr = expand_with_replicate(img_arr, 1)
    
    # Perform convolution using numpy array
    res1 = my_conv(img_arr, mask, threshold)
    
    # Expand result for neighbor checking using numpy
    res1 = expand_with_replicate(res1, 1)
    res2 = np.ones((img_size0, img_size1))  # Initialize with ones
    
    # Neighbor checking
    for i in range(img_size0):
        for j in range(img_size1):
            if res1[i + 1, j + 1] == 1:
                tmp = False
                for k in range(3):
                    for l in range(3):
                        if res1[i + k, j + l] == -1:
                            tmp = True
                            break
                    if tmp:
                        break
                if tmp:
                    res2[i, j] = 0

    return res2 * 255

img_arr_laplace2 = laplace2(lena_arr, 15)
img_laplace2 = im.fromarray(img_arr_laplace2.astype(np.uint8))
# img_laplace2.save("./img_laplace2.bmp")
# img_laplace2.show()

def minimum_variance_laplacian(img_arr, threshold):
    mask = np.array([[2, -1, 2], 
                     [-1, -4, -1], 
                     [2, -1, 2]], dtype=np.float64)
    mask /= 3
    
    # Expand input for padding using numpy
    img_arr = expand_with_replicate(img_arr, 1)
    
    # Perform convolution using numpy array
    res1 = my_conv(img_arr, mask, threshold)
    
    # Expand result for neighbor checking using numpy
    res1 = expand_with_replicate(res1, 1)
    res2 = np.ones((img_size0, img_size1))  # Initialize with ones
    
    # Neighbor checking
    for i in range(img_size0):
        for j in range(img_size1):
            if res1[i + 1, j + 1] == 1:
                tmp = False
                for k in range(3):
                    for l in range(3):
                        if res1[i + k, j + l] == -1:
                            tmp = True
                            break
                    if tmp:
                        break
                if tmp:
                    res2[i, j] = 0

    return res2 * 255

img_arr_minimum_variance_laplacian = minimum_variance_laplacian(lena_arr, 20)
img_minimum_variance_laplacian = im.fromarray(img_arr_minimum_variance_laplacian.astype(np.uint8))
# img_minimum_variance_laplacian.save("./img_minimum_variance_laplacian.bmp")
# img_minimum_variance_laplacian.show()

def laplace_gauss(img_arr, threshold):
    mask = np.array([[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0], 
                     [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0], 
                     [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0], 
                     [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1], 
                     [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1], 
                     [-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2], 
                     [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1], 
                     [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1], 
                     [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0], 
                     [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
                     [0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]])
    
    # Expand input for padding using numpy
    img_arr = expand_with_replicate(img_arr, 5)
    
    # Perform convolution using numpy array
    res1 = my_conv(img_arr, mask, threshold)
    
    # Expand result for neighbor checking using numpy
    res1 = expand_with_replicate(res1, 5)
    res2 = np.ones((img_size0, img_size1))  # Initialize with ones
    
    # Neighbor checking
    for i in range(img_size0):
        for j in range(img_size1):
            if res1[i + 1, j + 1] == 1:
                tmp = False
                for k in range(3):
                    for l in range(3):
                        if res1[i + k, j + l] == -1:
                            tmp = True
                            break
                    if tmp:
                        break
                if tmp:
                    res2[i, j] = 0

    return res2 * 255
    
img_arr_laplace_gauss = laplace_gauss(lena_arr, 3000)
img_laplace_gauss = im.fromarray(img_arr_laplace_gauss.astype(np.uint8))
# img_laplace_gauss.save("./img_laplace_gauss.bmp")
# img_laplace_gauss.show()

def difference_gauss(img_arr, threshold):
    mask = np.array([[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
                     [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3], 
                     [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4], 
                     [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
                     [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7], 
                     [-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8], 
                     [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7], 
                     [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6], 
                     [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4], 
                     [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3], 
                     [-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]])
    
    # Expand input for padding using numpy
    img_arr = expand_with_replicate(img_arr, 5)
    
    # Perform convolution using numpy array
    res1 = my_conv(img_arr, mask, threshold)
    
    # Expand result for neighbor checking using numpy
    res1 = expand_with_replicate(res1, 5)
    res2 = np.ones((img_size0, img_size1))  # Initialize with ones
    
    # Neighbor checking
    for i in range(img_size0):
        for j in range(img_size1):
            if res1[i + 1, j + 1] == 1:
                tmp = False
                for k in range(3):
                    for l in range(3):
                        if res1[i + k, j + l] == -1:
                            tmp = True
                            break
                    if tmp:
                        break
                if tmp:
                    res2[i, j] = 0

    return res2 * 255

img_arr_difference_gauss = difference_gauss(lena_arr, 1)
img_difference_gauss = im.fromarray(img_arr_difference_gauss.astype(np.uint8))
# img_difference_gauss.save("./img_difference_gauss.bmp")
# img_difference_gauss.show()