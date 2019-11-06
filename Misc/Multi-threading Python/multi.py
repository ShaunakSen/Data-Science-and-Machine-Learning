from PIL import Image
import numpy as np
import glob
from keras.preprocessing.image import ImageDataGenerator
from multiprocessing.dummy import Pool as ThreadPool

### take a look at the dataset


#### augment the imgs

def augment_images(raw_images, files, mult_factor):
    gen = ImageDataGenerator()