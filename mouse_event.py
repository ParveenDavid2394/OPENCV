import cv2
import numpy as np

# check the available mouse click events in cv2 library
# events = [i for i in dir(cv2) if 'EVENT' in i]

# for event in events:
#     print(event)

def click_event(event, x, y, flag, param):
    font = cv2.FONT_HERSHEY_COMPLEX

    if event == cv2.EVENT_LBUTTONDOWN:
        # x and y are provided by the MouseCallback
        textXY = '{0},{1}'.format(x, y)
        cv2.putText(img, textXY, (x, y), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        # in general we say 1280p x 720p which is [width, height] but
        # image matrix store in [height, width, channel] / [y, x, channel]
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        textBGR = '{0},{1},{2}'.format(blue, green, red)
        cv2.putText(img, textBGR, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)


# img = np.zeros([512, 512, 3], np.uint8)
# img = cv2.imread('lena.jpg')
img = cv2.imread('messi5.jpg')

cv2.imshow('image', img)

# function to catch mouse events
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
