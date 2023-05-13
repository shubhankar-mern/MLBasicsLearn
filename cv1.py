## Simple Program to read and show an Image

import cv2

img = cv2.imread('./abc.jpg')


cv2.imshow('senery',img)


cv2.waitKey(0)
cv2.destroyAllWindows()