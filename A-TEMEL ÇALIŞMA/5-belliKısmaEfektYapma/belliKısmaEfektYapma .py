import cv2
import numpy as np


resim=cv2.imread("kemal.jpg")
#renk tonlamasında sırasıyla BGR kullanılır.

resim[50:80,140:200,0]=255 #[y ekseni,x ekseni, renk katagorisi]=katagoriye atanan değer
resim[50:80,140:200,2]=255 
#göz kısımlarına ilgili efekt yansıtıldı.
cv2.imshow("kemal sunal",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
