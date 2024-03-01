import cv2
import numpy as np

img = cv2.imread("resources/lambo.png")
img_resize = cv2.resize(img, (300, 200))

img_cropped = img[0:200, 200:500]


print(f"Original image: {img.shape}\nResize image: {img_resize.shape}")
cv2.imshow("Image", img)
cv2.imshow("Image resize", img_resize)
cv2.imshow("Image cropped", img_cropped)
cv2.waitKey(0)