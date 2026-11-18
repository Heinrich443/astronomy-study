import os
from matplotlib import pyplot as plt
import numpy as np
from convenience_functions import show_image
from photutils.aperture import EllipticalAperture

plt.style.use("guide.mplstyle")
seed = os.getenv("GUIDE_RANDOM_SEED", None)

if seed is not None:
    seed = int(seed)

noise_rng = np.random.default_rng(seed)
synthetic_image = np.zeros([1000, 1000])
show_image(synthetic_image, cmap='gray')

plt.show()