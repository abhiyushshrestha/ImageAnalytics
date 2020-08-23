import face_recognition
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt
import config

class FaceRecognition():

    def __init__(self):

        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def recognizeFace(self):
        self.img = face_recognition.load_image_file(config.ORG_IMAGE)
        face_locations = face_recognition.face_locations(self.img)
        top1, right1, bottom1, left1 = face_locations[0]
        self.face_image = self.img[top1:bottom1, left1:right1]
        roi = {
            'top': top1,
            'right': right1,
            'bottom': bottom1,
            'left' : left1
        }
        plt.imshow(self.face_image)
        cv2.imwrite('image/face.jpg', self.face_image)
        return roi, self.face_image

    def checkFaceRatio(self):
        original_img = self.img.shape[0] * self.img.shape[1] * self.img.shape[2]
        face_image = self.face_image.shape[0] * self.face_image.shape[1] * self.face_image.shape[2]
        ratio = face_image / original_img

        if (ratio < 0.5):
            print("Score of face quality being too small - {:0.2f}".format(ratio))
        else:
            print("score of face quality is fine{:0.2f}".format(ratio))

    def recognizeMouth(self):
        img = cv2.imread(config.ORG_IMAGE)
        img = imutils.resize(img, width=500)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 1)
        for (i, rect) in enumerate(rects):
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            (x, y, w, h) = cv2.boundingRect(np.array([shape[48:68]]))  # (48 to 68 is number of region for mouth)
            roi = img[y:y + h, x:x + w]
            roi = imutils.resize(roi, height=250, width=250, inter=cv2.INTER_CUBIC)
            plt.imshow(roi)
            cv2.imwrite(config.MOUTH_IMAGE, roi)
