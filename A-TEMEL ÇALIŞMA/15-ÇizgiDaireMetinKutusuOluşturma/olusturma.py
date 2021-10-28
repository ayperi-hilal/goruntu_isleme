import cv2
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")
#çizgi çekelim
cv2.line(resim,(0,0),(100,100),(20,60,255),3)

cv2.imshow("deneme line ",resim)
#daire oluşturalım
cv2.circle(resim,(150,150),25,(0,255,0),3,)
cv2.imshow("deneme line ",resim)

#metin kutusu oluşturalım.
cv2.putText(resim,("yazı kutusu"),(50,200),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0))#resim,yazılacak yazı,konumu,yazıtipi,YAZI BOYUTU,RENK
cv2.imshow("deneme line ",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()