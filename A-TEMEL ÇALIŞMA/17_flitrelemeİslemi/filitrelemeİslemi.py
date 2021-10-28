import cv2
import numpy as np

image=cv2.imread("resim2.jpg")

#mean filter
meanFilter=cv2.blur(image,(3,3))
meanFilter2=cv2.blur(image,(5,5))

#median filter
medianFilter=cv2.medianBlur(image,3)

#gauss filter
gauss=cv2.GaussianBlur(image,(3,3),0)




cv2.imshow("oejinal resim",image)
cv2.imshow("flitresli  resim",meanFilter)
#cv2.imshow("flitresli  resim 2",meanFilter2)


cv2.imshow("median filitreli",medianFilter)


cv2.imshow("gauss filitreli",gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()