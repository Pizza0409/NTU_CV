from PIL import Image as img
import numpy as np

# Load the image
lena = img.open('lena.bmp')
lena_arr = np.asarray(lena)

# Downsample the image by taking the top-left pixel of each 8x8 block
def downsample(arr):
    m, n = len(arr), len(arr[0])
    result = np.zeros((m // 8, n // 8), dtype=np.uint8)
    # result = [[0] * (n // 8) for _ in range(m // 8)]
    for i in range(m // 8):
        for j in range(n // 8):
            result[i, j] = arr[i * 8, j * 8]
    return result

# Upsample the image back to 512x512 for visualization purposes
def upsample(arr):
    m, n = len(arr), len(arr[0])
    result = np.zeros((m // 8, n // 8), dtype=np.uint8)
    # result = [[0] * (n * 8) for _ in range(m * 8)]
    for i in range(m * 8):
        for j in range(n * 8):
            result[i, j] = arr[i // 8, j // 8]
    return result

# Expand the image array with a border of zeros for boundary conditions
def expand_with_zeros(arr):
    m, n = len(arr), len(arr[0])
    result = [[0] * (n + 2) for _ in range(m + 2)]
    for i in range(m):
        for j in range(n):
            result[i + 1][j + 1] = arr[i][j]
    return result

# Function for computing Yokoi connectivity number
def h(b, c, d, e):
    if b != c:
        return 's'
    else:
        if d == b and e == b:
            return 'r'
        else:
            return 'q'

def f(a1, a2, a3, a4):
    if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
        return 5
    count = sum(1 for a in [a1, a2, a3, a4] if a == 'q')
    return count

def yokoi(arr):
    m, n = len(arr), len(arr[0])
    result = [[0] * n for _ in range(m)]
    arr = expand_with_zeros(arr)
    
    for i in range(m):
        for j in range(n):
            a1 = h(arr[i+1, j+1], arr[i+1, j+2], arr[i, j+2], arr[i, j+1])
            a2 = h(arr[i+1, j+1], arr[i, j+1], arr[i, j], arr[i+1, j])
            a3 = h(arr[i+1, j+1], arr[i+1, j], arr[i+2, j], arr[i+2, j+1])
            a4 = h(arr[i+1, j+1], arr[i+2, j+1], arr[i+2, j+2], arr[i+1, j+2])
            
            tmp = f(a1, a2, a3, a4)
            if tmp and arr[i+1, j+1]:
                result[i, j] = tmp
    return result

# Mark pairs in the Yokoi array for thinning
def mark_pairs(yokoi_arr):
    m, n = len(yokoi_arr), len(yokoi_arr[0])
    result = [[0] * n for _ in range(m)]
    yokoi_arr = expand_with_zeros(yokoi_arr)
    
    for i in range(m):
        for j in range(n):
            if yokoi_arr[i+1, j+1] == 1:
                count = sum(1 for x, y in [(i, j+1), (i+1, j), (i+2, j+1), (i+1, j+2)] if yokoi_arr[x, y] == 1)
                if count >= 1:
                    result[i, j] = 1
    return result

# Helper function for thinning
def h2(b, c, d, e):
    return 1 if b == c and (b != d or b != e) else 0

def f2(a1, a2, a3, a4, x):
    return 0 if a1 + a2 + a3 + a4 == 1 else x

# Perform the thinning process on the image
def thinning_process(original, marked_arr):
    m, n = len(original), len(original[0])
    original = expand_with_zeros(original)
    modified = 0  # Track if changes occur
    
    for i in range(m):
        for j in range(n):
            if marked_arr[i][j]:
                a1 = h2(original[i+1, j+1], original[i+1, j+2], original[i, j+2], original[i, j+1])
                a2 = h2(original[i+1, j+1], original[i, j+1], original[i, j], original[i+1, j])
                a3 = h2(original[i+1, j+1], original[i+1, j], original[i+2, j], original[i+2, j+1])
                a4 = h2(original[i+1, j+1], original[i+2, j+1], original[i+2, j+2], original[i+1, j+2])
                
                temp = f2(a1, a2, a3, a4, original[i+1, j+1])
                if temp != original[i+1, j+1]:
                    modified = 1
                    original[i+1, j+1] = temp
    
    # Remove the zero-padded border
    thinned_result = [[original[i+1, j+1] for j in range(n)] for i in range(m)]
    return thinned_result, modified

# Downsample, apply thinning, and upsample for visualization
binary_lena = (lena_arr // 128) * 255  # Binarize image
downsampled = downsample(binary_lena)
change = 1

while change:
    yokoi_arr = yokoi(downsampled)
    marked_arr = mark_pairs(yokoi_arr)
    downsampled, change = thinning_process(downsampled, marked_arr)

# Upsample for clearer visualization
final_result = upsample(downsampled)
result_image = img.fromarray(np.array(final_result, dtype=np.uint8))
result_image.show()
