import cv2
import numpy as np
import face_recognition

imgSin = face_recognition.load_image_file('sh.png')
imgSin = cv2.cvtColor(imgSin, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('sh.png')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

cv2.imshow('sinmina', imgSin)
cv2.imshow('sinmina_test', imgTest)
cv2.waitKey(0)