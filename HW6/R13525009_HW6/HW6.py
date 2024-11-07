from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt

img = im.open("./lena.bmp")
img_arr = np.array(img)

img_arr_binary = (img_arr >= 128).astype(np.uint8) * 255
# img_binary = im.fromarray(img_arr_binary)
# img_binary.show()

downsample = np.zeros((64, 64), dtype=np.uint8)
for i in range(64):
    for j in range(64):
        downsample[i, j] = img_arr_binary[i * 8, j * 8]

# Yokoi Connectivity 
def yokoi_connectivity(pixel, img, x, y):
    def h(b, c, d, e):
        if b == c and (b != d or b != e):
            return 1
        elif b == c == d == e:
            return 2
        else:
            return 0
    
    if pixel == 0:
        return 0

    neighbors = {
        "r": img[x, y+1] if y + 1 < 64 else 0,
        "q": img[x-1, y] if x - 1 >= 0 else 0,
        "s": img[x, y-1] if y - 1 >= 0 else 0,
        "t": img[x+1, y] if x + 1 < 64 else 0
    }

    # Count number
    count = sum([
        h(pixel, neighbors["r"], neighbors["t"], neighbors['q']),
        h(pixel, neighbors["q"], neighbors["s"], neighbors['r']),
        h(pixel, neighbors["s"], neighbors["t"], neighbors['q']),
        h(pixel, neighbors["t"], neighbors["r"], neighbors['s'])
    ])

    return 5 if count == 4 else count

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
plt.gca()
plt.savefig("./result.png")
plt.show()
