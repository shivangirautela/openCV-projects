import cv2

def nothing(x):
    pass

img = cv2.imread('nature.jpeg',0)
cv2.namedWindow('Cannyt')
cv2.createTrackbar('Thresh 1','Cannyt',0,255,nothing)
cv2.createTrackbar('Thresh 2','Cannyt',0,255,nothing)
while True:
    thresh1 = cv2.getTrackbarPos('Thresh 1','Cannyt')
    thresh2 = cv2.getTrackbarPos('Thresh 2','Cannyt')
    canny = cv2.Canny(img,thresh1,thresh2)
    cv2.imshow('Original Image',img)
    cv2.imshow('Canny Edge',canny)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
