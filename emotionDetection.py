#https://towardsdatascience.com/face-detection-recognition-and-emotion-detection-in-8-lines-of-code-b2ce32d4d5de
from fer import FER
import cv2

class EmotionDetection():
    def __init__(self):

        self.detector = FER()

    def detect(self):
        self.img = cv2.imread("image/image.jpg")
        self.detector.detect_emotions(self.img)
        emotion, score = self.detector.top_emotion(self.img)
        print("The emotion of the person:", emotion)