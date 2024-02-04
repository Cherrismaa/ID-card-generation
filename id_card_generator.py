#  pip install opencv-contrib-python
#  pip install matplotlib
#  pip install pandas
#  pip install numpy


import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def text(img,word,position,color):
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img,word,position, font, 0.4,color,1,cv2.LINE_AA)
data = pd.read_csv("student_data.csv").values
for students in data:
    print("Students : " , students[-1])
    img = cv2.imread("idcard.jpg").copy()
    student_img = cv2.imread("photos/"+students[-1]).copy()
    student_img = cv2.resize(student_img,(125,159))
    img[175:334,303:428] = student_img
    text(img,students[0],(143,265),(255,255,255))
    text(img,students[1],(143,287),(255,255,255))
    text(img,students[2],(143,308),(255,255,255))
    text(img,students[3],(143,329),(255,255,255))
    cv2.imwrite("id_cards/"+students[-1],img)

print("ID card generation completed")
