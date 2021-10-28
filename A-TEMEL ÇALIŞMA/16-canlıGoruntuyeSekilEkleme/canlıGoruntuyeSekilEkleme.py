import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.rectangle(goruntu,(100,100),(200,200),(0,20,60),2)
    cv2.line(goruntu,(120,120),(200,200),(0,0,255))
    cv2.circle(goruntu,(152,180),4,(0,0,255))
    cv2.putText(goruntu,"yazı",(250,250),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),1)
    cv2.imshow("kamera kaydı",goruntu)

    if cv2.waitKey(20) & 0XFF==ord('1'):
        break

kamera.release()# kamera serbest bırakılır.
 
cv2.destroyAllWindows()