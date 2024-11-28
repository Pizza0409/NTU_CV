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
            '''
            r1 = [-1 0
                   0 1]
            r2 = [[0 -1
                   1  0]
            '''
            r1 =  - int(img_arr[i][j]) + int(img_arr[i+1][j+1])
            r2 = - int(img_arr[i][j+1]) + int(img_arr[i+1][j])
            
            grad = np.sqrt(r1**2 + r2**2)
            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr

img_arr_robert = robert(lena_arr, 12)
img_robert = im.fromarray(img_arr_robert.astype(np.uint8))
# img_robert.save("./img_robert.bmp")
# img_robert.show()

def prewitt_edge(img_arr, threshold):
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
            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr

img_arr_prewitt = prewitt_edge(lena_arr, 24)
img_prewitt = im.fromarray(img_arr_prewitt.astype(np.uint8))
# img_prewitt.save("./img_prewitt.bmp")
# img_prewitt.show()

def sobel_edge(img_arr, threshold):
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
            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr    

img_arr_sobel = sobel_edge(lena_arr, 38)
img_sobel = im.fromarray(img_arr_sobel.astype(np.uint8))
# img_sobel.save("./img_sobel.bmp")
# img_sobel.show()

def frel_and_chen_grad(img_arr, threshold):
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
            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr

img_arr_frel_a_chen = frel_and_chen_grad(lena_arr, 30)
img_frel_a_chen = im.fromarray(img_arr_frel_a_chen.astype(np.uint8))
# img_frel_a_chen.save("./img_frel_a_chen.bmp")
# img_frel_a_chen.show()

def kirsch_comass(img_arr, threshold):
    img_arr = expand_with_replicate(img_arr, 1)
    m, n = img_arr.shape
    res_arr = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            '''
            k0 = [-3   -3    5
                  -3    0    5
                  -3   -3    5]
            k1 = [-3    5    5
                  -3    0    5
                  -3   -3   -3]
            k2 = [5     5    5
                 -3     0   -3
                 -3    -3   -3]
            k3 = [5     5   -3
                  5     0   -3
                 -3    -3   -3]
            k4 = [5    -3   -3
                  5     0   -3
                  5    -3   -3]
            k5 = [-3   -3   -3
                   5    0   -3
                   5    5   -3]
            k6 = [-3   -3   -3
                  -3    0   -3
                   5    5    5]
            k7 = [-3   -3   -3
                  -3    0    5
                  -3    5    5]
            '''
            k0 = - 3 * int(img_arr[i, j]) - 3 * int(img_arr[i, j+1]) + 5 * int(img_arr[i, j+2]) \
                - 3 * int(img_arr[i+1, j]) + 5 * int(img_arr[i+1, j+2]) \
                - 3 * int(img_arr[i+2, j]) - 3 * int(img_arr[i+2, j+1]) + 5 * int(img_arr[i+2, j+2])
            k1 = - 3 * int(img_arr[i, j]) + 5 * int(img_arr[i, j+1]) + 5 * int(img_arr[i, j+2]) \
                - 3 * int(img_arr[i+1, j]) + 5 * int(img_arr[i+1, j+2]) \
                - 3 * int(img_arr[i+2, j]) - 3 * int(img_arr[i+2, j+1]) - 3 * int(img_arr[i+2, j+2])
            k2 = 5 * int(img_arr[i, j]) + 5 * int(img_arr[i, j+1]) + 5 * int(img_arr[i, j+2]) \
                - 3 * int(img_arr[i+1, j]) - 3 * int(img_arr[i+1, j+2]) \
                - 3 * int(img_arr[i+2, j]) - 3 * int(img_arr[i+2, j+1]) - 3 * int(img_arr[i+2, j+2])
            k3 = 5 * int(img_arr[i, j]) + 5 * int(img_arr[i, j+1]) - 3 * int(img_arr[i, j+2]) \
                + 5 * int(img_arr[i+1, j]) - 3 * int(img_arr[i+1, j+2]) \
                - 3 * int(img_arr[i+2, j]) - 3 * int(img_arr[i+2, j+1]) - 3 * int(img_arr[i+2, j+2])
            k4 = 5 * int(img_arr[i, j]) - 3 * int(img_arr[i, j+1]) - 3 * int(img_arr[i, j+2]) \
                + 5 * int(img_arr[i+1, j]) - 3 * int(img_arr[i+1, j+2]) \
                + 5 * int(img_arr[i+2, j]) - 3 * int(img_arr[i+2, j+1]) - 3 * int(img_arr[i+2, j+2])
            k5 = - 3 * int(img_arr[i, j]) - 3 * int(img_arr[i, j+1]) - 3 * int(img_arr[i, j+2]) \
                + 5 * int(img_arr[i+1, j]) - 3 * int(img_arr[i+1, j+2]) \
                + 5 * int(img_arr[i+2, j]) + 5 * int(img_arr[i+2, j+1]) - 3 * int(img_arr[i+2, j+2])
            k6 = - 3 * int(img_arr[i, j]) - 3 * int(img_arr[i, j+1]) - 3 * int(img_arr[i, j+2]) \
                - 3 * int(img_arr[i+1, j]) - 3 * int(img_arr[i+1, j+2]) \
                + 5 * int(img_arr[i+2, j]) + 5 * int(img_arr[i+2, j+1]) + 5 * int(img_arr[i+2, j+2])
            k7 = - 3 * int(img_arr[i, j]) - 3 * int(img_arr[i, j+1]) - 3 * int(img_arr[i, j+2]) \
                - 3 * int(img_arr[i+1, j]) + 5 * int(img_arr[i+1, j+2]) \
                - 3 * int(img_arr[i+2, j]) + 5 * int(img_arr[i+2, j+1]) + 5 * int(img_arr[i+2, j+2])

            k_list = np.array([k0, k1, k2, k3, k4, k5, k6, k7])
            grad = np.max(k_list)

            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr

