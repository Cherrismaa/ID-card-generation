import cv2
import matplotlib.pyplot as plt
img = cv2.imread("idcard.jpg")
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
plt.imshow(img)
plt.show()
