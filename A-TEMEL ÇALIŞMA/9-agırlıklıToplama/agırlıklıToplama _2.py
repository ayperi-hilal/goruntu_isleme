import cv2
import numpy as np

resim1=cv2.imread("kus_2.jpg")
resim2=cv2.imread("kus.jpg")

cv2.imwrite("resim1.jpg",resim1)
cv2.imwrite("resim2.jpg",resim2)
#cv2.imshow("resim2",resim2)
#cv2.imshow("kus",resim2)

#yeni bir resim oluşturup iki resmi üst üste koymamız gerekiyor.hadi başlayalım :)

#toplam=cv2.add(resim1,resim2)
#cv2.imshow("yeni resim",toplam)

agırlıkıtoplama=cv2.add(resim1,0.7,resim2,0.3,0)
cv2.imshow("ağırlılı resim",agırlıkıtoplama)

cv2.waitKey(0)
cv2.destroyAllWindows()

#burada hata alıyorum çünkü resim boyutları aynı değil . hadi gelin önce resize operatörüne bakalım.