import cv2
import numpy as np

def nothing(x):
    print(x)

# create a named window
cv2.namedWindow('image')

# create trackbar and display the change in value on the screen
cv2.createTrackbar('POS','image',10,400,nothing)

switch = 'Color/Gray'
cv2.createTrackbar(switch,'image',0,1,nothing)

while True:

    img = cv2.imread('lena.jpg')

    pos = cv2.getTrackbarPos('POS','image')
    s = cv2.getTrackbarPos(switch,'image')
    cv2.putText(img,str(pos),(10,80), cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),2,cv2.LINE_AA)

    k = cv2.waitKey(1)

    if k == 27:
        break

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow('image',img)


cv2.destroyAllWindows()