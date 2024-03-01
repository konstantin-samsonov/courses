import cv2
import numpy as np

frame_width = 1200
frame_height = 800
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

my_colors = [
    [97, 111, 113, 140, 164, 207],  # blue
    [50, 81, 77, 69, 255, 143],  # green
    [0, 173, 182, 39, 215, 249]  # yellow
]

my_colors_value = [
    [255, 0, 0],
    [0, 128, 0],
    [255, 195, 11]
]

my_points = []  # [x, y, color_id]


def find_colors(img, my_colors, my_colors_value):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in my_colors:
        lower = np.array([color[0:3]])  # min: hue/sat/value
        upper = np.array([color[3:6]])  # max: hue/sat/value
        mask = cv2.inRange(img_hsv, lower, upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = get_contours(mask)
        cv2.circle(img_result, (x, y), 10, my_colors_value[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, count])
        count += 1
    return new_points


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y


def draw_on_canvas(my_points, my_color_values):
    for point in my_points:
        cv2.circle(img_result, (point[0], point[1]), 10, my_colors_value[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = find_colors(img, my_colors, my_colors_value)
    if len(new_points) != 0:
        for new_p in new_points:
            my_points.append(new_p)

    if len(my_points) != 0:
        draw_on_canvas(my_points, my_colors_value)

    cv2.imshow("Results", img_result)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
