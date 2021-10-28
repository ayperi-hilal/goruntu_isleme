import cv2
import numpy as np

resim=cv2.imread("hababam.jpg")

#resim[0:20,0:30,1]=255#[y,x] koordinatlarıdır.
#köşeli parantezler hep y,x dir.
cv2.rectangle(resim,(100,150),(130,50),[0,0,255],3)#(),() içlerindeki değeri değiştirerek karenin veya diktörgenin yeri değiştirilir.[] içerindeki değer renk sıkalasıdır. diğer sayı ise kalınlık öçüsüdür.
cv2.imshow("hababam sinifi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