img_arr_kirsch_compass = kirsch_comass(lena_arr, 135)
img_kirsch_compass = im.fromarray(img_arr_kirsch_compass.astype(np.uint8))
# img_kirsch_compass.save("./img_kirsch_compass.bmp")
# img_kirsch_compass.show()

def robinson_compass(img_arr, threshold):
    img_arr = expand_with_replicate(img_arr, 1)
    m, n = img_arr.shape
    res_arr = np.zeros([img_size0, img_size1])

    for i in range(img_size0):
        for j in range(img_size1):
            '''
            r0 = [-1    0     1
                  -2    0     2
                  -1    0     1]
            r1 = [0     1     2
                 -1     0     1
                 -2    -1     0]
            r2 = [1     2     1
                  0     0     0
                 -1    -2    -1]
            r3 = [2     1     0
                  1     0    -1
                  0    -1    -2]
            r4 = [1     0    -1
                  2     0    -2
                  1     0    -1]
            r5 = [0    -1    -2
                  1     0    -1
                  2     1     0]
            r6 = [-1   -2    -1
                   0    0     0
                   1    2     1]
            r7 = [-2   -1     0
                  -1    0     1
                   0    1     2]
            '''
            r0 = - int(img_arr[i, j]) + int(img_arr[i, j+2]) \
                - 2 * int(img_arr[i+1, j]) + 2 * int(img_arr[i+1, j+2]) \
                - int(img_arr[i+2, j]) + int(img_arr[i+2, j+2])
            r1 = int(img_arr[i, j+1]) + 2 * int(img_arr[i, j+2]) \
                - int(img_arr[i+1, j]) + int(img_arr[i+1, j+2]) \
                - 2 * int(img_arr[i+2, j]) - int(img_arr[i+2, j+1])
            r2 = int(img_arr[i, j]) + 2 * int(img_arr[i, j+1]) + int(img_arr[i, j+2]) \
                - int(img_arr[i+2, j]) - 2 * int(img_arr[i+2, j+1]) - int(img_arr[i+2, j+2])
            r3 = 2 * int(img_arr[i, j]) + int(img_arr[i, j+1]) \
                + int(img_arr[i+1, j]) - int(img_arr[i+1, j+2]) \
                - int(img_arr[i+2, j+1]) - 2 * int(img_arr[i+2, j+2])
            r4 = int(img_arr[i, j]) - int(img_arr[i, j+2]) \
                + 2 * int(img_arr[i+1, j]) - 2 * int(img_arr[i+1, j+2]) \
                + int(img_arr[i+2, j]) - int(img_arr[i+2, j+2])
            r5 = - int(img_arr[i, j+1]) - 2 * int(img_arr[i, j+2]) \
                + int(img_arr[i+1, j]) - int(img_arr[i+1, j+2]) \
                + 2 * int(img_arr[i+2, j]) + int(img_arr[i+2, j+1])
            r6 = - int(img_arr[i, j]) - 2 * int(img_arr[i, j+1]) - int(img_arr[i, j+2]) \
                + int(img_arr[i+2, j]) + 2 * int(img_arr[i+2, j+1]) + int(img_arr[i+2, j+2])
            r7 = - 2 * int(img_arr[i, j]) - int(img_arr[i, j+1]) \
                - int(img_arr[i+1, j]) + int(img_arr[i+1, j+2]) \
                + int(img_arr[i+2, j+1]) + 2 * int(img_arr[i+2, j+2])

            r_list = np.array([r0, r1, r2, r3, r4, r5, r6, r7])
            grad = np.max(r_list)

            res_arr[i, j] = 255 if grad < threshold else 0
    
    return res_arr

