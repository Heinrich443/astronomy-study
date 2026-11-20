import os
from matplotlib import pyplot as plt
import numpy as np
from convenience_functions import show_image
from photutils.aperture import EllipticalAperture

def read_noise(image, amount, gain=1):
    """
    Generate simulated read noise.

    Parameters
    ----------

    image: numpy array
        Image whose shape the noise array should match.
    amount : float
        Amount of read noise, in electrons.
    gain : float, optional
        Gain of the camera, in units of electrons/ADU.
    """
    shape = image.shape
    noise = noise_rng.normal(scale=amount/gain, size=shape)
    return noise

def bias(image, value, realistic=False):
    """
    Generate simulated bias image.

    Parameters
    ----------

    image: numpy array
        Image whose shape the bias array should match.
    value: float
        Bias level to add.
    realistic : bool, optional
        If ``True``, add some columns with somewhat higher bias value (a not uncommon thing)
    """
    # This is the whole thing: the bias is really suppose to be a constant offset!
    bias_im = np.zeros_like(image) + value

    # If we want a more realistic bias we need to do a little more work.
    if realistic:
        shape = image.shape
        number_of_columns = 5

        # We want a random-looking variation in the bias,
        # but unlike the readnoise the bias should *not* change from image to image,
        # so we make sure to always generate the same "random" numbers.
        rng = np.random.RandomState(seed=8392)
        columns = rng.randint(0, shape[1], size=number_of_columns)

        # This adds a little random-looking noise into the data.
        col_pattern = rng.randint(0, int(0.1 * value), size=shape[0])

        # Make the chosen columns a little brighter than the rest...
        for c in columns:
            bias_im[:, c] = value + col_pattern

    return bias_im

def dark_current(image, current, exposure_time, gain=1.0, hot_pixels=False):
    """
    Simulate dark current in a CCD, optionally including hot pixels.

    Parameters
    ----------

    image : numpy array
        Image whose shape the cosmic array should match.
    current : float
        Dark current, in electrons/pixel/second, which is the way manufacturers typically
        report it.
    exposure_time : float
        Length of the simulated exposure, in seconds.
    gain : float, optional
        Gain of the camera, in units of electrons/ADU.
    strength : float, optional
        Pixel count in the cosmic rays.
    """

    # dark current for every pixel;
    # we'll modify the current for some pixels if the user wants hot pixels.
    base_current = current * exposure_time / gain

    # This random number generation should change on each call.
    dark_im = noise_rng.poisson(base_current, size=image.shape)
    if hot_pixels:
        # We'll set 0.01% of the pixels to be hot;
        # that is probably too high but should ensure they are visible.
        y_max, x_max = dark_im.shape
        n_hot = int(0.0001 * x_max * y_max)

        # Like with the bias image, we want the hot pixels to always be in the same places
        # (at least for the same image size) but also want them to appear to be randomly
        # distributed. So we set a random number seed to ensure we always get the same thing.
        rng = np.random.RandomState(16201649)
        hot_x = rng.randint(0, x_max, size=n_hot)
        hot_y = rng.randint(0, y_max, size=n_hot)

        hot_current = 10000 * current
        dark_im[(hot_y, hot_x)] = hot_current * exposure_time / gain
    return dark_im

def sky_background(image, sky_counts, gain=1):
    """
    Generate sky background, optionally including a gradient across the image (because
    some times Moons happen).

    Parameters
    ----------

    image : numpy array
        Image whose shape the cosmic array should match.
    sky_counts : float
        The target value for the number of counts (as opposed to electrons or
        photons) from the sky.
    gain : float, optional
        Gain of the camera, in units of electrons/ADU.
    """
    sky_im = noise_rng.poisson(sky_counts * gain, size=image.shape) / gain

    return sky_im

plt.style.use("guide.mplstyle")
seed = os.getenv("GUIDE_RANDOM_SEED", None)

if seed is not None:
    seed = int(seed)

# generate an empty image
noise_rng = np.random.default_rng(seed)
synthetic_image = np.zeros([1000, 1000])
show_image(synthetic_image, cmap='gray')

# add read noise
plt.figure()
noise_im = synthetic_image + read_noise(synthetic_image, 5)
show_image(noise_im, cmap='gray')

# bias only
bias_only = bias(synthetic_image, 1100, realistic=True)
show_image(bias_only, cmap='gray', figsize=(10, 10))
plt.title('Bias only, bad columns included', fontsize='20')

# add bias
bias_noise_im = noise_im + bias_only
show_image(bias_noise_im, cmap='gray', figsize=(10, 10))
plt.title('Realistic bias frame (includes read noise)', fontsize='20')

# dark current only
dark_exposure = 100
dark_cur = 0.1
dark_only = dark_current(synthetic_image, dark_cur, dark_exposure, hot_pixels=True)
show_image(dark_only, cmap='gray')
title_string = "Dark current only, {dark_cur} $e^-$/sec/pix\n{dark_exposure} sec exposure".format(dark_cur=dark_cur, dark_exposure=dark_exposure)
plt.title(title_string, fontsize='20')

# add dark current
dark_bias_noise_im = bias_noise_im + dark_only
show_image(dark_bias_noise_im, cmap='gray')
plt.title('Realistic dark frame \n(with bias, read noise)', fontsize='20')

# sky background only
sky_level = 20
sky_only = sky_background(synthetic_image, sky_level)
show_image(sky_only, cmap='gray')
plt.title("Sky background only, {} counts input.".format(sky_level), fontsize='20')

# add sky background
sky_dark_bias_noise_im = dark_bias_noise_im + sky_only
show_image(sky_dark_bias_noise_im, cmap='gray')
plt.title('Sky, dark, bias and noise\n(Realistic image of clouds)', fontsize='20')
plt.show()