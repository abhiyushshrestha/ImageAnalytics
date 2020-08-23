from scrapper import Scrapper
from dataManager import DataManager
from faceRecognition import FaceRecognition
from filterImage import FilterImage
from emotionDetection import EmotionDetection
from model import Model
import config
import argparse
from time import sleep
class Main:
    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-train", "--train", required=True,
                        help="whether to train a model or not")
        self.args = vars(ap.parse_args())

        self.scrapper = Scrapper()
        # self.dataManager = DataManager()
        self.filterImage = FilterImage()
        self.faceRecognition = FaceRecognition()
        self.emotionDetection = EmotionDetection()
        self.model = Model()
    def run(self):
        self.scrapper.scrape()
        # self.dataManager.manage()
        roi_face, face_image = self.faceRecognition.recognizeFace()
        self.filterImage.blurImage(roi_face)
        self.faceRecognition.checkFaceRatio()
        self.emotionDetection.detect()
        self.faceRecognition.recognizeMouth()

        if self.args['train'] == '1':
            save_weights_name = input("Enter the name for weights: ")
            self.model.train(save_weights_name, save_weights = 'TRUE')
        self.model.load_weights(config.WEIGHT_NAME)
        self.model.predict()
        pass
if __name__ == '__main__':
    m = Main()
    m.run()
