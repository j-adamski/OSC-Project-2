import cv2
import numpy as np

img=np.zeros((512,512,3), np.uint8)
cv2.rectangle(img,(0,0),(500,500),(80,100,100),1000)
cv2.putText(img,'TO',(25,200),cv2.FONT_HERSHEY_SIMPLEX,6,(0,230,240), thickness=15)
cv2.putText(img,'DO',(220,200),cv2.FONT_HERSHEY_SIMPLEX,6,(230,160,0),thickness=15)

cv2.line(img,(390,120),(400,170),(0,230,240),15)
cv2.line(img,(400,170),(480,50),(0,230,240),15)
cv2.line(img,(420,165),(485,63),(80,100,100),8)
cv2.line(img,(418,120),(499,-2),(80,100,100),7)

cv2.imshow('Logo',img)
cv2.resizeWindow('Logo', 500,350)

cv2.waitKey(0)

