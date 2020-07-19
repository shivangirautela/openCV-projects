import cv2
import numpy as np

def nothing(x):
  pass

img = np.zeros([400,400,3],dtype='uint8')

cv2.namedWindow('color variation')
cv2.createTrackbar('red','color variation',0,255,nothing)
cv2.createTrackbar('green','color variation',0,255,nothing)
cv2.createTrackbar('blue','color variation',0,255,nothing)

while True:
    cv2.imshow('original',img)
    if cv2.waitKey(1) == ord('q'):  # or == ascii value of any key 
        break
    r = cv2.getTrackbarPos('red','color variation')
    g = cv2.getTrackbarPos('green','color variation')
    b = cv2.getTrackbarPos('blue','color variation')
    img[:,:]=[b,g,r] #BGR
       
cv2.destroyAllWindows()
