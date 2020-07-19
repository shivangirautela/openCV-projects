import cv2

img = cv2.imread('C:/Users/Shivangi rautela/Desktop/types_of_inheritance.jpg')

img[0:50,0:50]=[0,0,0]
print(img.shape)
print(img)
print(img.size)


cv2.imshow('Image',img)
cv2.imwrite('duplicate image.jpg',img) #writing an image
cv2.waitKey(0)
cv2.destroyAllWindows()

