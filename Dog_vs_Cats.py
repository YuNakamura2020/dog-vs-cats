from keras import preprocessing
from keras
from matplotlib import pyplot
import sys
from random import random
from shutil import copyfile
from os import listdir
import random
from os import makedirs
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from pathlib import Path
from PIL import Image
from io import BytesIO
from matplotlib.image import imread
import time

# define folder path of datasets
PATH = 'Train/'

# plot first 9 images
for i in range(9):
    # define subplot
    plt.subplot(330 + 1 + i)
    # define filename
    filename = PATH + 'dog.' + str(i) + '.jpg'
    # load image pixels
    image = imread(filename)
    # plot raw pixel data
    plt.imshow(image)

# sho the figure
plt.show()
time.sleep(50)

# create direcctories
dataset_home = 'dataset_dog_vs_cat/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
    # create label subdirectories
    labeldirs = ['dogs/', 'cats/']
    for labldir in labeldirs:
        newdir = dataset_home + subdir + labldir
        makedirs(newdir, exist_ok=True)

# seed random number generator
random.seed(100)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories

src_directory = 'Train/'
for file in listdir(src_directory):
    src = src_directory + file
    dst_dir = 'train/'
    if random() < val_ratio:
        dst_dir = 'test/'
    if file.startswith('cat'):
        dst = dataset_home + dst_dir + 'cats/' + file
        copyfile(src, dst)
    elif file.startswith('dog'):
        dst = dataset_home + dst_dir + 'dogs/' + file
        copyfile(src, dst)

# build baseline model for the dogs vs cats dataset
from keras import preprocessing
from matplotlib import pyplot