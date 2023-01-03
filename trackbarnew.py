import cv2
import numpy as np

def empty(a):
    pass

path='Task1A\public_test_images\maze_0.png'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)

cv2.createTrackbar("Sat Min","TrackBars",255,255,empty)

cv2.createTrackbar("Val Min","TrackBars",255,255,empty)
img_hsv=cv2.imread(path)
while True:
   
    
    #imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h=cv2.getTrackbarPos("Hue Min","TrackBars")
    
    s=cv2.getTrackbarPos("Sat Min","TrackBars")
    
    v=cv2.getTrackbarPos("Val Min","TrackBars")
    img_hsv[:]=(h,s,v)
    img_bgr=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow("frame",img_bgr)
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()




