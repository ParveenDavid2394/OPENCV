import cv2
import numpy as np

img = cv2.imread('lena.jpg',1)

# create a black img using numpy
#img = np.zeros([512,512,3])

# override img to draw line
img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)    # (B, G, R)

# draw a rectangular line
img = cv2.rectangle(img, (0, 0), (200, 200), (255, 0, 0), 3) # thickness = -1 for covering the place with bgr color

# draw a circle
img = cv2.circle(img, (255, 100), 100, (0,255,0), 2)

# draw an arrowed line
img = cv2.arrowedLine(img, (0,255), (255,255), (255,156,30), 3)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'Lena', (10, 500), font, 4, (255,255,255), 5, cv2.LINE_AA) # font, font size = 4

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()