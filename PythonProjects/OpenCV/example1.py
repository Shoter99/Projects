import cv2
import os
img = cv2.imread(os.path.join("Resources", "img.jpg"))
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('NormalImage', img)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)
cv2.imshow("Blur", imgBlur)
cv2.waitKey(0)
        

