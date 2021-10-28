import cv2
import numpy as np

cocuk_resmi= cv2.imread("cocuklar.jpg")

kesit=cocuk_resmi[50:150,50:150]

#cv2.imshow("kesit",kesit)
print(cocuk_resmi.shape)
cocuk_resmi[0:100,0:100]=kesit
cocuk_resmi[: , : ,0]=200

cv2.imshow("cocuk bayrami",cocuk_resmi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#yapıştırma noktasında boyutlar çok önemli yoksa sürekli bir hata alma durumu olacaktır.