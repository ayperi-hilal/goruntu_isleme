import cv2
import numpy as np

kamera=cv2.VideoCapture(0) #kendi bilgisayarın kamerası 0, usb ile bağlantı kurulan kameralar için 1, dahil edilen videodan görsel almak için 2 yazılır.

#video demek ard arda çekilmiş resimleden olşur ve bir döngü oluşturur bu nedenle while kullanıyoruz.

while True:
#ret kameranın çalıştığını kontrol ediyor.
    ret,goruntu=kamera.read()
    cv2.imshow(" alınan video",goruntu)
#görüntünün bir viedeo olması için waitkey yazıcaz.() parantez içine yazan yavaşlık-akıcılık hızı olacak
    if cv2.waitKey(30) & 0xFF==ord('1'): ##1 ya basana kadar video almaya devam edecek.

     break

kamera.release()

cv2.destroyAllWindows()