import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("resources/test_image.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img_gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

# cv2.imshow("Image", img)
cv2.imshow("Image Gray", img_gray)
cv2.waitKey(0)
