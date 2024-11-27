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

def robert(img_arr, threshold):
    res_arr = np.zeros([img_size0, img_size1])
    for i in range(img_size0-1):
        for j in range(img_size1-1):  
            r1 =  - int(img_arr[i][j]) + int(img_arr[i+1][j+1])
            r2 = - int(img_arr[i][j+1]) + int(img_arr[i+1][j])
            grad = np.sqrt(r1**2 + r2**2)

            if grad < threshold:
                res_arr[i, j] = 255
            else:
                res_arr[i, j]= 0
    
    return res_arr

img_arr_robert = robert(lena_arr, 12)
img_robert = im.fromarray(img_arr_robert.astype(np.uint8))
# img_robert.save("./img_robert.bmp")
# img_robert.show()

def prewitts_edge(img_arr, threshold):
    img_arr = expand_with_replicate(img_arr, 1)
    m, n = img_arr.shape
    res_arr = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            '''
            p1 = [-1 -1 -1
                    0 0 0
                    1 1 1]
            p2 = [-1 0 1
                    -1 0 1
                    -1 0 1]
            '''
            p1 = - int(img_arr[i, j]) - int(img_arr[i, j+1]) - int(img_arr[i, j+2]) + int(img_arr[i+2, j]) + int(img_arr[i+2, j+1]) + int(img_arr[i+2, j+2])
            p2 = - int(img_arr[i, j]) - int(img_arr[i+1, j]) - int(img_arr[i+2, j]) + int(img_arr[i, j+2]) + int(img_arr[i+1, j+2]) + int(img_arr[i+2, j+2])

            grad = np.sqrt(p1**2 + p2**2)
            if grad < threshold:
                res_arr[i, j] = 255
            else:
                res_arr[i, j] = 0
    
    return res_arr

img_arr_prewitts = prewitts_edge(lena_arr, 24)
img_prewitts = im.fromarray(img_arr_prewitts.astype(np.uint8))
# img_prewitts.save("./img_prewitts.bmp")
# img_prewitts.show()

def sobels_edge(img_arr, threshold):
    img_arr = expand_with_replicate(img_arr, 1)
    m, n = img_arr.shape
    res_arr = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            '''
            s1 = [-1 -2 -1
                    0 0 0
                    1 2 1]
            s2 = [-1 0 1
                    -2 0 2
                    -1 0 1]
            '''
            s1 = - int(img_arr[i, j]) - 2 * int(img_arr[i, j+1]) - int(img_arr[i, j+2]) + int(img_arr[i+2, j]) + 2 * int(img_arr[i+2, j+1]) + int(img_arr[i+2, j+2])
            s2 = - int(img_arr[i, j]) - 2 * int(img_arr[i+1, j]) - int(img_arr[i+2, j]) + int(img_arr[i, j+2]) + 2 * int(img_arr[i+1, j+2]) + int(img_arr[i+2, j+2])

            grad = np.sqrt(s1**2 + s2**2)
            if grad < threshold:
                res_arr[i, j] = 255
            else:
                res_arr[i, j] = 0
    
    return res_arr    

img_arr_sobels = sobels_edge(lena_arr, 38)
img_sobels = im.fromarray(img_arr_sobels.astype(np.uint8))
# img_sobels.save("./img_sobels.bmp")
# img_sobels.show()

def frel_and_chens_grad(img_arr, threshold):
    img_arr = expand_with_replicate(img_arr, 1)
    m, n = img_arr.shape
    res_arr = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            '''
            s1 = [-1 sqrt(-2)   -1
                    0       0   0
                    1 sqrt(2)   1]
            s2 = [-1        0   1
                sqrt(-)2    0 sqrt(2)
                -1          0   1]
            '''
            s1 = - int(img_arr[i, j]) - np.sqrt(2) * int(img_arr[i, j+1]) - int(img_arr[i, j+2]) + int(img_arr[i+2, j]) + np.sqrt(2) * int(img_arr[i+2, j+1]) + int(img_arr[i+2, j+2])
            s2 = - int(img_arr[i, j]) - np.sqrt(2) * int(img_arr[i+1, j]) - int(img_arr[i+2, j]) + int(img_arr[i, j+2]) + np.sqrt(2) * int(img_arr[i+1, j+2]) + int(img_arr[i+2, j+2])

            grad = np.sqrt(s1**2 + s2**2)
            if grad < threshold:
                res_arr[i, j] = 255
            else:
                res_arr[i, j] = 0
    
    return res_arr

img_arr_frel_a_chens = frel_and_chens_grad(lena_arr, 30)
img_frel_a_chens = im.fromarray(img_arr_frel_a_chens.astype(np.uint8))
img_frel_a_chens.save("./img_frel_a_chens.bmp")
img_frel_a_chens.show()