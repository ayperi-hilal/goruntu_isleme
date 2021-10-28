import cv2
import numpy as np

image=cv2.imread("kelebek.jpg",0)

ret,thres1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)#127nin altındaki pikseller sıfıra yuvaralanacak. diğerleri ise255 yuvarlanacak.
ret,thres2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thres3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thres4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thres5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("orjinal resim",image)
cv2.imshow("thres1 resim",thres1)
cv2.imshow("thres2 resim",thres2)
cv2.imshow("thres3 resim",thres3)
cv2.imshow("thres4 resim",thres4)
cv2.imshow("thres5 resim",thres5)

cv2.waitKey()
cv2.destroyAllWindows()