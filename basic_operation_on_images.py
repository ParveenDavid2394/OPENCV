import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
imgROI = cv2.imread('messi5.jpg')

# print image shape in (rows,columns,channel) format
print(img.shape)

# print image size = total num of pixels
print(img.size)

# print the datatype of the image
print(img.dtype)

# split the image into individual channels
i = cv2.split(img)
b, g, r = i
print(b,g,r)

# merge back all the channels using merge
img = cv2.merge((b,g,r))
print(img)

# add 2 images together
# 2 methods, cv2.add and cv2.addWeighted
# 1st methog -> add
img2 = cv2.imread('opencv-logo.png')

# make sure both pic are in same size before add
# so use resize option

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# now can add
dst = cv2.add(img,img2)

# method 2 -> addWeighted
# alpha + beta = 1 and gamma = scalar number
dstW = cv2.addWeighted(img,0.5,img2,0.5,0)

# ROI = region of interest
# choose points of interest first to extract
ball = imgROI[280:340, 330:390]

# then replace back in new points
imgROI[280:340, 70:130] = ball

cv2.imshow('add',dst)
cv2.imshow('addWeighted',dstW)
cv2.imshow('ROI', imgROI) # has another ball in the pic
cv2.waitKey(0)
cv2.destroyAllWindows()