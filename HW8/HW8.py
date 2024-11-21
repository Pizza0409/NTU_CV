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
def gaussian_noise(img, amp):
    img_gauss_arr = np.zeros([img_size0, img_size1])
    for i in range(img_size0):
        for j in range(img_size1):
            img_gauss_arr[i, j] = max(0, min(255, img_arr[i, j] + amp * random.gauss(0, 1)))

    snr = SNR(img_arr, img_gauss_arr)
    print("SNR for Gaussian noisy with amp = {amp} is {snr}.".format(amp=amp, snr=snr))
    img_gauss = im.fromarray(np.array(img_gauss_arr, dtype=np.uint8))
    img_gauss.save("./gauss_{amp}.bmp".format(amp=amp))
    img_gauss.show()

gaussian_noise(img, 10)
gaussian_noise(img, 30)

def salt_and_pepper(img, threshold):
    
