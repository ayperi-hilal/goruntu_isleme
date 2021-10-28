import cv2
import numpy as np

image=cv2.imread("yazi.jpg")
#gürültü giderme diration genişletme
kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(image,kernel,iterations=1)
#cv2.imshow("dilation",dilation)
#cv2.imshow("orjinal resim",image)

#gürültü giderme erotion azaltma

erosion=cv2.erode(image,kernel,iterations=1)
#cv2.imshow("rosion",erosion)
#cv2.imshow("orjinal resim",image)

#erotion üzerine diretion yapalım.
erosion=cv2.erode(image,kernel,iterations=1)
#cv2.imshow("rosion",erosion)
#cv2.imshow("orjinal resim",image)


dilation=cv2.dilate(erosion,kernel,iterations=1)
cv2.imshow("dilation",dilation)
cv2.imshow("orjinal resim",image)


cv2.waitKey(0)
cv2.destroyAllWindows()