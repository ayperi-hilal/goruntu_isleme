import cv2
import numpy as np

image=cv2.imread("kelebek.jpg",0)
#SİMPLE THRESHHOLDİNG
ret,thresh1=cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#adaptive thresholding

thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                cv2.THRESH_BINARY,11,2)

cv2.imshow("orjinal",image)
cv2.imshow("simple thresh",thresh1)
cv2.imshow("adaptive thresholding",thresh2)



cv2.waitKey()
cv2.destroyAllWindows()