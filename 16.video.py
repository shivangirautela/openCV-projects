import cv2

cap = cv2.VideoCapture(0)  #0 for laptop web cam 

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('output',frame)
    if cv2.waitKey(1) == 13:
        break
    
if cap.isOpened():
    _,frame = cap.read()
cv2.imshow('output',frame)
cv2.waitKey(0)
        
cap.release() #release web cam port to avoid damage 
cv2.destroyAllWindows()
