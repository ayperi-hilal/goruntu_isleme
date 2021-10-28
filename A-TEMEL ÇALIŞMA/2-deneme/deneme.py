import cv2
import numpy as np 
## import numpy as np  demek numpy bundan sonra np olarak ta anılacaktır.
resim1=cv2.imread("logo.png")# bu kısımda resmi olduğu gibi okumaktadır.
resim2=cv2.imread("kus.jpg")
resim3=cv2.imread("logo.png",0) #bu kısımda ise renkleri kullanmayacaktır. ve siyah beyaz bir resim olacaktır.
##resim değişkenine resimi aktardık.sadece burada okuma işlemi yapılıyor.
cv2.imshow("KUS",resim2) #resim gösterilir
#cv2.imshow("gosterilecek resim",resim)#resim gösterilir.
#cv2.imwrite("siyah_beyaz_resim.jpg",resim)#elde edilen resim aynı klasöre istenilen isimdeve uzantıda kayıt edildi.
#print(resim) #resmin herir pikselinin değernin termnal kısmında verecektir.
print(resim1.size) #resmin boyutunu verecektir.
print(resim2.dtype) #resmin tipini verecektir.
print(resim3.shape)#resim bilgisini veriri.(genişlik, yükseklik. kanalsayısını) verir.
cv2.waitKey(0) ## resim açıldığında beklemesi içindir. herhangi bi tuşa basana kadar resim ekranda kalır.
cv2.destroyAllWindows() ##"x" işaretine basıldığında tüm opencv pencereleri kapanır.
