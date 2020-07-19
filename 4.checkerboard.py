import numpy as np
import cv2
  #zeros for black
w=np.zeros([400,400,3],dtype='uint8') #width, height ,depth 3D for colors
# 2 variable = i-rows,j-columns
for i in range(0,400,100):
    for j in range(0,400,100):
        w[i:i+50,j:j+50] = [255,0,0]

for i in range(50,401,100):
    for j in range(50,401,100):
         w[i:i+50,j:j+50] = [255,0,0]
        
cv2.imshow('image',w)
cv2.waitKey(0) #0 is infinite time of wait to display window                   
cv2.destroyAllWindows()     #to help to close the window
