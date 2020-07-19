import cv2
import numpy as np

img = np.ones([400,400,3],dtype = 'uint8')*255 #scalar multiplication for getting white color 

wname='drawing'
cv2.namedWindow(wname)

def draw_shape(event,x,y,flags,param): #to define other values and parameters 
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),30,(255,0,0),-1)
        print(x,y)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+10,y+40),(255,0,0),-1)
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.rectangle(img,(x,y),(x+1,y+1),(255,255,255),-1)
     
cv2.setMouseCallback(wname, draw_shape) #callback method


while True:
   
    cv2.imshow(wname,img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
