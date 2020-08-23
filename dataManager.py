import glob
import os
import shutil
import config

class DataManager():

    def __init__(self):

        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists('data/training_data'):
            os.makedirs('data/training_data')

        if not os.path.exists('data/training_data/showingTeeth'):
            os.makedirs('data/training_data/showingTeeth')

        if not os.path.exists('data/training_data/notShowingTeeth'):
            os.makedirs('data/training_data/notShowingTeeth')

        if not os.path.exists('data/validation_data/showingTeeth'):
            os.makedirs('data/validation_data/showingTeeth')

        if not os.path.exists('data/validation_data/notShowingTeeth'):
            os.makedirs('data/validation_data/notShowingTeeth')

        self.training_images = glob.glob("/home/anonymous/PycharmProjects/TeethClassifierCNN/img/training_data/*")
        self.validation_images = glob.glob("/home/anonymous/PycharmProjects/TeethClassifierCNN/img/validation/*")

    def manage(self):
        for image in self.training_images[0:5000]:
            if 'showingteeth' in image:
                shutil.copy(image, config.SHOW_TEETH_TRAIN_DIRECTORY)
            else:
                shutil.copy(image, config.NOT_SHOW_TEETH_TRAIN_DIRECTORY)

        for image in self.validation_images[0:500]:
            if 'showingteeth' in image:
                shutil.copy(image, config.SHOW_TEETH_VAL_DIRECTORY)
            else:
                shutil.copy(image, config.NOT_SHOW_TEETH_VAL_DIRECTORY)