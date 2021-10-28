import cv2
import numpy as np

cocuk_resmi= cv2.imread("cocuklar.jpg")

kesit=cocuk_resmi[50:150,50:150]

#cv2.imshow("kesit",kesit)
print(cocuk_resmi.shape)
cocuk_resmi[0:100,0:100]=kesit
#resmin belli bir alanını boyadık.
cocuk_resmi[10:30 , 30:50]=(0,150,255)#bgr 


cv2.imshow("cocuk bayrami",cocuk_resmi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#yapıştırma noktasında boyutlar çok önemli yoksa sürekli bir hata alma durumu olacaktır.