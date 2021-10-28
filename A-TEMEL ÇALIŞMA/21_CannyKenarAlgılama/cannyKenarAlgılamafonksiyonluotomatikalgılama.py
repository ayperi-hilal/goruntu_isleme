import cv2
import numpy as np

image=cv2.imread("kus.jpg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)

def autoCanny(blur,sigma=0.33):    #fonsiyon oluşturuyoruz(nerede,hangi durumlarda)
    median=np.median(blur)  #görüntüdeki piksel yoğunluklarının medianını hesaplıyoruz.
   #alt eşik dğeri
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0+sigma)*median))
    canny=cv2.Canny(blur,lower,upper)

    return canny

wide=cv2.Canny(blur,10,220)
tigght=cv2.Canny(blur,200,230)
auto=autoCanny(blur)


cv2.imshow("blur orjinal resim",blur)
cv2.imshow("kenarlar",np.hstack([wide,tigght,auto])) #tüm resimleri yan yana gösteriyoruz.




cv2.waitKey(0)
cv2.destroyAllWindows()