import cv2
import numpy as np

# pin a circle when left click on mouse & join the circle with lines
# then when right click on an image display the color at that specific point

def click_event(event, x, y, flag, param):
    font = cv2.FONT_HERSHEY_COMPLEX

    if event == cv2.EVENT_LBUTTONDOWN:
        # create circle
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        # record the coordinates of clicked points
        points.append((x,y))
        # if more than 2 points then can start to connect them one after another
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 5)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)

        # create a new image to display the color where the mouse is clicked
        colorImg = np.zeros([512,512,3], np.uint8)
        colorImg[:] = [blue,green,red]
        # display the color in new window
        cv2.imshow('Color',colorImg)


#img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('lena.jpg')

cv2.imshow('image', img)

# function to catch mouse events
cv2.setMouseCallback('image', click_event)

# create list to remember points
points = []

cv2.waitKey(0)
cv2.destroyAllWindows()
