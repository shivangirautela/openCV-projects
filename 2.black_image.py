import numpy as np
import cv2
  #10 pixels
b=np.zeros([300,300],dtype='int16')
print(b)
print(type(b))
cv2.imshow('Black Backgroud',b)

cv2.waitKey(0) # 0 is infinite time of wait to display window
                            
cv2.destroyAllWindows()     # to help to close the window

