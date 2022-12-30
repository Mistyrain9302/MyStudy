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
# %%
def images_by_class(path,folders):
    """
    각 경로/폴더마다 각 클래스(분류)의 수와 비율을 반복 계산하는 함수
    """
    # accumulators (계산 축적)
    normal,verymild,mild,moderate =0,0,0,0
    # print header (공백을 넣어서 윤곽 맞추기)
    msg = '{:8} {:8} {:11} {:7} {:9} {:9} {:11} {:8} {:8}'.format('folder','normal','verymild','mild','moderate',
                                                                  'normal %','verymild %','mild %','moderate %')
    print(msg)  
    print("-"*len(msg))
    
    for folder in folders:
        for dirname,_, filenames in os.walk(os.path.join(path,folder)):
            for file in filenames:
                if "NonDemented" in dirname:
                    normal+=1
                if "VeryMildDemented" in dirname:
                    verymild+=1
                if 'MildDemented' in dirname:
                    mild+=1
                if 'ModerateDemented' in dirname:
                    moderate+=1
        # calculate total and percentages            
        total = normal+verymild+mild+moderate
        if total >0:
            n  = round(normal/total,2)*100
            vm = round(verymild/total,2)*100
            m  = round(mild/total,2)*100
            mo =round(moderate/total,2)*100
        else:
            n,vm,m,mo = 0,0,0,0
            
        print("{:6} {:8} {:10} {:7} {:11} {:8} {:10} {:8} {:12}".format(folder,normal,verymild,mild,moderate,n,vm,m,mo))
        normal,verymild,mild,moderate =0,0,0,0
# %%
# Images by class in the input directory
images_by_class(DIR_INPUT,FOLDERS)
# %%
# create a new directory if it doesn't exist
def create_dir(dir_path,folder,verbose=True):
    """
    dir_path/folder가 없을 경우 새로 생성
    """
    msg = ""
    folder_path = os.path.join(dir_path,folder)
    if not path.exists(folder_path):
        try:
            os.mkdir(folder_path)
            msg = folder_path + ' created'
        except OSError as err:
            print('Error creating folder:{} with error:{}'.format(folder_path,err))
    if verbose:
        print(msg)
        
    return folder_path
# %%
# create model directory
create_dir(DIR_INPUT,'models',True)
# %%
