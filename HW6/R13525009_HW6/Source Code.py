from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt

# Binarize
img = im.open("./lena.bmp")
img_arr = np.array(img)
img_arr_binary = (img_arr >= 128).astype(np.uint8) * 255

# Downsample
downsample = np.zeros((64, 64), dtype=np.uint8)
for i in range(64):
    for j in range(64):
        downsample[i, j] = img_arr_binary[i * 8, j * 8]

# Define the h function
def h(b, c, d, e):
    if b == c and (d != b or e != b):
        return 'q'
    elif b == c and (d == b and e == b):
        return 'r'
    else:
        return 's'

# Yokoi connectivity
def yokoi_connectivity(pixel, img, x, y):
    if pixel == 0:
        return 0

    # Define the neighborhoods
    x0 = pixel
    x1 = img[x, y + 1] if y + 1 < 64 else 0
    x2 = img[x - 1, y] if x - 1 >= 0 else 0
    x3 = img[x, y - 1] if y - 1 >= 0 else 0
    x4 = img[x + 1, y] if x + 1 < 64 else 0
    x5 = img[x + 1, y + 1] if (x + 1 < 64 and y + 1 < 64) else 0
    x6 = img[x - 1, y + 1] if (x - 1 >= 0 and y + 1 < 64) else 0
    x7 = img[x - 1, y - 1] if (x - 1 >= 0 and y - 1 >= 0) else 0
    x8 = img[x + 1, y - 1] if (x + 1 < 64 and y - 1 >= 0) else 0

    # Calculate the output
    a1 = h(x0, x1, x6, x2)
    a2 = h(x0, x2, x7, x3)
    a3 = h(x0, x3, x8, x4)
    a4 = h(x0, x4, x5, x1)

    # Decide the output
    if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
        return 5
    else:
        return sum(1 for a in [a1, a2, a3, a4] if a == 'q')

# Calculate Yokoi connectivity numbers
result = np.full((64, 64), " ", dtype=str)
for i in range(64):
    for j in range(64):
        result[i, j] = str(yokoi_connectivity(downsample[i, j], downsample, i, j))

# plot the result
plt.figure(figsize=(10, 10))
plt.axis('off')

for i in range(64):
    for j in range(64):
        if result[i][j] != '0':  
            plt.text(j, 63 - i, str(result[i][j]), ha='center', va='center', fontsize=8, color='black')

plt.xlim(-1, 64)
plt.ylim(-1, 64)
plt.savefig("./result.png")
# plt.show()
