# Import some awesome packages
import numpy as np
import cv2

# RGBHistogram class (WOW)
class RGBHistogram:

    """
        In the constructor we initialise
        the number of bins used per each
        channel. Hence, the bins parame-
        ter given is list containing 3 i-
        ntegers.
    """
    def __init__(self, bins):
        self.bins = bins

    """
        In describe method, we proceed in
        computing the desription of our -
        image. In the following case our
        descriptor will be a 3D RGB histogram
        which "describes" the color space of
        our image.
    """
    def describe(self, image):

        # Compute histogram for the image
        hist = cv2.calcHist([image], [0, 1, 2],
                            None, self.bins, [0, 256, 0, 256, 0, 256])

        # Normalise histogram for scale invariance
        # a.k.a get the same histogram for the same
        # image but different sizes
        hist = cv.normalize(hist)

        # Return flattened numpy array
        # for our human-dumb computational
        # ease
        return hist.flatten()
