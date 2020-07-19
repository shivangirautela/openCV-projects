import cv2   # Importing cv library
import numpy as np  # Importing numpy library for creating arrays
img = np.ones([600,600],dtype = 'uint8')*255 # Creating a variable named img to get white picture of 600*600 pixels

img[100:500,100:500] = 0 # A part of img is turned out to be black

wname = 'Canvas' # Defining my window name 
cv2.namedWindow(wname)
abc= False             # Flag by default value to be considered as False
def draw_eraser(event,x,y,flags,param): # Defining my function for mouse call back
    global abc # Variable is considered to be global so that it can used in the function

    if event == cv2.EVENT_LBUTTONDOWN: # Checking the first condition for Left Button Down Event
        abc = True # Set flag value to True indicating that left button is clicked
        cv2.rectangle(img,(x,y),(x+20,y+20),(255,255,255),-1)  # REctangle shape is drawn
    elif event == cv2.EVENT_MOUSEMOVE: # Checking the second condition for scrolling the mouse
        if (abc ==True): # Nested if to check another condition with flag being true
            cv2.rectangle(img,(x,y),(x+20,y+20),(255,255,255),-1) # REctangle shape is drawn
    else: # If none of the above conditions are met, (scrolling mouse without left click)
        abc = False  # Flag is set to default value of false
cv2.setMouseCallback(wname,draw_eraser)# Callback Method
while True: # Forever loop
    cv2.imshow(wname,img)
    key = cv2.waitKey(1) # Declaring a variable key and initializing it to a waitkey (1)
    if key == ord('q'): # 1st condition q : Quit
        break
    elif key == ord('c'): # 2nd condition c: clear
        img[100:500,100:500] = 0
    elif key == ord('w'): # 3rd condition w: writing/saving
        out = img[100:500,100:500]
        cv2.imwrite('Output Image.jpg',out)        
cv2.destroyAllWindows()
