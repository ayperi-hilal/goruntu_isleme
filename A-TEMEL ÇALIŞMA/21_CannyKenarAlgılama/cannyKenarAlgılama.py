import cv2
import numpy as np

image=cv2.imread("kus.jpg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)

#kenar belirleyelim.
canny=cv2.Canny(blur,50,150)

cv2.imshow("orjinal",image)
cv2.imshow("gri resim",gray)
cv2.imshow("blur resim",blur)
cv2.imshow("canny resim",canny)
cv2.waitKey()
cv2.destroyAllWindows()