img_arr_robinson = robinson_compass(lena_arr, 43)
img_robinson = im.fromarray(img_arr_robinson.astype(np.uint8))
# img_robinson.save("./img_robinson.bmp")
# img_robinson.show()

def nevatia_babu_5x5(img_arr, threshold):
# 定義 Nevatia-Babu 算子 
    kernels = [ 
        np.array([[ 100, 100, 100, 100, 100], 
                [ 100, 100, 100, 100, 100], 
                [ 0, 0, 0, 0, 0], 
                [-100, -100, -100, -100, -100], 
                [-100, -100, -100, -100, -100]]), 
        np.array([[ 100, 100, 100, 100, 100], 
                [ 100, 100, 100, 78, -32], 
                [ 100, 92, 0, -92, -100], 
                [ 32, -78, -100, -100, -100], 
                [-100, -100, -100, -100, -100]]),
        np.array([[ 100, 100, 100, 32, -100], 
                [ 100, 100, 92, -78, -100], 
                [ 100, 100, 0, -100, -100], 
                [ 100, 78, -92, -100, -100], 
                [ 100, -32, -100, -100, -100]]), 
        np.array([[-100, -100, 0, 100, 100], 
                [-100, -100, 0, 100, 100], 
                [-100, -100, 0, 100, 100], 
                [-100, -100, 0, 100, 100], 
                [-100, -100, 0, 100, 100]]),
        np.array([[-100, 32, 100, 100, 100], 
                [-100, -78, 92, 100, 100], 
                [-100, -100, 0, 100, 100], 
                [-100, -100, -92, 78, 100], 
                [-100, -100, -100, -32, 100]]), 
        np.array([[ 100, 100, 100, 100, 100], 
                [ -32, 78, 100, 100, 100], 
                [-100, -92, 0, 92, 100], 
                [-100, -100, -100, -78, 32], 
                [-100, -100, -100, -100, -100]]) 
    ] 
    img_arr = expand_with_replicate(img_arr, 2) 
    res_arr = np.zeros([img_size0, img_size1]) 
    for i in range(img_size0): 
        for j in range(img_size1): 
            grads = [] 
            for kernel in kernels: 
                region = img_arr[i:i+5, j:j+5] 
                grad = np.sum(kernel * region) 
                grads.append(grad) 
            max_grad = np.max(grads) 
            res_arr[i, j] = 0 if max_grad > threshold else 255 
    return res_arr

img_arr_nevatia_babu = nevatia_babu_5x5(lena_arr, 12500)
img_nevatia_babu = im.fromarray(img_arr_nevatia_babu.astype(np.uint8))
img_nevatia_babu.save("./img_nevatia_babu.bmp")
img_nevatia_babu.show()