import cv2
import numpy as np

img = np.ones([400,400,3],dtype = 'uint8')*255 #scalar multiplication for getting white color 

i = 0
j = 0+2
while True:
    cv2.line(img,(0,i),(400,0),(0,0,255),1)
    i = i+20
    j=j+1
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
