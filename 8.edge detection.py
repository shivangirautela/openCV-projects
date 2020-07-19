import cv2
img = cv2.imread('C:/Users/Shivangi rautela/Desktop/GM-Sudoku2.png',0)

sobel_x = cv2.Sobel(img,cv2.CV_8U,dx =1 ,dy =0 ,ksize=-1) # scraping thorugh y axis 
sobel_y = cv2.Sobel(img,cv2.CV_8U,dx =0 ,dy =1 ,ksize=-1) # scraping thorugh x axis
sobel_f = cv2.bitwise_or(sobel_x,sobel_y) #convolusion multiply and add bitwise

canny = cv2.Canny(img,127,255) 

cv2.imshow('original image',img)
cv2.imshow('Sobel X image',sobel_x)
cv2.imshow('Sobel Y image',sobel_y)
cv2.imshow('Sobel total image',sobel_f) #final image
cv2.imshow('Canny Edge',canny) 
#Laplacian
cv2.waitKey(0)
cv2.destroyAllWindows()

#applications of edge detection
#camscanner for cropping and scanning 
#self driving cars for identifying objects 


