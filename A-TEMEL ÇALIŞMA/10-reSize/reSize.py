import cv2
import numpy as np

yukseklik=225
genislik=225

resim1=cv2.imread("kelebek.jpg")
resim2=cv2.imread("kus.jpg")
resim1_1=cv2.resize(resim1,(genislik,yukseklik))
resim2_1=cv2.resize(resim2,(genislik,yukseklik))

cv2.imshow("degişen boyutlu",resim1_1)
cv2.imwrite("kelebek_boyut.jpg",resim1_1)
cv2.imshow("degişen boyutlu",resim2_1)
cv2.imwrite("kus_boyut.jpg",resim2_1)



cv2.waitKey(0)
cv2.destroyAllWindows()