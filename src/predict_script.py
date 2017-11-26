import scipy.io as scio
import numpy as np
from scipy import misc

from keras import applications
from keras.models import Sequential, Model, load_model 
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras import backend as k 

from cnn_methods import load_data
from cnn_methods import instantiate_model

model_final = load_model("vgg16_1.h5")

input_array, labels = load_data("InputData.mat")

test = misc.imread('75.jpg')

test = misc.imresize(test, (50,80))

print(model_final.predict(test[None, :, : , :]))


