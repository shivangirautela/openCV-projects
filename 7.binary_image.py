import cv2

img = cv2.imread('nature.jpeg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)


cv2.imshow('original Image',img)
cv2.imshow('grayscale image',gray)
cv2.imshow('binary image',binary)

cv2.waitKey(0)
cv2.destroyAllWindows()

#binary means black and white
#colorfull -> gray -> black
