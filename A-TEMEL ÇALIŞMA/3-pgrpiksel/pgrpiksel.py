import cv2
import numpy as np

kurtresmi=cv2.imread("kurt.jpg")

cv2.imshow("kurt resmi",kurtresmi)
print(kurtresmi[(230,80)])#belli bir kısmını görmek istiyoruz.

print("resmin boyutu:"+str(kurtresmi.size)) #yazı ile alınan değerler aynı olmalı yoksa hata veriyor.
print("resmin özekkikleri:"+str(kurtresmi.shape))
print("resmin veritipi:"+str(kurtresmi.dtype))




cv2.waitKey(0)
cv2.destroyAllWindows()

