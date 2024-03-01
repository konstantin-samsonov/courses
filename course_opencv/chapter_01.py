import cv2

# Image
# img = cv2.imread("resources/test_image.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Video and Webcam
# cap = cv2.VideoCapture("resources/test_video.mp4")
cap = cv2.VideoCapture(0) # webcam
cap.set(3, 640) # frameWidth
cap.set(4, 480) # frameHeight


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
