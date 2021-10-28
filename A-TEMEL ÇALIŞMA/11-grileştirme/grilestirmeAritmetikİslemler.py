import cv2
import numpy as np
resim1=cv2.imread("kelebek.jpg")
resim2=cv2.imread("kus.jpg")
#grileştirme işlemi yapacağız şimdi
resimgri=cv2.cvtColor(resim1,cv2.COLOR_BGR2GRAY)
resim11=resim1[: ,:,0]

cv2.imshow("sıfırlı resm",resim11)

cv2.imshow("ilk resim",resim1)

cv2.imshow("grileştirilmiş",resimgri)

#bu çalışmada iki farklı gri resim elde ettik.

#şimdi elde edilen resimlerin yükseklik genişlik ve kanal sayılarını çıkartmamız gerekmektedir.
#bakalım ne gibi değişilkikler oldu

yukseklik,genislik,kanalSayisi=resim1.shape

print("orjinal",yukseklik,genislik,kanalSayisi)

#grileştirince kanal sayısı 1 olacağından shape hata verir.
yukseklik,genislik=resim11.shape
print("sıfırlı",yukseklik,genislik)
yukseklik,genislik=resimgri.shape
print("gri",yukseklik,genislik)
cv2.waitKey(0)
cv2.destroyAllWindows()