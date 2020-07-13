import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)

# create a black img using numpy
img = np.zeros([512,512,3])

# override img to draw line
img = cv2.line(img, (0,0), (640,640), (255,0,0), 5)

# draw a rectangular line
img = cv2.rectangle(img, (0, 0), (200, 200), (255, 0, 0), 3) # thickness = -1 for covering the place with bgr color

img = cv2.circle(img, (255, 255), 150, (0,255,0), 2)
img = cv2.arrowedLine(img, (640,640), (100,300), (255,156,30), 3)
img = cv2.rectangle(img, (384,0), (500,100), (0,0,255), 3)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'Lena', (100, 500), font, 3, (255,255,255), 3)

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()