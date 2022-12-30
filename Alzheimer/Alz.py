# %%
# Import Libraries
import numpy as np 
import pandas as pd 
import time
import itertools

# file system libraries
import os
import os.path
from   os import path
import shutil

# confusion matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# splits train folders into train/validation with stratification
import splitfolders

# Images, Plotting
from skimage import io
import matplotlib.pyplot as plt
import keras.preprocessing
from keras.preprocessing.image import ImageDataGenerator

# tensorflow - CNNs
import tensorflow as tf
import kerastuner as kt
from tensorflow import keras
from keras.models import Model
from keras import backend, models, layers, Sequential
from keras.layers import Input, Concatenate, Dense, Dropout, Flatten, Add
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.callbacks import EarlyStopping,ReduceLROnPlateau
from keras.applications import DenseNet121,InceptionV3, Xception, ResNet101
from kerastuner.tuners import Hyperband 
# %%
# Constants
FOLDERS     = ['train','val','test']
DIR_INPUT   = './Alzheimer_s Dataset'
DIR_WORK    = './'
DIR_MODELS  = os.path.join(DIR_WORK,'models')
DIR_TRAIN   = os.path.join(DIR_WORK,'train')
DIR_VAL     = os.path.join(DIR_WORK,'val')
DIR_TEST    = os.path.join(DIR_WORK,'test')
CLASS_LIST  = ['MildDememted','ModerateDemented','NonDememted','VeryMildDemented']


# Set seeds for reproducibility 
SEED        = 1985
tf.random.set_seed(SEED)
np.random.seed(SEED)