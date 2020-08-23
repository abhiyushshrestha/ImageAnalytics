from PIL import Image,ImageFilter
from faceRecognition import FaceRecognition
import cv2
import numpy as np
class FilterImage():

    def blurImage(self, roi_face):
        orig_img = Image.open('image/image.jpg')
        face_img = orig_img.crop((roi_face['left'], roi_face['top'], roi_face['right'], roi_face['bottom']))
        face_img_array = np.array(face_img)
        cv2.imwrite("image/cropped.jpg", face_img_array)
        print()
        blurred_img = orig_img.filter(ImageFilter.GaussianBlur(radius=4))
        blurred_img.paste(face_img,(roi_face['left'], roi_face['top'], roi_face['right'], roi_face['bottom']))
        blurred_img.show()