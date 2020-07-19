#1.opencv library 2. xml file 3.photo 4.haarcascade classification algo for facial recognition
import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    f = face.detectMultiScale(gray,scaleFactor =1.1,minNeighbors =8) #scale factor grater than 1 always ,  keep highest possible neighbors of faces 

    for x,y,w,h in f: # x,y are facial coordinates which we get from f and w,h are width and height unknown 
        img = cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),2)
        cv2.imshow('Faces Recognized',img)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
