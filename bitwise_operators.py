import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)

img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

# compares the white are and black areas in both images
# only regions where both white and both black intersects is retained
# perform bitwise AND operation on both img1 and img2
bitAnd = cv2.bitwise_and(img1,img2)

# perform bitwise OR operation on both img1 and img2
# white treated as 1 and black treated as 0
bitOr = cv2.bitwise_or(img1,img2)

# use bitwise XOR
# 1 & 1 or 0 & 0 = 0, if 1 & 0 or vice versa = 1
bitXOR = cv2.bitwise_xor(img1,img2)

# use bitwise NOT
# takes only 1 input
# gives the opposite
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOr',bitOr)
cv2.imshow('bitXOR',bitXOR)
cv2.imshow('bitNOT1',bitNot1)
cv2.imshow('bitNOT2',bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()