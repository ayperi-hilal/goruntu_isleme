import cv2
import numpy as np


resim1=cv2.imread("joker.jpg")
resim1[50,30]=[255,255,255]#ilgili piksel değeri ni [255,255,255] değeri ile değiştirdik.resimde küçük bir yer beyaz oluyor.
#belli bir alan için çalışma yapmak için for döngüsü oluşturulu
for i in range(100):#100 px sağa doğru çizdi çekiyor.
    resim1[70,i]=[255,255,255] #satırın başında girinti olması önemli aksi taktirde yanlış hata veriyor.

cv2.imshow("jokerin resmi",resim1)

cv2.waitKey(0)
cv2.destroyAllWindows()