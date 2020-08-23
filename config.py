import os

USERNAME = "abhiyushshrestha@gmail.com"
PASSWORD = "*****"
LOGIN_URL = "https://www.linkedin.com/login"

WEIGHT_NAME = "/home/anonymous/PycharmProjects/ImageAnalytics/teeth_classifier_I2.h5"

BASE_DIRECTORY = "/home/anonymous/PycharmProjects"
SHOW_TEETH_TRAIN = "ImageAnalytics/data/training_data/showingTeeth"
NOT_SHOW_TEETH_TRAIN= "ImageAnalytics/data/training_data/notShowingTeeth"
SHOW_TEETH_TRAIN_DIRECTORY = os.path.join(BASE_DIRECTORY, SHOW_TEETH_TRAIN)
NOT_SHOW_TEETH_TRAIN_DIRECTORY = os.path.join(BASE_DIRECTORY, NOT_SHOW_TEETH_TRAIN)

SHOW_TEETH_VAL = "ImageAnalytics/data/validation_data/showingTeeth"
NOT_SHOW_TEETH_VAL = "ImageAnalytics/data/validation_data/notShowingTeeth"
SHOW_TEETH_VAL_DIRECTORY = os.path.join(BASE_DIRECTORY, SHOW_TEETH_VAL)
NOT_SHOW_TEETH_VAL_DIRECTORY = os.path.join(BASE_DIRECTORY, NOT_SHOW_TEETH_VAL)

ORG_IMAGE = "image/image.jpg"
MOUTH_IMAGE = "image/mouth.jpg"