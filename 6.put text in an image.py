import cv2

img = cv2.imread('nature.jpeg')

r = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.putText(r,"Diazonic Labs",(60,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),5)

cv2.imshow('RGB Normal Image',r)

#cv2.imwrite('Duplicated RGB Image.png',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
