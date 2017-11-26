import scipy.io as scio
import numpy as np

from keras import applications
from keras.models import Sequential, Model 
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D, Convolution2D, Activation, MaxPooling2D
from keras import backend as k 
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping

def load_data(filename):
	file = scio.loadmat(filename)

	input_array_interm = file['image_array']
	input_array = np.array(input_array_interm)

	labels_interm = file['labels']
	labels = np.array(labels_interm)

	return input_array, labels

def instantiate_model(): 
	img_width, img_height = 80, 50
	batch_size = 16 
	epochs = 10

	model = applications.VGG16(weights = "imagenet", include_top=False, input_shape = (img_height, img_width, 3))
	   
	for layer in model.layers[:5]:
		 layer.trainable = False

	#Adding custom Layers 
	x = model.output
	x = Convolution2D(64, 3, 3, border_mode='same', name='conv2')(x)
	x = Activation('relu', name='act_2')(x)
	x = Flatten()(x)
	x = Dense(1024, activation="relu")(x)
	x = Dropout(0.5)(x)
	x = Dense(1024, activation="relu")(x)
	predictions = Dense(2, activation="sigmoid")(x)

	# creating the final model 
	model_final = Model(input = model.input, output = predictions)

	return model_final

def load_image( infilename ) :
	
   from scipy import misc
   image = misc.imread(infilename) # 640x480x3 array
	