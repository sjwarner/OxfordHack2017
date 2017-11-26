from cnn_methods import load_data
from cnn_methods import instantiate_model
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping

img_width, img_height = 80, 50
batch_size = 16 
nb_epochs = 7

input_array, labels = load_data("InputData.mat")

model_final = instantiate_model()

# compile the model 
model_final.compile(loss = "categorical_crossentropy", optimizer = SGD(lr=0.0001, momentum=0.9), metrics=["accuracy"])

checkpoint = ModelCheckpoint("vgg16_2.h5", monitor='val_acc', verbose=1, save_best_only=False, save_weights_only=False, mode='auto', period=1)
early = EarlyStopping(monitor='val_acc', min_delta=0, patience=10, verbose=1, mode='auto')

print('Commencing model training...')
model_final.fit(input_array, labels,
    batch_size=batch_size,
    nb_epoch=nb_epochs,
    shuffle=True,
    callbacks=[checkpoint])