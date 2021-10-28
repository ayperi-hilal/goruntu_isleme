import cv2
import numpy as np

resim=cv2.imread("adile.jpg")
#aynalama işlemi yapacağız.
aynalananResim=cv2.copyMakeBorder(resim,100,75,150,120,cv2.BORDER_REFLECT)
uzatılanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
sarma=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT, value=(0,0,255))


cv2.imshow("aynalanan resim",aynalananResim)
cv2.imwrite("aynalanan resim.jpg",aynalananResim) #bu kısımdaresim kaydetme yaptık .
cv2.imshow("uzatılan resim",uzatılanResim)
cv2.imshow("TERRARLANA resim",tekrarResim)
cv2.imshow("sarmal resim",sarma)
cv2.waitKey(0)
cv2.destroyAllWindows()
