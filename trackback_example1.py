import cv2
import numpy as np


# prints the x points when trackbar pos changes
def nothing(x):
    print(x)

# create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbar for each color
# nothing is the function call back when the trackbar changes
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# create a switch trackbar
switch = 'ON <--> OFF'
cv2.createTrackbar(switch,'image',0,1, nothing)

while True:

    cv2.imshow('image', img)
    k = cv2.waitKey(1)

    if k == 27:
        break

    # gets the changes on trackbar
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')

    # use condition if switch == 1 then can change color
    s = cv2.getTrackbarPos(switch,'image')
    if s == 1:
        # changes on each color is set on the img image
        img[:] = [b,g,r]
    else:
        img[:] = 0

cv2.destroyAllWindows()
