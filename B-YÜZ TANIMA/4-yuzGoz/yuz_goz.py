#ayperi
import cv2
import numpy as np
#yüz göz tanımak için ilgili xml dosyaları kurulum dosyasının içerisinde mevcuttur.
#  benim dosyam aşağıdaki adreste. tabi sizinki faklı adreste olabilir.
# ilgili xml yolunu tırnak içine yapıştırarak kodu güncelleyebilirsiniz.
faceCascade=cv2.CascadeClassifier("C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
eyeCascade=cv2.CascadeClassifier("C:\Python\Lib\site-packages\cv2\data\haarcascade_eye.xml")
video=cv2.VideoCapture(0)
while True:
    ret,frema=video.read()
    gray=cv2.cvtColor(frema,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frema,(x,y),(x+w,y+h),(0,255,0),2)
        eyes=eyeCascade.detectMultiScale(gray,1.1, 5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frema,(ex,ey),(ex+ew,ey+eh),(255,1,0),4)
            
    cv2.imshow('video',frema)

    if cv2.waitKey(1) & 0xFF==ord('q'):

        break

video.release()

cv2.destroyAllWindows()

#eğer ki bu programı çalıştırdığınızda terminalde 
# [ WARN:1] global C:\Users\runneradmin\AppData\Local\Temp\pip-req-build-sn_xpupm\opencv\modules\videoio\src\cap_msmf.cpp (438) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
#hatası alırsanız cmd yi yönetici olark çalıştırıp "setx OPENCV_VIDEOIO_PRIORITY_MSMF 0" kodu yazıp enter
#diyin. bu kodu kapatıp tekrar açın. artık uyarı almayacaksınız
