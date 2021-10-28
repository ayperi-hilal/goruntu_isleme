import cv2
import numpy as np

resim1=cv2.imread("kus_boyut.jpg")
resim2=cv2.imread("kelebek_boyut.jpg")

#yeni bir resim oluşturup iki resmi üst üste koymamız gerekiyor.hadi başlayalım :)

toplam=cv2.add(resim1,resim2)
cv2.imshow("yeni resim",toplam)

agırlıkıtoplama=cv2.addWeighted(resim1,0.7,resim2,0.3,0)
cv2.imshow("ağırlılı resim",agırlıkıtoplama)

cv2.waitKey(0)
cv2.destroyAllWindows()