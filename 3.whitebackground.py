import numpy as np
import cv2
  #300 pixels
b=np.ones([300,300,3],dtype='uint8') #width, height ,depth 3D for colors
b[0:300,0:300]=[119,168,87] #BGR scale
b[100:200,0:300]=[0,0,255]
b[200:300,0:300]=[0,255,0]
print(b)
print(b.dtype)
print(b.ndim)

cv2.imshow('Red Background',b)
cv2.waitKey(0) #0 is infinite time of wait to display window                   
cv2.destroyAllWindows()     #to help to close the window

#0- lowest value
#255- highest value
#dtype - int32,int16,int8,int4,int2
#range of datatypes: int(-as well as+) -127 to 128
#uint8 - 0 to 255
#for uint16 - 0 to 655342 do for red take 65543 instead of 255.
