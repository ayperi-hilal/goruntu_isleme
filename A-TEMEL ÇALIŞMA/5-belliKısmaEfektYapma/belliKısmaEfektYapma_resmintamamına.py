import cv2
import numpy as np


resim=cv2.imread("kemal.jpg")
#renk tonlamasında sırasıyla BGR kullanılır.#[y ekseni,x ekseni, renk katagorisi]=katagoriye atanan değer
resim[:,:,0]=500 #resme kırmızı ve yeşili aynı kalmak kaydı ile mavi tonuna değer atadık.0,1,2 diye değerler verilir.
resim[:,:,1]=200 #resme yeşil efekti verir.
#resim[:,:,2]=20#resme kırmızı efekti verir.
#eşitlenen sayı değerleri tonu ifade eder ve [0,255] arası değer alır.

cv2.imshow("kemal sunal",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
