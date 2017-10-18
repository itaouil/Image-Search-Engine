# Import amazin packages
from rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2

# Set up our user friendly argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path of the directory containing the dataset images.")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the serialisation is stored.")
args = vars(ap.parse_args())

# Declare our dictonaries, containing computed histograms
index = {}

# Create our image descriptor instance
# with 8 bins per colour channel
desc = RGBHistogram([8, 8, 8])

# Loop over image dataset and compute 3D histogram
for imagePath in glob.glob(args["dataset"] + "/*.jpeg"):
    # Get image filename
    k = imagePath[imagePath.rfind("/") + 1:]

    # Load image and compute its
    # features vector
    image    = cv2.imread(imagePath)
    features = desc.describe(image)

    # Store filename/histogram pair
    index[k] = features

# Serialise our index dictionary
f = open(args["index"], "wb")
f.write(cPickle.dumps(index))
f.close()
