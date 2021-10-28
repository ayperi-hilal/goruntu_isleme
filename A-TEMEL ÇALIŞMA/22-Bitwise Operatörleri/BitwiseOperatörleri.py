import cv2
import numpy as np

resim1=cv2.imread("kare.jpg")
resim2=cv2.imread("nokta.jpg")

#resimlerin boyutları aynı olmaz ise hata alınır bunun için resize klasörü kullanılabilir.
#and operatörü hepsi dogruiken doğru çarpma işareti aslında


cv2.imshow("kare",resim1)
cv2.imshow("nokta",resim2)
#ancak üstüste gelen pikseller beyaz lduğu zaman beyaz olur aksi taktirde siyah çıktı verir.
bit_And=cv2.bitwise_and(resim1,resim2)

cv2.imshow("bitwise",bit_And)

#or yada toplama işlemi gibi düşünülür yalnızca sıfır durumunda sıfır olu. yani her ikisi siyah olduğunda siyah olur.

bit_Or=cv2.bitwise_or(resim1,resim2)

cv2.imshow("bitwise_or",bit_Or)

#xor özel veya dır ikiside aynı olursa 0 olur onın dışında 1 olur.

bit_Xor=cv2.bitwise_xor(resim1,resim2)

cv2.imshow("bitwise_Xor",bit_Xor)

#not operatörü . bir girişin zıttını verir.
bit_Not1=cv2.bitwise_not(resim1)

cv2.imshow("bitwise_Not_1",bit_Not1)
bit_Not2=cv2.bitwise_not(resim2)

cv2.imshow("bitwise_Not_2",bit_Not2)


cv2.waitKey(0)
cv2.destroyAllWindows()