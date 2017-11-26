import scipy.io as scio
import numpy as np
from scipy import misc

from keras import applications
from keras.models import Sequential, Model, load_model 
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras import backend as k 

from cnn_methods import load_data
from cnn_methods import instantiate_model

import os 

model_final = load_model("vgg16_1.h5")

input_array, labels = load_data("InputData.mat")

happy_dog_file = open('./happy_dog_database.txt', 'x')
sad_dog_file = open('./sad_dog_database.txt', 'x')

for filename in os.listdir("C:/Users/sagar_000/Documents/UniversityWork/4thYear/Hackathon/TrainingImages/sad_dog"):
	image = misc.imread('./sad_dog/' + filename)
	image = misc.imresize(image, (50,80))
	list_element = model_final.predict(image[None, :, : , :])
	print(list_element[0][0])
	print(str(list_element[0][0]).split())
	sad_dog_file.write(filename + ',' + str(list_element[0][0]) + ',' + str(list_element[0][1]) + '\n')

for filename in os.listdir("C:/Users/sagar_000/Documents/UniversityWork/4thYear/Hackathon/TrainingImages/happy_dog"):
	image = misc.imread('./happy_dog/' + filename)
	image = misc.imresize(image, (50,80))
	list_element = model_final.predict(image[None, :, : , :])
	print(list_element[0][0])
	print(str(list_element[0][0]).split())
	happy_dog_file.write(filename + ',' + str(list_element[0][0]) + ',' + str(list_element[0][1]) + '\n')	

print(happy_dog_database)

#np.savetxt("database_predictions.csv", database, delimiter=",")
#np.savetxt("database_images.csv", input_array, delimiter=",")