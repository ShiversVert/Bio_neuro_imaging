import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage import data_dir
from skimage.transform import radon, rescale

#image = imread(data_dir + "/phantom.png", as_gray=True)
#image = rescale(image, scale=0.4, mode='reflect', multichannel=False)
image = np.zeros((64, 64))

theta = np.linspace(0., 360., max(image.shape), endpoint=False)

fig, axs = plt.subplots(8, 8)

for i in range(0, 63, 8):
    for j in range(0, 63, 8):
        image = image = np.zeros((64, 64)); image[i][j] = 1;
        
        sinogram = radon(image, theta=theta, circle=True)
        axs[i//8, j//8].imshow(sinogram, cmap=plt.cm.Greys_r,
               extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')

plt.show()