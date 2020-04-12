#invisibility cloak
import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
time.sleep(1)

lower_blue =np.array([100,150,0])
upper_blue = np.array([140,255,255])

for i in range(60):
    r1,bg=cap.read()
    if not r1:
        continue
while(cap.isOpened()):
    r2,img = cap.read()
    if not r2:
        break
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((1,1), np.uint16)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=10)
    mask = cv2.dilate(mask, kernel, iterations=20)
    mask1 = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(bg, bg, mask = mask) #extracts the bg in the desired location 
    res2 = cv2.bitwise_and(img, img, mask=mask1) #filters the desired colored object
    
    op = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow('invisibility', op)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()

    
    
