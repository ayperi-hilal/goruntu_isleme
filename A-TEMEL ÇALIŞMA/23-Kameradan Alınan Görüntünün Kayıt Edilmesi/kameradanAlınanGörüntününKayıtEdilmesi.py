import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
width=int(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))

#videonun genişlik ve yüksekliğini terminale yazalım
print(width,height)
#kod çözücü yazmamız lazım.
fourcc=cv2.VideoWriter_fourcc(*'MP4V')
#VideoWriter_fourcc İLE VideoWriter KARIŞTIRLMAMALIDIR arasındaki fark vardır.önce uzantı belirledik. işmdi kayıt yapıyoruz.
writer=cv2.VideoWriter("kayıt.mp4",fourcc,20,(width,height))#isim, kod çözücü(VideoWriter_fourcc) kısmı ,kayıt hızı,genişlik,yükseklik


while True:

    ret,goruntu=kamera.read()
    writer.write(goruntu)#yularıda yerini ve formatını belirlediğimz videoyu buradan almasını sağladık.

    cv2.imshow("kamera kaydı",goruntu)

    if cv2.waitKey(20) & 0xFF==ord("1"):
        break
#buraya kadar video açtık.

kamera.release()
writer.release()

cv2.destroyAllWindows()