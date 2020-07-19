import cv2
import numpy as np

img = np.ones([400,400,3],dtype = 'uint8')*255


while True:
    cv2.circle(img,(100,100),50,(0,0,255),5)
    cv2.line(img,(250,10),(400,10),(255,0,0),5)
    cv2.rectangle(img,(300,250),(190,170),(0,255,0),-4) # ive for filling colors 

    cv2.imshow('Image',img)
    if cv2.waitKey(10e7):
        break
cv2.destroyAllWindows()
