import cv2
import numpy

print(cv2.__version__)
print(numpy.__version__)

# reading jpg file using cv2
img = cv2.imread('lena.jpg', 1)  # flag: 1 for color, 0 for grayscale, -1 for original plus alpha channel

cv2.imshow('lena', img)

k = cv2.waitKey(00)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
