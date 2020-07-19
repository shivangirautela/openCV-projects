import cv2
import numpy as np
img = np.zeros([400,400,3],dtype = 'uint8')
wname = 'Drawing'
cv2.namedWindow(wname)
abc= False             # Flag
def draw_eraser(event,x,y,flags,param):
    global abc

    if event == cv2.EVENT_LBUTTONDOWN:
        abc = True
        cv2.rectangle(img,(x,y),(x+10,y+10),(255,255,255),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if (abc ==True):
            cv2.rectangle(img,(x,y),(x+10,y+10),(255,255,255),-1)
    else:
        abc = False
cv2.setMouseCallback(wname,draw_eraser)# Callback Method
while True:
    cv2.imshow(wname,img)
    if cv2.waitKey(1) == 27:# ASCII Esc
        break
cv2.destroyAllWindows()
