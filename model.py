import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
import keras
import pickle
import config


from keras import applications
from keras.models import Sequential, load_model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Dense, Activation, Dropout
from keras.layers.normalization import BatchNormalization
from keras import Model
from keras import regularizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image


from sklearn.metrics import confusion_matrix

from itertools import chain
from collections import defaultdict


from keras.callbacks import ModelCheckpoint, CSVLogger, LearningRateScheduler, ReduceLROnPlateau

class Model():

    def __init__(self):
        self.classifier = self.model_classifier(32, 32, 3)

    def model_classifier(self, width, height, channel):
        classifier = Sequential()

        # Step-1 Convolutional layer
        classifier.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(width, height, channel), activation='relu'))
        # classifier.add(Dropout(0.2))
        # Step-2 Maxpooling
        classifier.add(MaxPooling2D(pool_size=(2, 2)))

        # Adding another convolutional layer
        classifier.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
        # classifier.add(Dropout(0.2))
        # Adding another maxpooling layer
        classifier.add(MaxPooling2D(pool_size=(2, 2)))

        # Step-3 Flatten
        classifier.add(Flatten())

        # Step-4 Full connection
        classifier.add(Dense(units=128, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
        classifier.add(Dropout(0.25))
        classifier.add(Dense(units=128, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
        classifier.add(Dropout(0.25))
        classifier.add(Dense(units=2, activation='softmax'))

        return classifier

    def train(self, save_weight_name, save_weights = 'FALSE'):
        self.classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        self.train_datagen = ImageDataGenerator(rescale=1. / 255,
                                                shear_range=0.2,
                                                zoom_range=0.2,
                                                rotation_range=15,
                                                horizontal_flip=True)

        self.validation_datagen = ImageDataGenerator(rescale=1. / 255)


        self.training_set = self.train_datagen.flow_from_directory(
            "/home/anonymous/PycharmProjects/ImageAnalytics/data/training_data",
            target_size=(32, 32),
            batch_size=32,
            class_mode='categorical')

        self.validation_set = self.validation_datagen.flow_from_directory(
            "/home/anonymous/PycharmProjects/ImageAnalytics/data/validation_data",
            target_size=(32, 32),
            batch_size=32,
            class_mode='categorical')

        history = self.classifier.fit_generator(self.training_set,
                                           steps_per_epoch=int(self.training_set.samples),
                                           epochs=2,
                                           validation_data=self.validation_set,
                                           validation_steps=int(self.validation_set.samples))

        if save_weights:
            self.classifier.save_weights(save_weight_name)

    def load_weights(self, weights_name):
        self.classifier.load_weights(weights_name)

    def predict(self):
        result_value = {
            0: "NOT SHOWING TEETH",
            1: "SHOWING TEETH"
        }
        test_image = image.load_img(config.MOUTH_IMAGE, target_size=(32, 32))
        plt.imshow(test_image)
        test_image_array = np.array(test_image)
        test_image_array = test_image_array / 255.0
        test_image_array_expand_dims = np.expand_dims(test_image_array, axis=0)

        result = self.classifier.predict(test_image_array_expand_dims)
        print("The result is :", result)
        print(result_value[result.argmax()])
